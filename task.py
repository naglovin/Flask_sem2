# Создать страницу, на которой будет форма для ввода имени и электронной почты,
# при отправке которой будет создан cookie-файл с данными пользователя,
# а также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.
#
# На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет удалён cookie-файл
# с данными пользователя и произведено перенаправление на страницу ввода имени и электронной почты.


from flask import Flask, request, make_response, render_template, session, redirect, url_for

app=Flask(__name__)
app.secret_key = '555n4ndmfgdngl4jyl45nkfgh'


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    name = request.form['name']
    email = request.form['email']
    response = make_response(redirect('/greet')) # Функция make_response() модуля flask используется вместо return в функции-представлении, для преобразования возвращаемого значения в объекта ответа Response.
    response.set_cookie('user_name', name)
    response.set_cookie('user_email', email)
    return response

@app.route('/greet')
def greet():
    user_name = request.cookies.get('user_name') # получаем и куки наше имя и подставляем в шаблон html для приветсвия
    if user_name:
        return render_template('greet.html')
    return redirect('/')

@app.route('/logout')
def logout():
    response = make_response(redirect('/'))
    # response.set_cookie('user_name', '', expires=0)  response - ответ. expiries время жизни куки "0" истекло
    # response.set_cookie('user_name', '', expires=0)
    response.delete_cookie('user_name')  # устанавливаем для наших значений куки
    response.delete_cookie('user_email')
    return response



"""GET — метод для чтения данных с сайта. Например, для доступа к указанной странице. Он говорит серверу, что клиент хочет прочитать указанный документ. 
На практике этот метод используется чаще всего, например, в интернет-магазинах на странице каталога. Фильтры, которые выбирает пользователь, передаются через метод GET.
POST — метод для отправки данных на сайт. Чаще всего с помощью метода POST передаются формы."""
# @app.route('/login', methods=['GET', 'POST'])
# def Login():
#     if request.method == 'POST':
#         session['username'] = request.form.get('username', 'email')
#         return redirect(url_for('main')) # redirect перенаправление на другую страницу
#     return render_template('login.html') # Функция render_template()  отображает шаблон из папки шаблонов с заданным контекстом . Переменные шаблона будут автоматически экранированы.

"""Сессии — еще один способ хранить данные конкретных пользователей между запросами. 
Они работают по похожему на куки принципу. Для использования сессии нужно сперва настроить секретный ключ. 
Объект session из пакета flask используется для настройки и получения данных сессии. 
Объект session работает как словарь, но он также может отслеживать изменения."""




if __name__ == '__main__':
    app.run(debug=True)

