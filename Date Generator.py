def date():
    import random
    random.randint(1,100)
    import random
    random.choice

    day = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    month = ['January', 'February','March','April', 'May','June', 'July','August', 'September', 'October', 'November', 'December']
    x = range(1,31)
    th = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,24,25,26,27,28,29,30,]
    st = [1,21,31]
    nd = [2,22]
    rd= [3,23]

    year = random.randint(2000,2023)
    temp = random.randint(1,120)
    temperature = f'{temp} degrees F.'

    ran_date = random.choice(x)

    str(random.choice(th)) + str('th')
    str(random.choice(st)) + str('st')
    str(random.choice(nd))+ str('nd')
    str(random.choice(rd))+ str('rd')
    
    if ran_date in th:
         con_date = str(ran_date) + str('th')
    elif ran_date in st:
         con_date =str(ran_date) + str('st')       
    elif ran_date in nd:
         con_date = str(ran_date) + str('nd')    
    elif ran_date in rd:
        con_date = str(ran_date) + str('rd')

    print(f"Today is {random.choice(day)}, {random.choice(month)} {con_date} {year}. It is currently {temperature}")

date()