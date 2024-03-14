from flask import Flask, render_template, url_for, redirect

from json import load
import os
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/member')
def member():
    path = os.path.abspath("templates")
    with open(f"{path}/members.json", encoding="utf-8") as file:
        rand = random.randint(1, 3)
        data = load(file)
        data = data["members"][f"member_{rand}"]
        members = dict(name_surname=data["name_surname"], path=url_for("static", filename=data["path"]),
                       list_prof=", ".join(data["list_prof"]))
        print(members["path"])
        return render_template('members.html', member=members)



@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    param = {}
    professinos = ["инженер", "строитель"]
    param["string"] = "e" if len([True for i in professinos if i in prof]) > 0 else "s"
    param["image"] = url_for('static', filename='img/IS.jpg') if param["string"] == "e" else url_for('static', filename='img/NS.jpg')
    return render_template('training.html', **param)


@app.route('/distribution')
def distribution():
    param = {}
    names = """Ридли Скотт
        Энди Уир
        Марк Уотни
        Венката Капур
        Тедди Сандерс
        Шон Бин""".split("\n")
    param["names"] = names
    return render_template('distribution.html', **param)


@app.route('/list_prof/<list>')
def professions(list):
    param = {}
    professions = ["Инженер-исследователь", "пилот", "строитель", "экзобиолог", "врач", "Инженер по терраформированию",
                   "климатолог" "специалист по радиационной защите", "астрогеолог", "гляциолог",
                   "инженер жинеобеспечения", "метеоролог", "оператор марсохода", "киберинженер", "штурман",
                   "пилот дронов"]
    param["list"] = list
    param["profs"] = professions
    return render_template('professions.html', **param)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    param = {
        "title": "Анкета",
        "surname": "Бикоушавелов",
        "name": "Изготин",
        "education": "среднее",
        "profession": "пилот",
        "sex": "male",
        "motivation": "Поспать",
        "ready": True,
        "css": url_for('static', filename='css/answer.css')
    }
    return render_template('answer.html', **param)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
