
def diff(x):
    flag = set([])
    strx = str(x)
    lens = len(strx)
    for i in range(lens):
        flag.add(strx[i])
    return lens == len(flag)


#print("##################")
#print(list(filter(diff, list(sum))))




#######################################################################################

# 多级比率计算
def li():
    l = float(input("请输入净利润:"))
    r = 0
    level = [100, 60, 40, 20, 10, 0]
    v = [0.01, 0.015, 0.03, 0.05, 0.075, 0.10]
    for i in range(6):
        if l > level[i]:
            r += (l - level[i])*v[i]
            l = level[i]
    print(r)


#li()



#######################################################################################

def test():
    n = 1
    while True:
        a = pow(n + 100, 0.5)
        b = pow(n + 100 + 168, 0.5)
        if int(a) == a and int(b) == b:
            print(n)
        n += 1


test()



#######################################################################################



def sor(*arg):
    so = []
    imax = arg[0]
    for i in arg:
        pass



#######################################################################################



def yang():
    L = [1]
    while True:
        yield L
        # 方式1
        #P = L + [0]
        #L = [P[i - 1] + P[i] for i in range(len(P))]
        # 方式2
        L = [1] + [L[i]+L[i+1] for i in range(len(L)-1)] + [1]



def yang():
    n = 1
    a = [1]
    while True:
        i = 0
        b = []
        while i < n:
            if i == 0 or i == n-1:
                b.append(1)
                i = i+1
                continue
            b.append(a[i-1]+a[i])
            i = i+1
        a = b
        yield(b)
        n = n+1


for i in yang():
    print(i)

#########################################

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a


def fib2(n):
    if n == 1 or n == 2:
        return 1
    return fib2(n-1)+fib2(n-2)



print(fib2(12))





#############################




def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列


a = primes()
print(next(a))
print(next(a))
print(next(a))
print(next(a))








#############################




from datetime import datetime
dt = datetime(2015, 4, 19, 12, 20)  # 用指定日期时间创建datetime
aa = dt.timestamp()  # 把datetime转换为timestamp
print(aa)

print(datetime.fromtimestamp(111.0))
print()





#############################


def nature():
    n = 1
    while True:
        n = n + 1
        yield n


def f(c):
    return lambda x: x % c > 0


def su():
    na = nature()
    while True:
        flag1 = next(na)
        na = filter(f(flag1), na)
        yield flag1


#   s = su()
#   for i in s:
#       if i < 1000:
#           print(i)


def naturn1():
    n = 1
    while True:
        yield n
        n = n + 1


def hui(x):
    x = str(x)
    lens = len(x)
    for i in range(lens):
        if x[i] != x[lens-1-i]:
            return False
    return True


def hui(n):
    N = str(n)
    return N == N[::-1]


print(list(filter(hui, list(range(1000)))))





#############################



def createCounter():
    X = []
    def counter():
        X.append(1)
        return sum(X)
    return counter



def createCounter1():
    n = 0
    def counter():
        nonlocal n
        n += 1
        return n
    return counter

def createCounter2():
    f = [0]
    def counter():
        f[0]+=1
        return f[0]
    return counter

a = createCounter()

print(a())
print(a())
print(a())
print(a())
print(a())
print(a())







#############################


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.user.timeline.list)




#############################




a = [1, 3, 5, 2, 4, 5, 7]
n = len(a)
for i in range(n):
    for j in range(i, n):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]
print(a)



#[int(input("enter a integer: ")) for x in range(3)]






#############################





from functools import reduce

l=[0,1]
for i in range(10):
    print(l[-1:-3:-1])
    l.append(reduce(lambda x,y:x+y,l[-1:-3:-1]))
print(l)






#############################




#for i in range(1, 10):
#    for j in range(10):
#        for k in range(10):
#            if i ** 3 + j ** 3 + k ** 3 == i * 100 + j * 10 + k:
#                print(i * 100 + j * 10 + k)


for i in range(100, 1000):
    g = i % 10
    s = i % 100 // 10
    b = i // 100
    if i == g ** 3 + s ** 3 + b ** 3:
        print(i)



for i in range(1000, 10000):
    g = i % 10
    s = i % 100 // 10
    b = i % 1000 // 100
    q = i % 10000 // 1000
    w = i % 100000 // 10000
    if g != s and g != b and s != b:
        print(i, ':', w, q, b, s, g)

"""
去除字符串首尾的空格
"""


def trim(s):
    if s[0] == ' ':
        return trim(s[1:])
    if s[-1] == ' ':
        return trim(s[:-1])
    return s






