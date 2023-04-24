#диференційована схема
def def_credit(amount, months, interests): 
    debt_remainder = amount # залишок 
    rows, cols = (months, 5)
    result = [[0 for i in range(cols)] for j in range(rows)]
    payment = []
    sum_amount_percent = 0
    sum_amount = 0
    for i in range(0, months):
        if i != months: 
            amount_per_month = debt_remainder/(months-i) # погашення основного боргу  
        amount_percent_per_month = debt_remainder*interests/1200 # погашення відсотків
        sum_amount_percent += amount_percent_per_month
        sum_amount += amount_per_month
        payment.append(i+1) # Період  
        payment.append(debt_remainder) # Залишок по кредиту 
        payment.append(amount_per_month) # Погашення боргу 
        payment.append(amount_percent_per_month) # Погашення відсотків
        payment.append(amount_per_month+amount_percent_per_month) # Щомісячний платіж 
        for j in range(0, len(payment)): 
            result[i][j] = round(payment[j], 2)
        payment.clear()
        debt_remainder -= amount_per_month # зміна залишку основної суми 
    sum_amount += sum_amount_percent
    result = tuple((result, round(sum_amount_percent, 2), round(sum_amount, 2)))
    return result

# ануїтетна схема 
def anu_credit(amount, months, percent): 
    percent = (percent/100)/12 # відсоток 
    k = (percent*((1+percent)**months))/(((1+percent)**months)-1) # коефіцієнт ануїтету
    A = k*amount # щомісячний платіж 
    payment = [] 
    rows, cols = (months, 5)
    result = [[0 for i in range(cols)] for j in range(rows)]
    sum_amount_percent = 0
    sum_amount = 0
    for i in range(0, months): # період 
        amount_percent_per_month = amount*percent # відсотки 
        amount_per_month = A - amount_percent_per_month # основний борг 
        sum_amount_percent += amount_percent_per_month # переплата по відсотках 
        sum_amount += amount_per_month
        payment.append(i+1) # Період  
        payment.append(amount) # Залишок по кредиту 
        payment.append(amount_per_month) # Погашення основного боргу 
        payment.append(amount_percent_per_month) # Погашення відсотків
        payment.append(amount_per_month+amount_percent_per_month) # Щомісячний платіж
        amount -= amount_per_month
        for j in range(0, len(payment)): 
            result[i][j] = round(payment[j], 2)
        payment.clear() 
    sum_amount += sum_amount_percent    
    result = tuple((result, round(sum_amount_percent, 2), round(sum_amount, 2)))
    return result