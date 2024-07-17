from flask import Flask

# создаёт экземпляр класса Flask (переменную app)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-will-never-guess'

from app import routes