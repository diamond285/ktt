import configparser

from telethon.sync import TelegramClient
# import pandas as pd

from datetime import datetime, timezone, timedelta

import telebot
import time
# Reading Configs
config = configparser.ConfigParser()
config.read("config.ini")

# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']

api_hash = str(api_hash)

phone = config['Telegram']['phone']
username = config['Telegram']['username']

bot = telebot.TeleBot("6534573371:AAGdzBGpB5uf3zchXcl129DBxKmKyFMfUMs")

channels = ['https://t.me/infranews', 
            'https://t.me/TransportPRO',
            'https://t.me/Coala_russia',
            'https://t.me/emphasises',
            'https://t.me/rzd_partner_news',
            'https://t.me/gruz0potok',
            'https://t.me/infranewsme',
            'https://t.me/Gudokru',
            'https://t.me/telerzd',
            'https://t.me/ElDalakz',
            'https://t.me/Vgudok',
            'https://t.me/kovshevny',
            'https://t.me/logistan',
            'https://t.me/international1520',
            'https://t.me/skladtech_expo',
            'https://t.me/today1520',
            'https://t.me/rzdlogistics',
            'https://t.me/gcnovotrans',
            'https://t.me/rzdtg',
            'https://t.me/mediastan',
            'https://t.me/CCA_Coal_Center',
            'https://t.me/ipem_research',
            'https://t.me/tzdjournal',
            'https://t.me/rzdfiles',
            'https://t.me/argus_price_agency',
            'https://t.me/trickyrails',
            'https://t.me/rollingstock']

def hasTag(tags, message):
    message = message.lower()
    for x in tags:
        if x in message:
            return True
    return False

while True:
    data = [] 
    with TelegramClient(username, api_id, api_hash) as client:
        f = open('tags.txt', 'r')
        tags = f.readlines()
        tags = [x[:-1].lower() for x in tags]
        f.close()
        for channel_link in channels:
            print(channel_link)
            for message in client.iter_messages(channel_link, offset_date=datetime.now(tz=timezone.utc) - timedelta(hours=1), reverse=True):
                data.append([channel_link, message.sender_id, message.text, message.date, message.id, message.post_author, message.views, message.peer_id.channel_id])
                if hasTag(tags, message.text):
                    bot.send_message('795918429', f'{channel_link}\n{message.date}\n\n{message.text}')
                    bot.send_message('853467565', f'{channel_link}\n{message.date}\n\n{message.text}')
                    bot.send_message('2013963466', f'{channel_link}\n{message.date}\n\n{message.text}')
    
    
    # df = pd.DataFrame(data, columns=["channel_link", "message.sender_id", "message.text"," message.date", "message.id",  "message.post_author", "message.views", "message.peer_id.channel_id" ]) # creates a new dataframe
    # df.to_csv(f'data {datetime.now()}.csv', encoding='utf-8')
    time.sleep(3600)
