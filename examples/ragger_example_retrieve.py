# Only for testing purposes

# if you want to test retriving data, first use ragger_example_submit.py to insert data

import os

from context_search.context_search import ContextSearch


cwd = os.getcwd()

cs = ContextSearch()
for record in cs.retrieve("machine Inteligence", 5):
    print(record)
