
## Файл для итераций с телефонами
import os
import random


phone_country_codes = {
    "+30": {"country": "греция", "length": 12},
    "+31": {"country": "нидерланды", "length": 11},
    "+32": {"country": "бельгия", "length": 11},
    "+33": {"country": "франция", "length": 11},
    "+34": {"country": "испания", "length": 11},
    "+35": {"country": "португалия", "length": 11},
    "+36": {"country": "венгрия", "length": 11},
    "+39": {"country": "италия", "length": 12},
    "+40": {"country": "румыния", "length": 11},
    "+41": {"country": "швейцария", "length": 11},
    "+43": {"country": "австрия", "length": 12},
    "+44": {"country": "великобритания", "length": 12},
    "+45": {"country": "дания", "length": 10},
    "+46": {"country": "швеция", "length": 11},
    "+47": {"country": "норвегия", "length": 10},
    "+48": {"country": "польша", "length": 11},
    "+49": {"country": "германия", "length": 12},
    "+351": {"country": "португалия", "length": 11},
    "+352": {"country": "люксембург", "length": 11},
    "+353": {"country": "ирландия", "length": 11},
    "+354": {"country": "исландия", "length": 9},
    "+355": {"country": "албания", "length": 11},
    "+356": {"country": "мальта", "length": 10},
    "+357": {"country": "кипр", "length": 10},
    "+358": {"country": "финляндия", "length": 11},
    "+359": {"country": "болгария", "length": 11},
    "+370": {"country": "литва", "length": 10},
    "+371": {"country": "латвия", "length": 10},
    "+372": {"country": "эстония", "length": 10},
    "+376": {"country": "андорра", "length": 8},
    "+377": {"country": "монако", "length": 10},
    "+378": {"country": "сан-марино", "length": 10},
    "+381": {"country": "сербия", "length": 11},
    "+382": {"country": "черногория", "length": 10},
    "+385": {"country": "хорватия", "length": 11},
    "+386": {"country": "словения", "length": 10},
    "+387": {"country": "босния и герцеговина", "length": 10},
    "+389": {"country": "северная македония", "length": 10},
    "+420": {"country": "чехия", "length": 11},
    "+421": {"country": "словакия", "length": 11},
    "+423": {"country": "лихтенштейн", "length": 9},
    "+90": {"country": "турция", "length": 12},
    "+91": {"country": "индия", "length": 12},
    "+92": {"country": "пакистан", "length": 12},
    "+93": {"country": "афганистан", "length": 11},
    "+94": {"country": "шри-ланка", "length": 11},
    "+95": {"country": "мьянма", "length": 11},
    "+98": {"country": "иран", "length": 12},
    "+966": {"country": "саудовская аравия", "length": 11},
    "+971": {"country": "оаэ", "length": 11},
    "+972": {"country": "израиль", "length": 11},
    "+973": {"country": "бахрейн", "length": 10},
    "+974": {"country": "катар", "length": 10},
    "+975": {"country": "бутан", "length": 10},
    "+976": {"country": "монголия", "length": 10},
    "+977": {"country": "непал", "length": 12},
    "+992": {"country": "таджикистан", "length": 11},
    "+993": {"country": "туркменистан", "length": 10},
    "+994": {"country": "азербайджан", "length": 11},
    "+995": {"country": "грузия", "length": 11},
    "+996": {"country": "киргизия", "length": 11},
    "+998": {"country": "узбекистан", "length": 11},
    "+81": {"country": "япония", "length": 12},
    "+82": {"country": "южная корея", "length": 12},
    "+84": {"country": "вьетнам", "length": 11},
    "+86": {"country": "китай", "length": 13},
    "+852": {"country": "гонконг", "length": 10},
    "+853": {"country": "макао", "length": 10},
    "+855": {"country": "камбоджа", "length": 11},
    "+856": {"country": "лаос", "length": 11},
    "+880": {"country": "бангладеш", "length": 12},
    "+886": {"country": "тайвань", "length": 11},
    "+1": {"country": "сша/канада", "length": 11},
    "+52": {"country": "мексика", "length": 12},
    "+54": {"country": "аргентина", "length": 12},
    "+55": {"country": "бразилия", "length": 13},
    "+56": {"country": "чили", "length": 11},
    "+57": {"country": "колумбия", "length": 12},
    "+58": {"country": "венесуэла", "length": 12},
    "+591": {"country": "боливия", "length": 10},
    "+592": {"country": "гайана", "length": 9},
    "+593": {"country": "эквадор", "length": 11},
    "+595": {"country": "парагвай", "length": 11},
    "+598": {"country": "уругвай", "length": 10},
    "+501": {"country": "белиз", "length": 9},
    "+502": {"country": "гватемала", "length": 10},
    "+503": {"country": "сальвадор", "length": 10},
    "+504": {"country": "гондурас", "length": 10},
    "+505": {"country": "никарагуа", "length": 10},
    "+506": {"country": "коста-рика", "length": 10},
    "+507": {"country": "панама", "length": 10},
    "+509": {"country": "гаити", "length": 10},
    "+1242": {"country": "багамы", "length": 10},
    "+1246": {"country": "барбадос", "length": 10},
    "+1473": {"country": "гренада", "length": 10},
    "+1758": {"country": "сент-люсия", "length": 10},
    "+1767": {"country": "доминика", "length": 10},
    "+1784": {"country": "сент-винсент", "length": 10},
    "+1809": {"country": "доминиканская республика", "length": 10},
    "+1868": {"country": "тринидад и тобаго", "length": 10},
    "+1876": {"country": "ямайка", "length": 10}
}


def CheckNumber(EmailWork):
    """Проверка и извлечение телефонных номеров из email адресов"""


    if not EmailWork:
        print("Сначала загрузите файл с email адресами!")
        return

    if not isinstance(EmailWork, str):
        print("Ошибка: Неверный формат пути к файлу!")
        return

    try:

        if not os.path.exists(EmailWork):
            print(f"Ошибка: Файл '{EmailWork}' не найден!")
            return

        if not os.path.isfile(EmailWork):
            print(f"Ошибка: '{EmailWork}' не является файлом!")
            return

        if os.path.getsize(EmailWork) == 0:
            print("Предупреждение: Файл пустой!")
            return

        chisla = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        MaybeNumbers = []  # Хранение эмейлов без доменов (если только числа)
        MaybeNumbers1 = []  # Хранение чтоб подходило под длинну

        # Чтение файла с обработкой ошибок кодировки
        try:
            with open(EmailWork, mode="r", encoding='utf-8', errors='ignore') as file:
                lines = file.readlines()
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return

        if not lines:
            print("Файл пустой!")
            return

        # Проверка что email состоит только из чисел
        valid_lines = 0
        for line_num, line in enumerate(lines, 1):
            email = line.strip()
            if not email:
                continue

            if "@" in email:
                if email.count("@") == 1:
                    localPart = email.split("@")[0]  # убираем домен
                    if localPart and all(char in chisla for char in localPart):
                        MaybeNumbers.append(localPart)
                        valid_lines += 1
                else:
                    print(f"Предупреждение: Строка {line_num} содержит некорректный email: {email}")
            else:
                # Пропускаем строки без @, так как ищем именно в email адресах
                pass

        if valid_lines == 0:
            print("Не найдено email адресов с числовыми именами.")
            return

        # Проверка на количество символов
        for check in MaybeNumbers:
            if check and 9 <= len(check) <= 13:  # чекаем чтоб подходило под длинну
                MaybeNumbers1.append(check)

        if not MaybeNumbers1:
            print("Не найдено номеров подходящей длины.")
            return

        VALIDnumbers = []  # ВАЛИДНЫЕ НОМЕРА!

        # Проверка номера на валидность
        for CheckValid in MaybeNumbers1:
            if not CheckValid:
                continue

            found_valid = False
            # ПРОВЕРЯЕМ ТЕЛЕФОННЫЕ КОДА ОТ 1 ДО 4 ЗНАЧНЫХ
            for i in range(1, min(5, len(CheckValid) + 1)):
                resultscode = "+" + CheckValid[:i]
                if resultscode in phone_country_codes:
                    if len(CheckValid) == phone_country_codes[resultscode]["length"]:
                        VALIDnumbers.append(CheckValid)
                        found_valid = True
                        break

            if not found_valid:
                print(f"Предупреждение: Номер {CheckValid} не соответствует ни одному коду страны")

        if not VALIDnumbers:
            print("Не найдено валидных телефонных номеров.")
            return

        """Создание файла для записи"""
        randomname = random.randint(1, 9999)
        filename = f"NUMBERS{randomname}.txt"

        # Проверка на существование файла
        while os.path.exists(filename):
            randomname = random.randint(1, 9999)
            filename = f"NUMBERS{randomname}.txt"

        try:
            with open(filename, mode="w", encoding='utf-8') as file:
                for tempnumbr in VALIDnumbers:
                    file.write(tempnumbr + "\n")
        except PermissionError:
            print(f"Ошибка: Нет прав на запись файла {filename}")
            return
        except Exception as e:
            print(f"Ошибка при записи файла: {e}")
            return

        print(f"Успешно! Было извлечено {len(VALIDnumbers)} номеров.")
        print(f"Название файла: {filename}.")
        print(f"Путь к файлу: {os.path.abspath(filename)}.")

    except Exception as e:
        print(f"Неожиданная ошибка при обработке номеров: {e}")












