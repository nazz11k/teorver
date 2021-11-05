import math
import numpy as np
import matplotlib.pyplot as plt


def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n


def A(m, n):
    return fac(n) / fac(n - m)


def C(n, m):
    return fac(n) / (fac(m) * fac(n - m))


def bern(n, m, p):
    return C(n, m) * (p ** m) * ((1 - p) ** (n - m))


def x(n, m, p):
    return (m - n * p) / math.sqrt(n * p * (1 - p))


def sum(arr):
    s = 0
    st = ""
    for i in arr:
        s += i
        st += str("%.3f" % i)
        if i != arr[-1]:
            st += " + "
    return s, st


def M(arr):
    m = 0
    for i in range(len(arr)):
        m += i * arr[i]
    return m


def M_str(arr):
    st = ""
    for i in range(len(arr)):
        st += str("%.0f" % i) + " * " + str("%.3f" % arr[i])
        if i != len(arr) - 1:
            st += " + "
    return st


def D(arr):
    d = 0
    for i in range(len(arr)):
        d += ((i - M(arr)) ** 2) * arr[i]
    return d


def D_str(arr):
    st = ""
    for i in range(len(arr)):
        st += "(" + str("%.0f" % i) + " - " + str("%.3f" % M(arr)) + ")^2 * " + str("%.3f" % arr[i])
        if i != len(arr) - 1:
            st += " + "
        return st


def ps(p, n):
    arr = []
    str1 = "   x   |"
    str2 = "   p   |"

    print("Знайдемо значення за формулою Бернуллі:")
    for i in range(n + 1):
        val = C(n, i) * (p ** i) * ((1 - p) ** (n - i))
        print("p" + str(i) + " = " + str("%.0f" % C(n, i)) + " * "
              + str("%.3f" % (p ** i)) + " * " + str("%.3f" % ((1 - p) ** (n - i)))
              + " = " + str("%.3f" % val))
        str1 += str("%7.0f" % i) + "|"
        str2 += str("%7.3f" % val) + "|"

    print()
    print("Закон розподілу величини буде такий:")

    print(str1)
    print(str2)

    print()
    print("Знайдемо функцію розподілу F(x):")
    print("F(x<0) = 0")
    for i in range(n):
        arr.append(C(n, i) * (p ** i) * ((1 - p) ** (n - i)))
        s, su = sum(arr)
        print("F(x<" + str(i+1) + ") = " + su + " = " + str("%.3f" % s))
    arr.append(C(n, n) * (p ** n) * ((1 - p) ** (n - n)))
    s, su = sum(arr)
    print("F(x>=" + str(n) + ") = " + su + " = " + str("%.3f" % s))

    d = D(arr)
    print()
    print("Знайдемо математичне сподівання, дисперсію і середнє квадратичне відхилення")
    print("M(X) = " + M_str(arr) + " = " + str("%.3f" % M(arr)))

    print()
    print("D(X) = " + D_str(arr) + " = " + str("%.3f" % D(arr)))

    print()
    print("σ(X) = √(" + str("%.3f" % d) + ") = " + str("%.3f" % math.sqrt(d)))

    plt.plot(arr)
    plt.plasma()
    plt.xlabel("x")
    plt.ylabel("p")
    plt.show()


ps(0.4, 3)
