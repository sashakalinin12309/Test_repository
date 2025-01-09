# Это просто симулятор взлома Пентагона с множествами сценариев! 
# Ненастоящий взлом! FAKE HACKING! 
# Надеюсь, меня никакие взрослые дяди не возьмут и не увезут в Америку за якобы "взлом"! 

# Импортируем все нужные нам модули.
import time
import random

percent = 0  # Счетчик процентов.

percent_final1 = random.randint(1, 200)  # До какого момента должны доходить проценты.
script_for_not_hacked = random.randint(1, 2)  # Выбор сценария для "неуспешной" попытки взлома.
script_for_yes_hacked = random.randint(1, 500)  # Выбор сценария для "успешной" попытки взлома.

# Вступительная часть.
print("\033[32m\0" 'Password hacking...\n') 
time.sleep(3)
print("\033[32m\0" 'The Pentagon password has been hacked...\n') 
time.sleep(2)
print("\033[32m\0" 'Starting hacking...\n') 
time.sleep(2)
# Конец вступительной части.

# Выбор в соответствии с полученными числами.

# Первая концовка: '''Ошибка всей жизни'''.
if percent_final1 < 100 and script_for_not_hacked == 1:
    
    while percent <= percent_final1:  # До какого момента будут идти проценты.
        
        print("\033[32m\0" 'Hack Pentagon', percent, '%', '..' * 49)  # Печать процентов в консоли зеленым цветом.
        
        time.sleep(0.1)  # Небольшой отдых, чтоб не сразу узнали исход.
        percent += 1  # Постепенное увеличение процента.
  
    print()
    print('ERROR.............')  # Вывод конечного текста об ошибке.
    
# Вторая концовка: '''А начиналось так красиво!.. '''.
elif percent_final1 < 100 and script_for_not_hacked == 2:
    
    while percent <= percent_final1:  # До какого момента будет продолжаться.
        
        print("\033[32m\0" 'Hack Pentagon', percent, '%', '..' * 49)  # Печать процесса.
        
        time.sleep(0.1)  # Небольшой промежуток.
        percent += 1  # Постепенно увеличиваем проценты.
  
    print()
    print('The Pentagon was not hacked! The US military quickly discovered and fixed the problem.') 
    # Немногое осуществимо на практике.

# Третья - десятая концовки.
# Данные концовки будет делится на несколько: 6 обычных и 1 суперредкая.
# Суперредкую нежелательно ловить =)  
elif percent_final1 >= 100 and script_for_yes_hacked < 450:
    
    while percent <= 100:  # Повторять пока процент меньше или равно 100.
        
        print("\033[32m\0" 'Hack Pentagon', percent, '%', '..' * 49)  
        
        time.sleep(0.1)  # И снова небольшой промежуток.
        percent += 1
    
    print()
    print("\033[32m\0" 'The Pentagon has been hacked!')  # Ура, свершилось! 
    
    bomb_final_or_not = random.randint(1, 1000)  # Переменная, от которой зависит суперредкая концовка.
    new_percent_final = random.randint(1, 200)  # До какого момента будут доходить проценты.
    the_end = random.randint(1, 4)  # Выбор концовки.
    
    # Начало поиска информации.
    print('')
    time.sleep(2)
    print("\033[32m\0" 'Search for classified information...\n')
    time.sleep(5)
 
    new_percent = 0  # Проценты под новые концовки.
    
 # Несуперредкая концовка.
    if bomb_final_or_not < 1000:
        
        # Хорошие и нейтральная концовки.
        if new_percent_final >= 100:
            
            # Третья концовка: '''Привет из космоса''', или '''Земля в илюминаторе...'''.
            if the_end == 1:
                
                while new_percent <= 100:  # До какого момента.
                    
                    print("\033[32m\0" 'Hacking files...', new_percent, '%', '..' * 48)
                    
                    time.sleep(0.1)  # Ну опять промежутки временем.
                    new_percent += 1  # Снова постепенное увеличение процесса.
    
                print('Secret data about aliens has been discovered!')
                
            # У всех циклов одинаковое строение, поэтому дальнейшие указания будут бессмысленными.
            
            # Четвертая концовка: '''Привет из глубин''', или '''Не, на рыбалку теперь не езжу!'''.
            elif the_end == 2:
                
                while new_percent <= 100:
                    
                    print("\033[32m\0" 'Hacking files...', new_percent , '%', '..' * 48)
                    
                    time.sleep(0.1)
                    new_percent += 1
    
                print('Secret data about the sea monster has been discovered!')
                
                
            # Пятая концовка: '''Военный стратег'''.
            elif the_end == 3:
                
                while new_percent <= 100:
                    
                    print("\033[32m\0" 'Hacking files...', new_percent, '%', '..' * 48)
                    
                    time.sleep(0.1)
                    new_percent += 1
    
                print('Secret information about military facilities has been discovered!')
                
                
            # Шестая концовка: '''Зачем все это, заче-е-ем?!'''.
            elif the_end == 4:
                
                while new_percent <= 100:
                    
                    print("\033[32m\0" 'Hacking files...', new_percent,  '%', '..' * 48)
                    
                    time.sleep(0.1)
                    new_percent += 1
    
                print('No secret documents were found...')
                
                
        # Плохая и нейтральная концовки.
        if new_percent_final < 100:
            
            # Концовка семь: '''@₽₽()₽!'''
            if the_end < 2:
                
                while new_percent <= new_percent_final:
                    
                    print("\033[32m\0" 'Hacking files...', new_percent, '%', '..' * 48)
                    
                    time.sleep(0.1)
                    new_percent += 1
    
                print('ERROR' * 3, sep='.........')
                
                
      # Восьмая концовка: '''Будто прибили укусившего комара!'''.
            elif the_end >= 2:
                
                while new_percent <= new_percent_final:
                    
                    print("\033[32m\0" 'Hacking files...', new_percent, '%', '..' * 48)
                    
                    time.sleep(0.1)
                    new_percent += 1
    
                print('The Pentagon noticed the leak and fixed it. And they figured you out by IP...')
                
    # Суперредкая, девятая концовка: '''Малейшая неисправность приводит к взрыву!'''.         
    else:
        
        bomb_final_percent = random.randint(1, 99)  # Конечный процент в данной концовке.
        
        while bomb_final_percent <= new_percent_final:
            
            print("\033[32m\0" 'Hacking files...', new_percent, '%', '..' * 48)
            
            time.sleep(0.1)
            new_percent += 1
            bomb_final_percent += 1
            
        while True:  # Бесконечный цикл, из-за чего будет бесконечно повторяться только одно:
            
            print('Errorrrrrrrrrrrrrrrrrr..! %) (/+==::&₽5%+', end='')
            
# Десятая концовка: ''' Беги, дорогая, беги! '''.    
elif percent_final1 >= 100 and script_for_yes_hacked >= 450:
    
    while percent <= 100:
        
        print("\033[32m\0" 'Hack Pentagon', percent, '%', '..' * 49)
        time.sleep(0.1)
        percent += 1

        print('')
        print('The Pentagon has been hacked!.. They have come for you. \n Run!')
