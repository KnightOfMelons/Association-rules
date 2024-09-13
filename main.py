import sys
from apriori_python import apriori
from efficient_apriori import apriori as eff_apriori
from fpgrowth_py import fpgrowth
# Пришлось пойти на данное ухищрение, чтобы кириллица правильно отображалась.
sys.stdout.reconfigure(encoding='utf-8')


def data_generator(filename):
    """
    Data generator
    """
    def data_gen():
        with open(filename) as file:
            for line in file:
                yield tuple(k.strip() for k in line.split(','))

    return data_gen


# Заранее положил все значения из дз по своему варианту сюда, чтобы не использовать
# по тысяче раз.
transactions = [
            ['Корректор','Фломастер','Скетчбук','Тубус','Гуашь','Ватман','Перо','Мальберт'],
            ['Перо','Скетчбук','Фломастер','Корректор','Тубус','Циркуль'],
            ['Мальберт','Палитра','Ватман','Корректор','Фломастер','Скетчбук'],
            ['Мальберт','Ватман','Палитра','Фломастер','Гуашь','Корректор'],
            ['Фломастер','Корректор','Скетчбук','Перо'],
            ['Гуашь','Мальберт','Палитра','Ватман'],
            ['Мальберт','Ватман','Фломастер','Корректор','Фломастер'],
            ['Фломастер','Корректор','Циркуль'],
            ['Скетчбук','Перо','Тубус','Корректор','Фломастер'],
            ['Фломастер','Корректор','Ватман','Циркуль','Скетчбук'],
            ['Циркуль','Фломастер','Корректор','Скетчбук'],
            ['Тубус','Корректор','Скетчбук','Фломастер'],
            ['Перо','Тубус'],
            ['Перо','Ватман','Циркуль'],
            ['Ватман','Скетчбук','Фломастер','Корректор'],
            ['Фломастер','Корректор','Перо','Скетчбук','Циркуль'],
            ['Фломастер','Корректор','Перо'],
            ['Фломастер','Мальберт','Ватман','Корректор'],
            ['Тубус','Циркуль'],
            ['Фломастер','Перо','Скетчбук','Корректор']
        ]


while True:
    choose = int(input("\n1 - Алгоритм Apriori.\n2 - Efficient-Aprioti алгоритм.\n3 - Алгоритм FPGrowth\n0 - Выход.\nВаш выбор: "))

    # Реализация алгоритма Apriori по данным из Excel, Вариант 6.
    if choose ==  1:
        # Это данные с моего домашнего задания, Вариант 6.
        freqItemSet, rules = apriori(transactions, minSup=0.5, minConf=0.5)

        for rule in rules:
            print(rule)

    # Реализация алгоритма Efficient-Apriori по данным из Excel, Вариант 6.
    elif choose == 2:
        freqItemSet, rules = eff_apriori(transactions, min_support=0.5, min_confidence=0.5)

        choose_second = int(input("\n1 - Вывод информации как обычно.\n2 - Вывод информации с помощью lambda\n3 - Запуск чтения из файла тех же значений.\n4 - Вывод частых предметных наборов + инф-ции о количестве встреч.\nВаш выбор: "))
        
        # Вывод как обычно
        if choose_second == 1:
            for rule in rules:
                print(rule)

        # Вывод по lambda функции
        elif choose_second == 2:
            rules_rhs = filter(lambda rule: len(rule.lhs) == 1 and len(rule.rhs) == 1, rules)
            for rule in sorted(rules_rhs, key=lambda rule: rule.confidence):
                print(rule)

        # Вывод из .csv файла
        elif choose_second == 3:
            data_transactions_file_CSV = data_generator('my_dataset.csv')()  
            freqItemSet, rules = eff_apriori(data_transactions_file_CSV, min_support=0.6, min_confidence=0.6)
            
            for rule in rules:
                print(rule)

        # Вывод соответствующих частых предметных наборов, а заодно информации о то, сколько
        # раз они встретились и в каких транзакциях.
        elif choose_second == 4:
            freqItemSet, rules = eff_apriori(transactions, output_transaction_ids=True)
            
            for rule in rules:
                print(rule)

    # Реализация алгоритма FPGrowth по данным из Excel.                
    elif choose == 3:
        freqItemSet, rules = fpgrowth(transactions, minSupRatio=0.5, minConf=0.5)
        
        for rule in rules:
                print(rule)

    # Выход из программы.
    elif choose == 0:
        break

    # Если пользователь написал неверное значение (то, которое отличается от имеющихся вариантов), то он заново предложит ввести вариант ответа.
    else:
        continue