from .helpers import get_n_most_words
from config import google_config

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError as GoogleHttpError

my_api_key = "AIzaSyAEpTmyAZPDK__CfUma0H33mMzBfTMdYtQ"
my_cse_id = "012435862673425950212:sy5dawx25b8"


def google_search(search_term, **kwargs):
    service = build("customsearch", "v1", developerKey=google_config['api_key'])
    try:
        res = service.cse().list(q=search_term, cx=google_config['cse_id'], **kwargs).execute()
        return res
    except GoogleHttpError:
        return None


def get_results(phrase):
    results = google_search(phrase)
    if results:
        return transform_results(results)
    else:
        return None


def transform_results(results):
    links_and_positions = [(results['items'].index(r)+1, r['link']) for r in results['items']]
    total_results = results['searchInformation']['totalResults']
    all_words = ' '.join('{} {}'.format(r['htmlSnippet'], r['htmlTitle']) for r in results['items'])

    ten_most_words = get_n_most_words(all_words, 10)

    return {'links_and_positions': links_and_positions,
            'total_results': total_results,
            'top_10_words': ten_most_words}
