from flask import Flask, render_template
from werkzeug.utils import redirect

from data import db_session
from data.jobs import Jobs
from data.user_form import RegisterForm
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()
    # user = User()
    # user.surname = 'Scott'
    # user.name = "Ridley"
    # user.age = 21
    # user.speciality = 'research engineer'
    # user.address = 'module_1'
    # user.email = "scott_chief@mars.org"
    # db_sess.add(user)
    # db_sess.commit()
    #
    # user = User()
    # user.surname = 'Scott1'
    # user.name = "Ridley1"
    # user.age = 211
    # user.speciality = 'research engineer1'
    # user.address = 'module_2'
    # user.email = "scott_chief@mars.org1"
    # db_sess.add(user)
    # db_sess.commit()
    # app.run()
    #
    # user = User()
    # user.surname = 'Scott2'
    # user.name = "Ridley2"
    # user.age = 29
    # user.speciality = 'engineer'
    # user.address = 'module_1'
    # user.email = "scott@mars.org"
    # db_sess.add(user)
    # db_sess.commit()
    #
    # user = User()
    # user.surname = 'Niggeril'
    # user.name = "Lol1"
    # user.age = 32
    # user.speciality = 'space_engineer'
    # user.address = 'module_5'
    # user.email = "scott_goooohoh@mars.org"
    # db_sess.add(user)
    # db_sess.commit()
    app.run()


@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    users = db_sess.query(User).all()
    names = {name.id: (name.surname, name.name) for name in users}
    return render_template("index.html", jobs=jobs, names=names)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            surname=form.name.data,
            age=form.name.data,
            position=form.name.data,
            Speciality=form.name.data,
            Address=form.name.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


if __name__ == '__main__':
    main()
