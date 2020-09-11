import re
import sys

"""
Фильтрует числа в двоичном виде.
Выдает только числа делящиеся на три.
Регулярка построена по конечному автомату - генератору двоичных чисел.
"""

for line in sys.stdin:
    line = line.strip()
    if re.search(r"\A[01]+\Z",line):
         if re.fullmatch(r"0*(1(0(1*)0)*10*)*",line[::-1]):
             print(line)



