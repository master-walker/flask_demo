#!/usr/bin/env python
#coding=utf-8

# from flask_mail import Message
# from app import mail
# from app import app
import os
print os.environ.get("MAIL_USERNAME")
print os.environ.keys()
# os.environ.setdefault("db_name",failobj="123")
# print os.environ.get("TEST")

msg = Message("test subject",sender="1158620887@qq.com",recipients=["807924140@qq.com"])
msg.body = "test body"
with app.app_context():
    mail.send(msg)


def binary_search(arr,ele):
    arr.sort()
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high)/2
        if arr[mid] < ele:
            low = mid + 1
        elif arr[mid] > ele:
            high = mid - 1
        else:
            print 'find ele {0}'.format(arr[mid])
            return arr[mid]
    return -1

arr = [1,3,5,9,7,5,4,6,0]
binary_search(arr,6)

