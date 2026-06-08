import random
char="abcdefghijklmnopqrstuvwxyzACDEGHIJKLMNOPQRSTUVWXYZ"
num="1234567890"
sym="@$&#(!)"
n_char=int(input("How many character you want? "))
n_num=int(input("How many number you want? "))
n_sym=int(input("How many symbol you want? "))
length=n_char+n_num+n_sym
print(f"your password length is {length}")
password=[]
for i in range(n_char):
    p1=random.choice(char)
    password+=p1
for i in range(n_num):
    p2=random.choice(num)
    password+=p2
for i in range(n_sym):
    p3=random.choice(sym)
    password+=p3
random.shuffle(password)
final="".join(password)
print(final)
