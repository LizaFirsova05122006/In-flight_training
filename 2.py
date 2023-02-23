from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/training/<prof>')
def index(prof):
    a = ["инженер", "технолог", "конструктор", "программист", "электроник", "энергетик", "проектировщик", "механик", "эколог"]
    b = ["социолог", "спелелог", "реставратор", "генетик", "врач", "астроном", "гидролог", "океанолог", "ихтиолог", "климатолог"]
    if prof in b:
        return render_template('2.html', title=prof, pharaza="Научные симуляторы", profi=2)
    if prof in a:
        return render_template('2.html', title=prof, pharaza="Инженерные тренажеры", profi=1)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.135')