# Варіант 7 (предметна область - BankChurners)
# CLIENTNUM - номер клієнта 
# Attrition_Flag - активність клієнта (якщо обліковий запис закрит - 1, інакше - 0)
# Customer_Age - вік клієнт 
# Gender - гендер 
# Dependent_count - кількість утриманців 
# Education_Level - рівень освіти 
# Marital_Status - сімейний статус
# Income_Category - категорія доходу 
# Card_Category - тип карти 
# Months_on_book - період користування банком 

# Частина 1. Написання базових функцій для програми аналізу даних 
import csv
# перетворення даних з файлу у списки або словники: 
def csv_to_dict(p, c='utf-8', nl='', dl=',', dic=True): 
    with open(p, encoding=c, newline=nl) as r_file: 
        if dic: 
            parser = csv.DictReader 
        else: 
            parser = csv.reader 
        result = [fields for fields in parser(r_file, delimiter = dl)] 
    return result

# групування масиву даних (списку зі словниками) за значенням колонки та визначення кількості позицій у кожній групі (у абсолютних та відносних значеннях)
# функція, яка аналізує вкладений список 
def count_lists_by(key, array): 
    result = {}
    array = array[1:] 
    for row in array: 
        val = row[key-1] or 'UNDEFINED' 
        if (val in result): 
            result[val] += 1
        else: 
            result[val] = 1
    return result
# функція для розрахунку відносних значень результатів фільтрування 
def entries_to_percent(entries, total):  
    result = {}
    for key in entries: 
        count = entries[key] 
        result[key] = str(round(count/total * 100, 2)) + '%' 
    return result 

# сортування згрупованих даних у словник за зростанням або спаданням значень 
def entries_sort(entries, sort_type = True, n = None): 
    sorted_tuples = sorted(entries.items(), key=lambda item: item[1], reverse = sort_type)[:n]
    sorted_dict = {key: value for key, value in sorted_tuples}
    return sorted_dict

# визначення кількості клієнтів у вікових категоріях
def category(array, start, step = 10): 
    result = {}
    for i in array.keys(): 
        if start<=int(i)<=start+step: 
            result[start+step] = array[i]
            start += step 
    return result 

# Частина 2. Розв'зання задач із завдання
# Завдання 2. Вивести інформацію про загальну кількість рядків та колонок у файлі з перерахуванням їх назв.
path1 = 'BankChurners.csv' 
result_dict = csv_to_dict(path1) 
result_list = csv_to_dict(path1, dic=False) 
r_total = len(result_list)-1  
c_total = len(result_list[0])  
print(f'Файл {path1} містить {c_total} колонки. ')
print(f'Файл {path1} містить такі колонки: {result_list[0]}')
print(f'Файл {path1} містить {r_total} записів')
print(f'Файл {path1} містить такі записи: {result_dict[1:-1]}')

# Завдання 3. тип - 1. вхідні дані перетворити у вкладений список списків та працювати далі з цим типом даних.
result_list = csv_to_dict(path1, dic=False)

# Завдання 4. Розподіл чоловіків і жінок у абсолютних і відносних значеннях
counted_lists_gender = count_lists_by(4, result_list)
percents_lists_gender = entries_to_percent(counted_lists_gender, len(result_list))
print('Групування списку за значенням Gender: ')
print(f'У абсолютних значеннях: \n{counted_lists_gender}')
print(f'У відносних значеннях: \n{percents_lists_gender}')

# Завдання 5. Сортування даних за категорією картки (Card_Category) у порядку зростання їх кількості у кожній категорії (категорія картки, кількість у %, абсолютна кількість)
counted_lists_card_category = count_lists_by(9, result_list)
percents_lists_card_category = entries_to_percent(counted_lists_card_category, len(result_list))
sorted_counted_minmax_list_card_category = entries_sort(counted_lists_card_category, False)
sorted_percents_minmax_list_card_category = entries_sort(percents_lists_card_category, False)
print(f'Сортування значень за категорією картки у порядку зростання (абсолютні значення): {sorted_counted_minmax_list_card_category}')
print(f'Сортування значень за категорією картки у порядку зростання (відносні значення): {sorted_percents_minmax_list_card_category}')

# Завдання 6. Скільки власників карток у абсолютних та відносних значеннях у кожному віковому діапазоні (Сustomer_Age) від 25 років до макс. значення з кроком 10.
counted_lists_customer_age = count_lists_by(3, result_list) 
percents__lists_customer_age = entries_to_percent(counted_lists_customer_age, len(result_list))
age_c = category(counted_lists_customer_age, 25)
age_p = category(percents__lists_customer_age, 25)
print(f'Кількість власників карток у віковому діапазоні (абсолютні значення) = {age_c}')
print(f'Кількість власників карток у віковому діапазоні (відносні значення) = {age_p}')