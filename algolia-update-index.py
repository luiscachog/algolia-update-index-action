import json
from algoliasearch.search_client import SearchClient
from os import getenv

ALGOLIA_APIKEY = getenv('INPUT_ALGOLIA_APIKEY', 'none')
ALGOLIA_APP_ID = getenv('INPUT_ALGOLIA_APP_ID', 'none')
ALGOLIA_INDEX_NAME = getenv('INPUT_ALGOLIA_INDEX_NAME', 'none')
FILE = getenv('INPUT_FILE', 'none')
EXCEPTIONS = getenv('INPUT_EXCEPTIONS', 'none')

client = SearchClient.create(ALGOLIA_APP_ID, ALGOLIA_APIKEY)
index = client.init_index(ALGOLIA_INDEX_NAME)

with open(FILE, 'r') as file:
    data = json.load(file)

# Looking for the 'objectID' that is larger than 10k for Legacy plans
# and pop it from the data to NOT send the 'content' field related to the
# 'objectID'
# https://www.algolia.com/doc/faq/basics/is-there-a-size-limit-for-my-index-records/
for element in data:
    if element["objectID"] in EXCEPTIONS:
        element.pop('content', None)

index.replace_all_objects(data, {'safe': True})
