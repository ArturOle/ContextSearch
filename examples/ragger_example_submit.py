# Only for testing purposes

# if you want to test the functionalities, correct the neo4j uri in the config file

import os

from context_search.context_search import ContextSearch


cwd = os.getcwd()

cs = ContextSearch()
cs.submit(path=[
    cwd + r"/data/pdf-ai-generated/ES_article.pdf",
    cwd + r"/data/pdf-ai-generated/ML_article.pdf",
    cwd + r"/data/pdf-ai-generated/HumanInteligence_article.pdf"
])
