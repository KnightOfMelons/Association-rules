from apriori_python import apriori

itemSetList = [
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

freqItemSet, rules = apriori(itemSetList, minSup=0.5, minConf=0.5)
print(rules)