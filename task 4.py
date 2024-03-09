from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def mission():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвест"


@app.route('/promotion_image')
def promotion():
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <title>Привет, Марс!</title>
                            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>                        
                          </head>
                          <body>
                            <h1 class="h_1">Жди нас, Марс!</h1>
                            <img src="{url_for('static', filename='img/mars.png')}" 
                            alt="здесь должна была быть картинка, но не нашлась">
                            <div class="p-3 mb-2 bg-light text-dark">Человечество вырастает из детства.</div>
                            <div class="p-3 mb-2 bg-success-subtle text-success-emphasis">Человечеству мала одна планета.</div>
                            <div class="p-3 mb-2 bg-body-secondary">Мы сделаем обитаемыми безжизненные пока планеты.</div>
                            <div class="p-3 mb-2 bg-warning-subtle text-warning-emphasis">И начнем с Марса!</div>
                            <div class="p-3 mb-2 bg-danger-subtle text-danger-emphasis">Присоединяйся!</div>
                          </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
