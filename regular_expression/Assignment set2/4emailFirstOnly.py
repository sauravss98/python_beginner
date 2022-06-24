import re


def email(text):
    x=re.findall("(\S+)@",text)
    print(x)
email("fjanj n   saur@gmail.com ad adasd as sand@yagoo.com  as ad ")