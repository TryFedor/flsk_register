from flask import Flask
from data.db_session import global_init, create_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    global_init(input())
    db_sess = create_session()
    for user in db_sess.query(User).filter(User.address == 'module_1',
                                           User.speciality.not_like('%engineer%'),
                                           User.position.not_like('%engineer%')):
        print(user.id)


if __name__ == '__main__':
    main()
