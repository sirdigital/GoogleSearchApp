from config import general_config, postgres_config

from collections import Counter
import re
import uuid


def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


def get_just_text(raw_text):
    return clean_html(raw_text).translate(general_config['translator'])


def get_n_most_words(text, n):
    WordCounter = Counter(get_just_text(text).split())
    return WordCounter.most_common(n)


def generate_uuid():
    return str(uuid.uuid4())


def get_db_connection_uri():
    return "postgresql://{username}:{password}@{host}/{database}".format(**postgres_config)
