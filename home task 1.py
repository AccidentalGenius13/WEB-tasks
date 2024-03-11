from flask import Flask, url_for

app = Flask(__name__)


@app.route('/choice/<planet_name>')
def greeting(planet_name):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h2>Мое предложение: {planet_name}!</h2>
                    <h4>Эта планета близка к Земле;</h4>
                    <h4 class="mb-2 bg-success-subtle text-success-emphasis">На ней мноого необходимых ресурсов;</h4>
                    <h4 class="mb-2 bg-light text-dark">На ней есть вода и атмосфера;</h4>
                    <h4 class="mb-2 bg-warning-subtle text-warning-emphasis">На ней есть небольшое магнитное поле;</h4>
                    <h4 class="mb-2 bg-danger-subtle text-danger-emphasis">Наконец, она просто красива!</h4>
                  </body>
                </html>'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
