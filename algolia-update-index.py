import json
from algoliasearch.search_client import SearchClient
from os import getenv

ALGOLIA_APIKEY = getenv('INPUT_ALGOLIA_APIKEY', 'none')
ALGOLIA_APP_ID = getenv('INPUT_ALGOLIA_APP_ID', 'none')
ALGOLIA_INDEX_NAME = getenv('INPUT_ALGOLIA_INDEX_NAME', 'none')
FILE = getenv('INPUT_FILE', 'none')

client = SearchClient.create(ALGOLIA_APP_ID, ALGOLIA_APIKEY)
index = client.init_index(ALGOLIA_INDEX_NAME)

with open(FILE, 'r') as file:
    data = json.load(file)
    index.replace_all_objects(data, {'safe': True})
