---
## Front matter
lang: ru-RU
title: "Лабораторная работа №6"
author: "Ухарова Софья"
institute: RUDN University, Moscow, Russian Federation
date: 2021

## Formatting
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Serif
monofont: PT Serif
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

Развить навыки администрирования ОС Linux. Получить первое практическое знакомство с технологией SELinux1. Проверить работу SELinx на практике совместно с веб-сервером Apache.


## Установим httpd

![Установим httpd](/Users/sofaavdeeva/Desktop/иб/6/image/61.png){ #fig:001 width=70% }

## Вносим изменения в конфигурационный файл

![Вносим изменения в конфигурационный файл](/Users/sofaavdeeva/Desktop/иб/6/image/62.png){ #fig:002 width=70% }

## Убедимся, что SElinux работает в нужном режиме, а также найдем apache в списке процессов

![Убедимся, что SElinux работает в нужном режиме, а также найдем apache в списке процессов](/Users/sofaavdeeva/Desktop/иб/6/image/63.png){ #fig:003 width=70% }

## Просмотрим состояние переключателей

![Просмотрим состояние переключателей](/Users/sofaavdeeva/Desktop/иб/6/image/64.png){ #fig:004 width=70% }

## Просмотрим статистику по политике

![Просмотрим статистику по политике](/Users/sofaavdeeva/Desktop/иб/6/image/65.png){ #fig:005 width=70% }

## Определим тип файлов и поддиректорий

![Определим тип файлов и поддиректорий](/Users/sofaavdeeva/Desktop/иб/6/image/66.png){ #fig:006 width=70% }


## Проверим, работает ли Веб-сервер, и запустим его

![Проверим, работает ли Вэб-сервер, и запустим его](/Users/sofaavdeeva/Desktop/иб/6/image/67.png){ #fig:007 width=70% }

## Пробуем перейти по ссылке и получаем ошибку доступа

![Пробуем перейти по ссылке и получаем ошибку доступа](/Users/sofaavdeeva/Desktop/иб/6/image/68.png){ #fig:008 width=70% }

## Просмотрим права доступа и лог

![Просмотрим права доступа и лог](/Users/sofaavdeeva/Desktop/иб/6/image/69.png){ #fig:009 width=70% }

## Пробуем запустить веб-сервер на прослушивание TCP-порта 81

![Пробуем запустить веб-сервер на прослушивание TCP-порта 81](/Users/sofaavdeeva/Desktop/иб/6/image/611.png){ #fig:010 width=70% }

## И пробуем снова открыть веб-страницу

![И пробуем снова открыть веб-страницу](/Users/sofaavdeeva/Desktop/иб/6/image/612.png){ #fig:011 width=70% }

## Откроем веб-страницу через порт 81

![Откроем веб-страницу через порт 81](/Users/sofaavdeeva/Desktop/иб/6/image/613.png){ #fig:012 width=70% }

## Удалим привязку к 81 порту

![Удалим привязку к 81 порту](/Users/sofaavdeeva/Desktop/иб/6/image/614.png){ #fig:013 width=70% }

## Удалим файл test.html

![Удалим файл test.html](/Users/sofaavdeeva/Desktop/иб/6/image/615.png){ #fig:014 width=70% }

# Вывод

В результате проделанной работы мы приобрели навыки администрирования ОС Linux и проверили работу SELinx на практике совместно с веб-сервером Apache.
