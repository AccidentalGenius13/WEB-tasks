from flask import Flask, url_for

app = Flask(__name__)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def greeting(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                    <title>Результаты</title>
                  </head>
                  <body>
                    <h2>Результаты отбора</h2>
                    <h4>Претендента на участие в миссии {nickname}:</h4>
                    <h4 class="mb-2 bg-success-subtle text-success-emphasis">Поздравляем! Ваш рейтинг после {level} этапа отбора</h4>
                    <h4 class="mb-2 bg-light text-dark">составляет {rating}!</h4>
                    <h4 class="mb-2 bg-warning-subtle text-warning-emphasis">Желаем удачи!</h4>
                  </body>
                </html>'''



if __name__ == '__main__':
    app.run()
