#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import requests,re,datetime

################################


# loginId: hfeng@139.com
# password: sal9a35f6735299c072b331f5d005856bee
#cookie = {'acw_tc':'2f624a5b15963238072607406e6a5d77bdb49b7863620e70a8f6047c366aaf','listen_repeat_number':'2', 'listen_repeat_interval':'2000','listen_word_interval':'10000','token':'QngsrHlqE8Se80hmQs2TXm5lC5YQX2721V992C41cOF21ndMtr','id':'4557084'}


################################

pages = 500
url = "http://www.iwordnet.com/quiz/getWordPageList.htm"
cookstr = 'last_vocal_listen_id=; listen_repeat_number=2; listen_repeat_interval=2000; listen_word_interval=10000; acw_tc=2f624a2615998131604444368e13c336567501b795d87e2e07c154c8ce4978; token=j9fuWlj6cXb6eo60PBGnV7dgtg878Hu0a7wV6gIpdIcT3xlCSr; id=7901305;'

data = {
    'p': 1,
    'type': '2',
    'from': '2020-08-01 00:00:00',
    'to': '2020-08-09 23:59:59',
    'pattern': '1,2,3'
}

data = {
    'p': 1,
    'type': '1',
    'from': 'A',
    'to': 'Z',
    'pattern': '1,2,3'
}
#################################

cookie = dict()
cookArray = re.split('=|; ', cookstr)
cookArray2 = [cookArray[i:i+2] for i in range(0, len(cookArray), 2)]
# print(cookArray2)
for i in cookArray2:
    cookie[i[0]] = i[1]

# print(cookie)
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}

today = str(datetime.date.today())
f = open(r'c:\Users\FENG\Desktop\zhimiword-'+today+'.word', 'w', encoding='utf-8')
df = open(r'c:\Users\FENG\Desktop\zhimidata-'+today+'.txt', 'w', encoding='utf-8')
while data['p'] <= pages:
    response = requests.post(url, data=data, headers=header, cookies=cookie)
    data['p'] += 1
    tdata = response.text
    jdata = response.json()
    # print(jdata)
    df.writelines(tdata)
    df.writelines('\n')
    df.flush()
    for word in jdata["words"]:
        word_tran = word['lemma']+"\t"+word['senior']
        print(word_tran)
        f.writelines(word_tran)
        f.writelines('\n')
        f.flush()
f.close()
df.close()




