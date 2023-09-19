from flask import Flask, render_template, request
from links import Links

app = Flask(__name__)


class Settings:
    debug = False
    url = "http://sssvpn.ru"
    url_support = "https://t.me/+hU9vIxKbtwg3ZGI6"
    # host = "127.0.0.1"
    host = "5.104.108.237"
    port = "14983"
    password = "238938"
    encription = "AES-256-GCM"
    ss_link = "ss://YWVzLTI1Ni1nY206MjM4OTM4@5.104.108.237:14983/#sssvpn.ru"


@app.route("/")
def index():
    ip_addr = request.remote_addr
    check = ip_addr == Settings.host
    return render_template(
        "index.html",
        settings=Settings,
        links=Links,
        ip_addr=ip_addr,
        check=check,
    )


if __name__ == "__main__":
    app.run(debug=Settings.debug, host="0.0.0.0", port=5000)
