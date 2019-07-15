from modules.google_api_search import get_results
from modules.helpers import get_db_connection_uri

from flask import Flask, request, render_template, render_template_string
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import TimeoutError, SQLAlchemyError
from flask import request
import datetime

app = Flask(__name__)
app.config['TIME_LIMIT'] = 5
app.config["SQLALCHEMY_DATABASE_URI"] = get_db_connection_uri()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

from models import *


def save_result_to_db(user_ip, phrase, results):
    new_record = Result(user_ip=user_ip,
                        phrase=phrase,
                        links_and_positions=results['links_and_positions'],
                        total_results=results['total_results'],
                        top_10_words=results['top_10_words'])

    try:
        db.session.add(new_record)
        db.session.commit()
    except (SQLAlchemyError, TimeoutError):
        pass


def check_if_result_in_db(user_ip, phrase):
    current_time = datetime.datetime.now()
    time_limit = current_time - datetime.timedelta(minutes=app.config['TIME_LIMIT'])

    try:
        record = Result.query.filter(Result.user_ip == user_ip,
                                     Result.phrase == phrase,
                                     Result.created_at > time_limit).first()
    except (SQLAlchemyError, TimeoutError):
        return None

    if record:
        return record.__dict__
    else:
        return None


@app.route('/search', methods=['GET', 'POST'])
def search():
    user_ip = request.remote_addr
    phrase = request.form.get('phrase')

    if not phrase:
        return render_template_string('Field Phrase cannot be left blank.')

    results = check_if_result_in_db(user_ip, phrase)
    if not results:
        results = get_results(phrase)
        if not results:
            return render_template_string('An error occurred. Try again.')
        save_result_to_db(user_ip, phrase, results)

    return render_template("search_results.html", results=results)


@app.route('/search_form')
def search_form():
    return render_template('search_form.html')


if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    app.run(debug=True)
