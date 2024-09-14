import sys
# Необходимо для измерения времени работы алгоритмов и всяческих выводов по ним.
import time
from apriori_python import apriori
from efficient_apriori import apriori as eff_apriori
from fpgrowth_py import fpgrowth
# Пришлось пойти на данное ухищрение, чтобы кириллица правильно отображалась.
sys.stdout.reconfigure(encoding='utf-8')


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


def data_generator(filename):
    """
    Data generator
    """
    def data_gen():
        with open(filename) as file:
            for line in file:
                yield tuple(k.strip() for k in line.split(','))

    return data_gen


while True:
    beginning_choose = int(input("\n1 - Работа со своими значениями из Excel (20 вариантов).\n2 - Работа с данными из репозиториев.\n0 - Выход.\nВаш выбор: "))
    
    # Работа со своими значениями, которых 20 и которые придумывали в аудитории. Вариант 6.
    if beginning_choose == 1:
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

    # Работа с данными из репозитория, у меня Вариант 2. https://github.com/viktree/curly-octo-chainsaw/blob/master/BreadBasket_DMS.csv
    elif beginning_choose == 2:
        choose = int(input("\n1 - Алгоритм Apriori для репозитория.\n2 - Efficient-Aprioti алгоритм для репозитория.\n3 - Алгоритм FPGrowth для репозитория.\n0 - Выход.\nВаш выбор: "))
        
        # Беру как раз-таки те значения, которые я сделал с помощью parser_script.py из BreadBasket_DMS.py
        from BreadBasket_DMS import transactions_from_github
        
        # Алгоритм Apriori с элементами из репозитория. Пришлось скрутить minSup и minConf, так как он совсем не работал при больших значениях.
        if choose == 1:
            # Замеряем время начала
            start_time_algo = time.time()

            freqItemSet, rules = apriori(transactions_from_github, minSup=0.06, minConf=0.06)

            # Замеряем время окончания
            end_time_algo = time.time()

            # Замеряем время вывода
            start_time_output = time.time()
            for rule in rules:
                print(rule)
            end_time_output = time.time()

            print(f"\nАлгоритм выполнен за {end_time_algo - start_time_algo:.4f} секунд, вывод занял {end_time_output - start_time_output:.4f} секунд.")

        elif choose == 2:
            # Замеряем время начала
            start_time_algo = time.time()
            freqItemSet, rules = eff_apriori(transactions_from_github, min_support=0.06, min_confidence=0.06)

            # Замеряем время окончания
            end_time_algo = time.time()

            # Замеряем время вывода
            start_time_output = time.time()
            for rule in rules:
                print(rule)
            end_time_output = time.time()

            print(f"\nАлгоритм выполнен за {end_time_algo - start_time_algo:.4f} секунд, вывод занял {end_time_output - start_time_output:.4f} секунд.")

        elif choose == 3:
            # Замеряем время начала
            start_time_algo = time.time()
            freqItemSet, rules = fpgrowth(transactions_from_github, minSupRatio=0.06, minConf=0.06)

            # Замеряем время окончания
            end_time_algo = time.time()

            # Замеряем время вывода
            start_time_output = time.time()
            for rule in rules:
                print(rule)
            end_time_output = time.time()

            print(f"\nАлгоритм выполнен за {end_time_algo - start_time_algo:.4f} секунд, вывод занял {end_time_output - start_time_output:.4f} секунд.")

        # Выход из программы.
        elif choose == 0:
            break

        # Если пользователь написал неверное значение (то, которое отличается от имеющихся вариантов), то он заново предложит ввести вариант ответа.
        else:
            continue

    # Выход из программы.
    elif beginning_choose == 0:
        break

    # Если пользователь написал неверное значение (то, которое отличается от имеющихся вариантов), то он заново предложит ввести вариант ответа.
    else:
        continue
