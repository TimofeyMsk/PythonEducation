"""
Расширение стандартного filter. Можно применять несколько функций
и ограниченно управлять логикой фильтрации.
"""
class multifilter:
    def judge_half( pos: int, neg: int):
        """
        Допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        pos: сколько функций допускают этот элемент
        neg: сколько функций НЕ допускают этот элемент
        """
        return pos >= neg

    def judge_any(pos, neg):
        """
        допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        """
        return pos >= 1

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        return pos >= 1 and neg == 0

    def __init__(self, iterable, *funcs, judge = judge_any):
        """
        iterable - исходная последовательность.
        funcs - допускающие функции.
        judge - решающая функция.
        """
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

        self.iter_forIterable = iter(iterable)

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        return self

    def __next__(self):
        while True:
            e = next(self.iter_forIterable)
            pos, neg = 0, 0
            for f in self.funcs:
                if f(e):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos,neg):
                return e
            else:
                continue


def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0


a = [i for i in range(61)] # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# [0, 30]

print(list(multifilter(a,mul2,mul3, mul5, judge= (lambda x,y:
                                            multifilter.judge_half(x,y) and not multifilter.judge_all(x,y))
                       )))