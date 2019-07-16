import string

postgres_config = {
    'username': 'dawidbodych',
    'password': 'test123',
    'host': '0.0.0.0',
    'database': 'websearch_app'
}

google_config = {
    'api_key': 'AIzaSyAEpTmyAZPDK__CfUma0H33mMzBfTMdYtQ',
    'cse_id': '012435862673425950212:sy5dawx25b8'
}

general_config = {
    'result_fields': ['links_and_positions', 'total_results', 'top_10_words'],
    'translator': str.maketrans('', '', string.punctuation)
}
