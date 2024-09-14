import pandas as pd

# Суть этого скрипта проста - он берет твой файл .csv, который ты должен был скачать с GitHub по варианту и затем обрабатывает его
# делая из него .py файл со структурированной информацией, с которой в последствии можно комфортно работать.
# Просто скачать свой .csv файл, кинь его в корневую папку и вставь в file_path = 'СЮДА'


# Загружаем CSV файл
file_path = 'BreadBasket_DMS.csv'  # Укажи путь к своему файлу
df = pd.read_csv(file_path)

# Проверяем, как выглядят данные, и заголовки
print("Столбцы перед обработкой:", df.columns)

# Убираем первую строчку, если она дублирует заголовки, и заменяем названия столбцов
df.columns = df.columns.str.strip()  # Убираем лишние пробелы из названий столбцов

# Теперь группируем данные по Transaction и собираем Item в списки
grouped = df.groupby('Transaction')['Item'].apply(list).tolist()

# Преобразуем элементы внутри каждого списка в строки без кавычек
grouped = [[item for item in transaction] for transaction in grouped]

# Создаем строку для записи в файл Python
transactions_str = "transactions_from_github = [\n"
transactions_str += ',\n'.join([str(transaction) for transaction in grouped])
transactions_str += "\n]"

# Сохраняем в Python файл
with open("BreadBasket_DMS.py", "w") as f:
    f.write(transactions_str)

print("Файл BreadBasket_DMS.py успешно создан!")