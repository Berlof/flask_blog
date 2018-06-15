"""
Простой веб-сервер, который отдает простую html страницу, основанную на шаблонизаторе
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello():
    """
    Функция возвращает html страницу.
    Html страница создается из шаблона hello.html с помощью функции render_template
    Т.к в шаблоне указана переменная, необходимо ее передать при рендере 
    """
    return render_template('hello.html', hello_text='Hello')


if __name__=='main':
    app.run()