# Задача 2: 
# Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

s = int(input("Сколько всего журавликов? "))

p = int(s/6)
k = int(2*s/3)

print(f"Катя сделала {k} штук(и), а Петя и Сережа по {p} штук(и)")
