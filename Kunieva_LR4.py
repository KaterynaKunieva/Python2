# 1. Списки 
# a)
list1 = [*range(0, 100, 10)]
list2 = [*range(0, 100, 10)]
# b) 
b = list1.pop(2)
print(b)
# c) 
list2[-1] = 200 
print(list2)
# d) 
list3 = list1 + list2 
print(list3)
# e) 
list4 = list3[7:-5]
print(list4)
# f) 
list4.append(13)
list4.insert(3, 12)
print(list4)
# g) 
minimun = min(list3)
maximum = max(list3)
print(minimun, maximum)

# 2. Кортежі
# a)
tuple1 = tuple(range(1, 26))
tuple2 = ('Буртовий', 'Вовк', 'Голик', 'Доан', 'Завірюха', 'Іваницький', 'Кунєва', 'Лебедєва', 'Мартинюк', 'Марченко', 'Маяраш', 'Мень', 'Меркотан', 'Мороз', 'Пархоменко', 'Петроченко', 'Півчук', 'Поєнко', 'Смирнов', 'Франчук', 'Чугай', 'Чулан', 'Шамаріна', 'Швиденко', 'Шевченко')
tuple3 = tuple(zip(tuple1, tuple2)) 
# або
(Буртовий, Вовк, Голик, Доан, Завірюха, Іваницький, Кунєва, Лебедєва, Мартинюк, Марченко, Маяраш, Мень, Меркотан, Мороз, Пархоменко, Петроченко, Півчук, Поєнко, Смирнов, Франчук, Чугай, Чулан, Шамаріна, Швиденко, Шевченко) = tuple1
# b)
surname = 'Кунєва'
num = next(x[0] for x in tuple3 if x[1]== surname)
print(num)
# або
print(Кунєва)
# c) 
tuple4 = tuple1+tuple2
print(tuple4)
# d)
tuple5 = tuple4[20:-10]
print(tuple5)

# 3. Словники 
# a) 
ff = {'IE:301': 24, 'IK-301': 14, 'IH-301': 31, 'IA-301': 20, 'IK-301k': 5, 'IK-301k': 25, 'IA-301k': 5}
print(ff)
# b) 
try: 
    group = input('Group: ')
    res = ff[group] 
except: 
    res = 'Такої групи на ІІТЕ не існує'
print(res)
# АБО
group = input('Group: ')
if group in ff: 
    res = ff[group] 
else: 
    res = 'Такої групи на ІІТЕ не існує'
print(res)

# c) 
ff['IA-301'] = 21
ff['IK-301'] = 15
ff['IH-301'] = 30
print(ff)
# d) 
ff['IH-302'] = 27
print(ff)
# e) 
ff['IH-301'] += ff['IH-302']
del(ff['IH-302']) 
print(ff)