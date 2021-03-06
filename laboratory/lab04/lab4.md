---
# Front matter
lang: ru-RU
title: "Отчет по лабораторной работе №4"
subtitle: "Модель гармонических колебаний"
author: "Ухарова Софья"
group: "НФИбд-03-18"
ID: "1032186064"


# Formatting
toc-title: "Содержание"
toc: true # Table of contents
toc_depth: 2
lof: true # List of figures
fontsize: 12pt
linestretch: 1.5
papersize: a4paper
documentclass: scrreprt
polyglossia-lang: russian
polyglossia-otherlangs: english
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase
indent: true
pdf-engine: lualatex
header-includes:
  - \linepenalty=10 # the penalty added to the badness of each line within a paragraph (no associated penalty node) Increasing the value makes tex try to have fewer lines in the paragraph.
  - \interlinepenalty=0 # value of the penalty (node) added after each line of a paragraph.
  - \hyphenpenalty=50 # the penalty for line breaking at an automatically inserted hyphen
  - \exhyphenpenalty=50 # the penalty for line breaking at an explicit hyphen
  - \binoppenalty=700 # the penalty for breaking a line at a binary operator
  - \relpenalty=500 # the penalty for breaking a line at a relation
  - \clubpenalty=150 # extra penalty for breaking after first line of a paragraph
  - \widowpenalty=150 # extra penalty for breaking before last line of a paragraph
  - \displaywidowpenalty=50 # extra penalty for breaking before last line before a display math
  - \brokenpenalty=100 # extra penalty for page breaking after a hyphenated line
  - \predisplaypenalty=10000 # penalty for breaking before a display
  - \postdisplaypenalty=0 # penalty for breaking after a display
  - \floatingpenalty = 20000 # penalty for splitting an insertion (can only be split footnote in standard LaTeX)
  - \raggedbottom # or \flushbottom
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

 

#Цель работы: построить фазовый портрет гармонических колебаний без затухания.

##Выполнение лабораторной работы


###1. Подключаю все необходимые библиотеки 

```
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
``` 

###2. Ввожу значение w и g из своего варианта для первой задачи
```
w = 7.5  # первая задача
g = 0
```
###3. Ввожу x0 и y0.

```
x0 = 0.2
y0 = -0.2

t0 = 0.0
tmax = 55
dt = 0.05
```

###3. Зададим функцию
```
def y(v,t):
x,y = v
return [y,-1*np.power(w,2)*x - g * y]
```

###4. Запишем само уравнение 
```
ans_1 = odeint(y,v0,t)
```

###5. Выводим график 
```
fig1, ax1 = plt.subplots()

ax1.plot(ans_1[:, 0], ans_1[:, 1])  # фазовый портрет
fig4, ax4 = plt.subplots()

ax4.plot(t, ans_1[:, 0])  # решение уравнения
ax4.plot(t, ans_1[:, 1]) 

```
###6. Ввожу значение w и g из своего варианта для первой второй 
```
w = 5 # вторая
g = 7

```
###7. Запишем уравнение и выводим график 
```
ans_2 = odeint(y,v0,t);
fig2, ax2 = plt.subplots()
ax2.plot(ans_2[:,0], ans_2[:,1]) # фазовый портрет
fig5, ax5 = plt.subplots()
ax5.plot(t, ans_2[:,0]) # решение уравнения
```
###8. Ввожу значение w и g из своего варианта для первой второй 
```
w = 4 # третья
g = 2

```
###9. Зададим функцию
```
def f(t):
 return 5 * sin(t)

def y_2(v,t):
    x,y = v
    return [y,-1*np.power(w,2)*x - g * y - f(t)]
```
###10. Запишем уравнение и выводим график 
```
ans_3 = odeint(y,v0,t);
fig3, ax3 = plt.subplots()
ax3.plot(ans_3[:,0], ans_3[:,1]) # фазовый портрет
fig6, ax6 = plt.subplots()
ax6.plot(t, ans_3[:,0]) # решение уравнения
```
###11. Полученные графики
График 1:
![fig1](images/fig1.png){ #fig:001 width=70% }
График 2:
![fig2]](images/fig2.png){ #fig:002 width=70% }
График 3:
![fig3]](images/fig3.png){ #fig:003 width=70% }
График 4:
![fig4]](images/fig4.png){ #fig:004 width=70% }
График 5:
![fig5]](images/fig5.png){ #fig:005 width=70% }
График 6:
![fig6]](images/fig6.png){ #fig:006 width=70% }

**Вывод:** научилась строить фазовый портрет гармонических колебаний без затухания.
