import psutil
import time
from threading import Thread

import os


def bytes2human(n):
    # http://code.activestate.com/recipes/578019
    # >>> bytes2human(10000)
    # '9.8K'
    # >>> bytes2human(100001221)
    # '95.4M'
    symbols = ("K", "M", "G", "T", "P", "E", "Z", "Y")
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return "%.1f%s" % (value, s)
    return "%sB" % n


class TFilter:
    # переменные для фильтра калмана
    varVolt = 0.25  # среднее отклонение (ищем в excel)
    varProcess = 0.1  # скорость реакции на изменение (подбирается вручную)
    Pc = 0.0
    G = 0.0
    P = 1.0
    Xp = 0.0
    Zp = 0.0
    Xe = 0.0

    def filter(self, val):  # функция фильтрации
        self.Pc = self.P + self.varProcess
        self.G = self.Pc / (self.Pc + self.varVolt)
        self.P = (1 - self.G) * self.Pc
        self.Xp = self.Xe
        self.Zp = self.Xp
        self.Xe = self.G * (val - self.Zp) + self.Xp  # "фильтрованное" значение

        return self.Xe


# класс получающий текущее количество переданных и принятых байт
class TByteCounter:
    old_num_bytes = {}
    filters = {}

    # конструктор
    def __init__(self):
        interfaces_list = self.get_all_interfaces()

        for interface in interfaces_list:
            self.old_num_bytes[interface] = {"in": 0, "out": 0}
            filterIn = TFilter()
            filterOut = TFilter()
            self.filters[interface] = {"in": filterIn, "out": filterOut}

    # возвращает словарь с значениями переданных
    # и принятых байт считая от последнего запроса
    def get_num_bytes(self):
        iostat = psutil.net_io_counters(pernic=True)
        new_num_bytes = {}

        for interface in iostat:
            current = {"in": iostat[interface][1], "out": iostat[interface][0]}
            new_num_bytes[interface] = {
                "in": iostat[interface].bytes_recv - self.old_num_bytes[interface]["in"],
                "out": iostat[interface].bytes_sent
                - self.old_num_bytes[interface]["out"],
            }
            self.old_num_bytes[interface] = current

        return new_num_bytes

    # возвращает все интерфейсы системы
    def get_all_interfaces(self):
        iostat = psutil.net_io_counters(pernic=True)
        interfaces_list = []
        for key in iostat:
            interfaces_list.append(key)
        return interfaces_list


# функция для бесконечного потока с опросом скорости
def main_counter(interval=1):
    global CURRENT_SPEED_MBit
    t0 = 0
    byte_counter = TByteCounter()
    MBit = 125000  # константа-делитель для перевода байт в мегабиты
    while True:
        num_bites = byte_counter.get_num_bytes()
        interfaces_list = byte_counter.get_all_interfaces()
        t1 = time.perf_counter() - t0
        for interface in interfaces_list:
            in_speed_mbit = round(num_bites[interface]["in"] / t1 / MBit, 3)
            out_speed_mbit = round(num_bites[interface]["out"] / t1 / MBit, 3)
            CURRENT_SPEED_MBit[interface] = {
                "Incoming": in_speed_mbit,
                "Outgoing": out_speed_mbit,
            }

        # print (t1)
        # print(CURRENT_SPEED_MBit)
        t0 = time.perf_counter()  # засекаем время
        time.sleep(interval)  # засыпаем


# функция для бесконечного потока с опросом дисков
def main_partitions(interval=600):
    global CURRENT_PARTITIONS
    while True:
        array_partitions = []
        for part in psutil.disk_partitions(all=False):
            if os.name == "nt":
                if "cdrom" in part.opts or part.fstype == "":
                    # skip cd-rom drives with no disk in it; they may raise
                    # ENOENT, pop-up a Windows GUI error for a non-ready
                    # partition or just hang.
                    continue
            usage = psutil.disk_usage(part.mountpoint)
            array_partitions.append(
                {
                    "partition": part.device + " " + bytes2human(usage.total) + "",
                    "used": usage.percent,
                    "free": 100 - usage.percent,
                }
            )

        CURRENT_PARTITIONS["partitions"] = array_partitions
        print(CURRENT_PARTITIONS)
        time.sleep(interval)


def get_partitions_info():
    p = psutil.disk_partitions()
    return p


#########################################################################################


# словарь для храения текущей скорости всех интерфейсов
CURRENT_SPEED_MBit = {}
CURRENT_PARTITIONS = {}

# описываем и стартуем поток опроса скорости интерфейсов
speed_thrd = Thread(target=main_counter, daemon=True, args=(0.3,))
speed_thrd.start()

# описываем и стартуем поток опроса дисков
partitions_thrd = Thread(target=main_partitions, daemon=True, args=(6,))
partitions_thrd.start()


# app = Flask(__name__)


# @app.route("/")
# def plot_graph():
#     interf = request.args.get("interface")

#     # если активный интерфейс не задан явно,
#     # то делаем активынм самый загруженный интерфейс
#     if interf is None:
#         x = 0
#         keys = list(CURRENT_SPEED_MBit.keys())
#         active_interface = keys[0]
#         for interface in CURRENT_SPEED_MBit.keys():
#             y = (
#                 CURRENT_SPEED_MBit[interface]["Incoming"]
#                 + CURRENT_SPEED_MBit[interface]["Outgoing"]
#             )
#             print(y)
#             if y > x:
#                 active_interface = interface
#                 x = y
#     else:
#         active_interface = interf
#     # -----------------------
#     CURRENT_PARTITIONS["id"] = "part"
#     return render_template(
#         "plot.html",
#         active_interface=active_interface,
#         interfaces=CURRENT_SPEED_MBit.keys(),
#         partitions=CURRENT_PARTITIONS,
#     )


# возвращает JSON со значением текущей скорости заданного интерфейса
@app.route("/get_speed", methods=["GET"])
def get_speed():
    interf = request.args.get("i")
    CURRENT_SPEED_MBit[interf]["id"] = "speed"
    return (
        json.dumps(CURRENT_SPEED_MBit[interf]),
        200,
        {"Content-Type": "application/json"},
    )


# # возвращает массив с дисками
# @app.route("/get_partitions", methods=["GET"])
# def get_partition():
#     CURRENT_PARTITIONS["id"] = "part"
#     return json.dumps(CURRENT_PARTITIONS), 200, {"Content-Type": "application/json"}
