---
## Front matter
lang: ru-RU
title: "Л.5. Дискреционное разграничение прав в Linux. Исследование влияния дополнительных атрибутов"
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

Изучение механизмов изменения идентификаторов, применения SetUID- и Sticky-битов. Получение практических навыков работы в консоли дополнительными атрибутами. Рассмотрение работы механизма смены идентификатора процессов пользователей, а также влияние бита Sticky на запись и удаление файлов.

# Ход работы 

## От имени пользователя guest создам файл simpleid.c и создадим программу

![Программа simpleid.c](/Users/sofaavdeeva/Desktop/иб/5/image/51.png){ #fig:001 width=70% }

## Скомпилируем программу:

![Компиляция simpleid.c](/Users/sofaavdeeva/Desktop/иб/5/image/52.png){ #fig:002 width=70% }

## Запускаем simpleid.c и сверяем с результатом команды id

![Запуск simpleid.c и id](/Users/sofaavdeeva/Desktop/иб/5/image/53.png){ #fig:003 width=70% }

Получили одинаковые результаты параметров.

## Усложним программу "simpleid.c", добавив вывод действительных идентификаторов

![Программа simpleid2.c](/Users/sofaavdeeva/Desktop/иб/5/image/54.png){ #fig:004 width=70% }

## Скомпилируем запустим simpleid2.c

![Компиляция и выполнение simpleid2.c](/Users/sofaavdeeva/Desktop/иб/5/image/55.png){ #fig:005 width=70% }

Теперь стало видно не только текущих группу и пользователя, но и владельца файла.

## Сменим владельца файла "simpleid2" и добавим ему атрибут SetUID

Запустим simpleid2 и id. Получаем идентичные параметры:

![Смена владельца и добавление атрибута s](/Users/sofaavdeeva/Desktop/иб/5/image/56.png){ #fig:006 width=70% }

## Создадим файл readfile.c

![Программа readfile.c](/Users/sofaavdeeva/Desktop/иб/5/image/57.png){ #fig:007 width=70% }

## Скомпилируем и изменим права, чтобы только root мог прочитать его, а guet -- нет


![Компиляция и изменение readfile.c](/Users/sofaavdeeva/Desktop/иб/5/image/58.png){ #fig:008 width=70% }

## Проверим, что gust не может прочесть readfile.c

![Изменение владельца readfile с SetUID](/Users/sofaavdeeva/Desktop/иб/5/image/59.png){ #fig:009 width=70% }


## Выясним, что на директории /tmp установлен атрибут Sticky:


![Атрибут Sticky на /tmp](/Users/sofaavdeeva/Desktop/иб/5/image/511.png){ #fig:010 width=70% }

## Создадим файл file1 и и разрешим чтение и запись для категории пользователей "все остальные"

![изменение атрибутов file1](/Users/sofaavdeeva/Desktop/иб/5/image/512.png){ #fig:011 width=70% }

## Пробуем записать информацию в file1

Удалить файл не получилось.

![Работа с file01.txt](/Users/sofaavdeeva/Desktop/иб/5/image/513.png){ #fig:012 width=70% }

## Снимим атрибут -t

![Снятие атрибута t](/Users/sofaavdeeva/Desktop/иб/5/image/514.png){ #fig:013 width=70% }

## Повторим наши действия с file1

Повторили все действия и, в отличие от предыдущего раза, теперь уже нам удалось удалить файл:

![Работа с file01](/Users/sofaavdeeva/Desktop/иб/5/image/515.png){ #fig:014 width=70% }

## Обратно вернем атрибут -t

![Возврат атрибута t](/Users/sofaavdeeva/Desktop/иб/5/image/516.png){ #fig:015 width=70% }

# Вывод

В результате проделаной работы мы изучили механизмы изменения идентификаторов, применения SetUID- Sticky-битов, а так же получили практические навыки работы в консоли с дополнительными атрибутами.


