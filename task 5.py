from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <title>Привет, Марс!</title>
                            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>                        
                          </head>
                          <body>
                            <h2 class="anketa_header_1">Анкета претендента</h2>
                            <h4 class="anketa_header_2">на участие в миссии</h4>
                            <div>
                                <form class="login_form" method="post">
                                    <div class="form-group mb-3">
                                        <input class="form-control" type="text" id="surname" placeholder="Введите фамилию" name="surname">
                                        <input class="form-control" type="text" id="name" placeholder="Введите имя" name="name">
                                    </div>
                                    <div class="form-group mb-3">
                                      <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    </div>
                                    <div class="form-group mb-3">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-select" id="educationSelect" name="education">
                                          <option value="1">Начальное</option>
                                          <option value="2">Основное общее</option>
                                          <option value="3">Среднее общее</option>
                                          <option value="4">Среднее профессиональное</option>
                                          <option value="4">Высшее</option>
                                        </select>
                                    </div>
                                    <div class="form-group mb-3">
                                        <label for="professionSelect">Какие у Вас есть профессии?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                          <label class="form-check-label" for="flexCheckDefault">
                                            инженер-исследователь
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked">
                                          <label class="form-check-label" for="flexCheckChecked">
                                            пилот
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                          <label class="form-check-label" for="flexCheckDefault">
                                            строитель
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked">
                                          <label class="form-check-label" for="flexCheckChecked">
                                            экзобиолог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                          <label class="form-check-label" for="flexCheckDefault">
                                            врач
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked">
                                          <label class="form-check-label" for="flexCheckChecked">
                                            специалист по радиационной защите
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked">
                                          <label class="form-check-label" for="flexCheckChecked">
                                            инженер жизнеобеспечения
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked">
                                          <label class="form-check-label" for="flexCheckChecked">
                                            оператор марсохода
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked">
                                          <label class="form-check-label" for="flexCheckChecked">
                                            киберинженер
                                          </label>
                                        </div>
                                    </div>
                                    
                                    <div class="form-group mb-3">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
        
                                    <div class="form-group mb-3">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    
                                    <div class="form-group mb-3">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    
                                    <div class="form-group form-check mb-3">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['education'])
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['file'])
        print(request.form['accept'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')