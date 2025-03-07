from context_search import context_search
import os
from ollama import chat
from ollama import ChatResponse

cwd = os.getcwd()
cs = context_search.ContextSearch()
prompt = "What is inteligence?"
rag_results = cs.retrive(prompt, 5)
print(rag_results)

response: ChatResponse = chat(model='deepseek-r1:1.5b', messages=[
  {
    'role': 'user',
    'content': f'''
        prompt: "What is inteligence?"
        ''',
  },
])
print(response.message.content)
