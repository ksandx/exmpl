#!/usr/bin/env python
# coding=utf-8
from urllib.request import Request, urlopen
from time import sleep
import sender

url = 'https://api.nanopool.org/v1/eth/reportedhashrate/0x0'

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
res = webpage.decode()
print(res.split(':')[2][:-2])
while True:

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    res = webpage.decode()
    hash_r = res.split(':')[2][:-2]
    if float(hash_r) < 430:
        print('Hash rate < 430 : ', hash_r)
        message = 'Reported hash rate: ' + str(hash_r)
        sender.send_mail(text=message)

    sleep(300)
