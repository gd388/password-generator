import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ACDEFGHIJKLMNOPQRSTUVWXYZ"
num="0123456789"
symbols="=-*/@#$%"
all=lower+upper+num+symbols
length=8
password="".join(random.sample(all,length))
print(password)