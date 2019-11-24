import requests
import time

# Important API info Things
url = 'Webhook Link Goes Here'
headers = {
    'content-type': 'application/json',
    'cache-control': "no-cache"
}
# Files
rule_art = open('Rule_Art.json', 'rb').read()
rule_data = open('rule_data.json', 'rb').read()
mod_art = open('mod_art.json', 'rb').read()
mod_data = open('mod_data.json', 'rb').read()
chan_art = open('chan_art.json', 'rb').read()
chan_data = open('chan_data.json', 'rb').read()
perma_link = open('perma_link.json', 'rb').read()


# API Calls
rule_art_post = requests.post(url, data=rule_art, headers=headers)
rule_data_post = requests.post(url, data=rule_data, headers=headers)


mod_art_post = requests.post(url, data=mod_art, headers=headers)
mod_data_post = requests.post(url, data=mod_data, headers=headers)

time.sleep(3)
chan_art_post = requests.post(url, data=chan_art, headers=headers)
chan_data_post = requests.post(url, data=chan_data, headers=headers)

perma_link_post = requests.post(url, data=perma_link, headers=headers)
