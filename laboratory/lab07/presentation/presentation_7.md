---
## Front matter
lang: ru-RU
title: "Лабораторная работа №7: Эффективность рекламы"
subtitle: "*дисциплина: Математическое моделирование*"
author: "Ухарова Софья Вячеславовна"
date: 2021, 11 March

## Formatting
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
toc: false
slide_level: 2
theme: metropolis
header-includes:
 - \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
 - '\makeatletter'
 - '\beamer@ignorenonframefalse'
 - '\makeatother'
aspectratio: 43
section-titles: true

---

# Цель работы

Ознакомиться с моделью "Эффективность рекламы" и построить графики по этой модели.

# Задание

Вариант 15

Построить график распространения рекламы, математическая модель которой описывается
следующим уравнением:  
1.$$\frac{{d}n}{{d}t} = (0.89 + 0.000015 n(t))(N - n(t))$$  
2.$$\frac{{d}n}{{d}t} = (0.000015 + 0.82 n(t))(N - n(t))$$  
3.$$\frac{{d}n}{{d}t} = (1\sin(t) + 0.3\cos(t) n(t))(N - n(t))$$

При следующих начальных условиях: $N = 1500, n(t) = 15$.

# Выполнение лабораторной работы

## Библиотеки

Подключаю все необходимые библиотеки

```
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from math import sin,cos
```

# Случай №1
## Значения
Ввод значений из своего варианта для первого случая (15 вариант)
```
a1 = 0.89
a2 = 0.000015
t = np.arange(0,5,0.1)
```
# Случай №1
## Решение системы
```
def f(n,t):
    dn = (a1 + a2*n)*(N-n)
    return dn
res = odeint(f,n,t)
```
# Случай №1
## Вывод графика

Вывод графика распространения рекламы(рис. -@fig:001).

![Вывод графика №1](images/1.png){#fig:001 width=70% }

# Случай №2
## Значения
Ввод значений из своего варианта для первого случая (15 вариант)
```
a1 = 0.000015
a2 = 0.82
t = np.arange(0,0.02,0.00001)
```
# Случай №2
## Решение системы
```
dn_max = [-1,-1]

def f(n,t):
    dn = (a1 + a2*n)*(N-n)
    global dn_max
    if dn >  dn_max[0]:
         dn_max = [dn,t]
    return dn

res = odeint(f,n,t)

print(dn_max[1])
```
# Случай №2
## Вывод графика

Вывод графика распространения рекламы(рис. -@fig:002).

![Вывод графика №2](images/2.png){#fig:002 width=70% }

# Случай №2
## Вывод времени

Момент времени с максимальной скоростью распространения рекламы(рис. -@fig:003).

![Время с максимальной скоростью](images/3.png){#fig:003 width=70% }

# Случай №3
## Значения
Ввод значений из своего варианта для первого случая (15 вариант)
```
a1 = 1
2 = 0.3
t = np.arange(0,0.5,0.01)
```

# Случай №3
## Решение системы
```
def f(n,t):
    dn = (a1*sin(t)+a2*cos(t)*n)*(N-n)
    return dn

res = odeint(f,n,t)
```

# Случай №3
## Вывод графика

Вывод графика распространения рекламы(рис. -@fig:004).

![Вывод графика №3](images/4.png){#fig:004 width=70% }


# Выводы

Я ознакомиась с моделью "Эффективность рекламы" и построил графики по этой модели.
