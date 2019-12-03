#!/usr/bin/env python

import yagmail
import requests
from bs4 import BeautifulSoup

url = 'https://www.merriam-webster.com/word-of-the-day'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

subject = soup.find('span', attrs = {'class' : 'w-a-title margin-lr-0 margin-tb-1875em'})

mail_subj = (subject.text.strip())

word = soup.find('div', attrs = {'class' : 'word-and-pronunciation'})

cleaned_word = word.text.strip().split()[0]

mail_word = cleaned_word


definition = soup.find('div', attrs = {'class' : 'wod-definition-container'})
mail_definition = (definition.find('p'))


fact = soup.find('div', attrs = {'class' : 'left-content-box'})
mail_fact = (fact.find('p'))


examples = soup.find('div', attrs = {'class' : 'wotd-examples'})
mail_examples = examples.find_all('p')

sender = 'sendersemail@gmail.com'
pswd = 'senders password'

yag  = yagmail.SMTP(sender, pswd)

contents = f'''<html><body><h1><b>{mail_word}</b></h1><br><h2>Definition<br>{mail_definition}</h2><br><h3>{mail_fact}</h3><br><h4><u><i>Examples:</i></u><br>{mail_examples}</h4></body></html>'''



yag.send(['receiver1@gmail.com', 'receiver2@gmail.com'], mail_subj, contents)
