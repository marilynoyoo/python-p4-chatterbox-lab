from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, Message

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>"Hello, World"</h1>'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/messages')
def messages():
    return ''

@app.route('/messages/<int:id>')
def messages_by_id(id):
    return ''

@app.route('/favicon.ico')
def favicon():
    return '', 204  # No content response


if __name__ == '__main__':
    app.run(port=5555)
