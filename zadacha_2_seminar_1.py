s = int(input("Введите чётное колличество журавликов: "))
from math import *

a = ceil(s / 3)
kat = s - a
sergey = ceil((kat / 2) / 2)
pitr = ceil((kat / 2) / 2)

print(sergey, kat, pitr)
