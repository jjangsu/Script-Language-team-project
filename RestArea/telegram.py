#!/usr/bin/python
# coding=utf-8

import sys
import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from datetime import date, datetime, timedelta
import traceback

import noti


routeNoToName = {'경부선':'0010', '남해선':'0100', '광주대구선':'0120', '무안광주선':'0121',
                 '서해안선': '0150',  '대구포항선':'0200',
                 '익산장수선': '0201', '호남선':'0251', '천안논산선':'0252', '논산천안선':'0252', '순천완주선':'0270', '청주영덕선':'0300',
                 '당진대전선': '0301', '중부선':'0352', '평택제천선':'0400', '중부내륙선':'0450',
                 '영동선':'0500', '중앙선' : '0550', '대구부산선':'0552', '서울양양선' : '0600', '동해선':'0650',
                 '서울외곽순환선': '1000', '남해2지선':'1040', '서천공주선':'1510', '호남지선':'2510', '중부내륙지선':'4510'
                 }


def replyAptData(date_param, user, loc_param='11710'):
    print(user, date_param, loc_param)
    res_list = noti.getData( date_param )
    print(res_list)
    msg = ''
    for r in res_list:
        print( str(datetime.now()).split('.')[0], r )
        if len(r+msg)+1>noti.MAX_MSG_LENGTH:
            noti.sendMessage( user, msg )
            msg = r+'\n'
        else:
            msg += r+'\n'
    if msg:
        noti.sendMessage( user, msg )
    else:
        noti.sendMessage( user, '그런 노선이 없슴다'%date_param )

def save( user, loc_param ):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    try:
        cursor.execute('INSERT INTO users(user, location) VALUES ("%s", "%s")' % (user, loc_param))
    except sqlite3.IntegrityError:
        noti.sendMessage( user, '이미 해당 정보가 저장되어 있습니다.' )
        return
    else:
        noti.sendMessage( user, '저장되었습니다.' )
        conn.commit()

def check( user ):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    cursor.execute('SELECT * from users WHERE user="%s"' % user)
    for data in cursor.fetchall():
        row = 'id:' + str(data[0]) + ', location:' + data[1]
        noti.sendMessage( user, row )


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        noti.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return

    text = msg['text']
    args = text.split(' ')
    if text.startswith('노선명') and len(args) > 1:
        print('try to 노선명', args[1])
        replyAptData(args[1], chat_id)
    elif text.startswith('저장')  and len(args)>1:
        print('try to 저장', args[1])
        save( chat_id, args[1] )
    elif text.startswith('확인'):
        print('try to 확인')
        check( chat_id )
    else:
        noti.sendMessage(chat_id, '노선명 [ex)경부선] 등의 명령을 입력하세요.')


today = date.today()
current_month = today.strftime('%Y%m')

print( '[',today,']received token :', noti.TOKEN )

bot = telepot.Bot(noti.TOKEN)
pprint( bot.getMe() )

bot.message_loop(handle)

print('Listening...')

while 1:
  time.sleep(10)