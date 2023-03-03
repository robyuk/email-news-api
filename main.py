import requests
from os import getenv
from send_email import send_email
from datetime import date

if __name__ == '__main__':
    _debug_ = False
    NL = '\n'

    topic = 'environment'
    lang = 'en'
    email_to = getenv('EMAIL2')
    today = date.today()
    yesterday = today.replace(day=today.day-1).isoformat()

    key = getenv('NEWSAPIKEY')
    url = f'https://newsapi.org/v2/everything?q={topic}&from={yesterday}&language={lang}&sortBy=relevancy&apiKey={key}'

    req = requests.get(url)
    content = req.json()
    message = f'Subject: {topic} News\n\n'

    for article in content['articles'][:20]:
        if _debug_:
            print(article['title'])
            print(article['url'])

        message = message + article['title'] + NL + article['url'] + 2*NL

    print(type(message), message)
    send_email(msg=message.encode('utf-8'), to=email_to)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
