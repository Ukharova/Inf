---
# Front matter
lang: ru-RU
title: "Отчет по лабораторной работе №1"
subtitle: "Установка и конфигурация операционной системы на виртуальную машину"
author: "Ухарова Софья Вячеславовна"
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

# Цель работы

Приобретение практических навыков установки операционной системы на виртуальную машину, настройки минимально необходимых для дальнейшей работы сервисов

# Последовательность выполнения работы

## Создам новую виртуальную машину
![VurtualBox: создание новой виртуальной машины](/Users/sofaavdeeva/Desktop/иб/1/image/11.png){#fig:001 width=70% }

## Укажу объём оперативной памяти
![Объём оперативной памяти](/Users/sofaavdeeva/Desktop/иб/1/image/12.png){#fig:002 width=70% }

## Задам тип жёсткого диска
![Выбор типа виртуального диска](/Users/sofaavdeeva/Desktop/иб/1/image/13.png){#fig:003 width=70% }

## Укажу формат хранения
![Задание формата виртуального диска](/Users/sofaavdeeva/Desktop/иб/1/image/14.png){#fig:004 width=70% }

## Укажу имя и размер файла
![Задание размера виртуального диска](/Users/sofaavdeeva/Desktop/иб/1/image/15.png){#fig:005 width=70% }

## Выберу образ диска с дистрибутивом ОС
![Монтирование образа диска](/Users/sofaavdeeva/Desktop/иб/1/image/16.png){#fig:006 width=70% }

## Выберу язык
![Выбор региона и языка](/Users/sofaavdeeva/Desktop/иб/1/image/17.png){#fig:007 width=70%}

## Задам имя узла
![Настройка сети](/Users/sofaavdeeva/Desktop/иб/1/image/18.png){#fig:008 width=70% }

## Выберу вариант установки CentOS
![Выбор набора приложений и конфигурации установки](/Users/sofaavdeeva/Desktop/иб/1/image/19.png){#fig:009 width=70% }

## Задам пароль root
![Задание пароля root пользователю](/Users/sofaavdeeva/Desktop/иб/1/image/111.png){#fig:010 width=70% }


## Запущу терминал перейду под учетную запись root  и обновлю системные файлы
![Обновление системных файлов из под root пользователя](/Users/sofaavdeeva/Desktop/иб/1/image/112.png)
{#fig:011 width=70% }
![](/Users/sofaavdeeva/Desktop/иб/1/image/113.png){#fig:012 width=70% }

## Установлю mc
![Установка mc](/Users/sofaavdeeva/Desktop/иб/1/image/114.png){#fig:013 width=70% }



# Выводы
 Я научилась устанавливать операционные системы на виртуальную машину, настраивать минимально необходимые для дальнейшей работы сервисы


