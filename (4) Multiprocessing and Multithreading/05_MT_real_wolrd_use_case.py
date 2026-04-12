'''
Real-World Example: Multi Threading for I/O bound tasks
Scenario : Web Scraping
Web Scraping often involves making numerous network requests to fetch web pages.
These tasks are I/O bound because they spend a lot of time wating for the responses from servers. 
Multithreading can significantly improve the performance by allowing multiple web pages to be fetched
'''

'''https://python.langchain.com/docs/introduction/
https://python.langchain.com/docs/concepts/
https://python.langchain.com/docs/tutorials/'''


import threading
import requests
from bs4 import BeautifulSoup

urls=[
'https://python.langchain.com/docs/introduction/',
      
'https://python.langchain.com/docs/concepts/',

'https://python.langchain.com/docs/tutorials/'

]

def fetch_content(url):
    response=requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')

threads = []

for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All Web Pages Fetched")