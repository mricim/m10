import math


def uno():
    num1=int(input("Num 1: "))
    num2=int(input("Num 2: "))

    print(((num1+num2)/2))

def dos():
    peus = int(input("peus: "))
    polzadas = int(input("polzades: "))

    print(((peus*12) + polzadas) * 2.54)
def tres():
    celsius = int(input("Celsius: "))
    print((celsius* 9 / 5) + 32)
def cuatro():
    entrada = int(input("segons: "))
    minuts=(entrada//60)
    segons=entrada%60
    print("minuts:%s segons:%s"%(minuts,segons))

uno()
dos()
tres()
cuatro()