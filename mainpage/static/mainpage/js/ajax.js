$(document).ready(function () {
    setInterval(function () {
        // AJAX - запрашивает у сервера обновленный ip клиента раз в 2 секунды
        $.ajax({
            url: '/update_ip/',
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                // Обработка полученных данных
                $('#ip').text("Ваш IP: " + data.ip);
                var x = data.check_ip
                html_warning = 'Статус подключения: <span class="badge rounded-pill bg-warning text-dark">НЕ ПОДКЛЮЧЕН</span>. Сначала подключитесь к VPN, а затем попробуйте открыть заблокированные Роскомнадзором ресурсы:'
                html_success = 'Статус подключения: <span class="badge rounded-pill bg-success">ПОДКЛЮЧЕН</span>. Теперь вы можете открывать заблокированные Роскомнадзором ресурсы. Помните, если какой-то сайт не открывается, это еще не значит что проблема в VPN - в наше время все возможно, пробуйте открыть другие ресурсы.'
                if (x) {
                    $('#test').html(html_success)
                    $("#tablet").css("display", "block");
                    $("#logo").attr("src", $("#logo").attr("src_success"))
                } else {
                    $('#test').html(html_warning)
                    $("#tablet").css("display", "none");
                    $("#logo").attr("src", $("#logo").attr("src_no-link"))            
                }

            }
        });
    }, 2000);
});
