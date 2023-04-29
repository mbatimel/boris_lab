from scipy import optimize
import numpy as np
import math
import warnings

# убираю предупреждение но возможно оно может влиять на значения поэтому лучше разобраться
warnings.filterwarnings('ignore')



def sumfun(Yt, Kt, Lt, list_obj):
    f = 0
    for i in range(len(Yt)):
        f += (Yt[i] - list_obj[i][0] * (Kt[i] ** list_obj[i][1]) * (Lt[i] ** (list_obj[i][1] - 1))) ** 2
    print(f)


# 3.2.1________________________________________

def funmin(Yt, Kt, Lt):
    list_obj = []
    for i in range(12):
        f = lambda x: (Yt[i]) - x[0] * ((Kt[i] ** x[1]) * (Lt[i] ** (x[1] - 1))) ** 2
        solution = optimize.minimize(f, x0=(0.1, 0.5))
        list_obj.append(solution.x)
    sumfun(Yt, Kt, Lt, list_obj)
    list_obj.clear()


# _____________________________________________
# 3.2.2________________________________________

def fminsearch(Yt, Kt, Lt):
    list_obj = []
    for i in range(len(Yt)):
        f = lambda x: (Yt[i] - x[0] * (Kt[i] ** x[1]) * (Lt[i] ** (x[1] - 1))) ** 2
        solution = optimize.minimize(f, x0=[0.1, 0.5], method='Nelder-Mead')
        list_obj.append(solution.x)
    sumfun(Yt, Kt, Lt, list_obj)
    list_obj.clear()


# _____________________________________________
# 3.2.3________________________________________

def BFGS(Yt, Kt, Lt):
    list_obj = []
    for i in range(len(Yt)):
        f = lambda x: (Yt[i] - x[0] * (Kt[i] ** x[1]) * (Lt[i] ** (x[1] - 1))) ** 2
        solution = optimize.minimize(f, x0=[0.1, 0.5], method='BFGS')
        list_obj.append(solution.x)
    sumfun(Yt, Kt, Lt, list_obj)
    list_obj.clear()


# _____________________________________________
# 3.2.4________________________________________

def Isqnonneg(Yt, Kt, Lt):
    list_obj = []
    for i in range(len(Yt)):
        f = lambda x: (Yt[i] - x[0] * (Kt[i] ** x[1]) * (Lt[i] ** (x[1] - 1))) ** 2
        solution = optimize.least_squares(f, x0=[0.1, 0.5])
        list_obj.append(solution.x)
    sumfun(Yt, Kt, Lt, list_obj)
    list_obj.clear()


# _____________________________________________


matrix = [[1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976],
          [180, 197, 215.5, 230.7, 245, 251.5, 284, 304.4, 336, 368.7, 393, 426],
          [151.7, 166.7, 189, 212.5, 237.6, 265, 283, 316, 353, 398.4, 455.7, 520],
          [1863, 1931, 1971, 2031, 2162, 2277, 2457, 2601, 2798, 2983, 3110, 3268]]
Yt = matrix[1]
Kt = matrix[2]
Lt = matrix[3]
funmin(Yt, Kt, Lt)
fminsearch(Yt, Kt, Lt)
BFGS(Yt, Kt, Lt)
Isqnonneg(Yt, Kt, Lt)
#    Наша функция Y=A*K^a*L^(1-a)
#   приводим к логарифмичискому виду ln(Y)=ln(A)+a*ln(K)+(a-1)*ln(L)
# начальное приближение х0 = [0.1 0.5]; 
# квадратичная функция sum(Yt-A*Kt^a*L^(a-1))
#   приводим к логарифмичискому виду ln(Y)=ln(A)+a*ln(K)+(a-1)*ln(L)
# options={'gtol': 1e-10, 'disp': True}
