# Файл для манипуляций с файлами формата email
import re
import random
import os

EmailWork = ""  # Инициализируем пустой строкой


def InputEmail():  # принимает txt файл с email адресами
    global EmailWork

    try:
        file_path = input("Введите путь к txt файлу: ").strip()

        # Проверка на пустой ввод
        if not file_path:
            print("Ошибка: Путь к файлу не может быть пустым!")
            return False

        file_path = file_path.strip('"').strip("'")

        # Проверяем существование файла
        if not os.path.exists(file_path):
            print(f"Ошибка: Файл '{file_path}' не найден!")
            return False

        # Проверяем, что это файл, а не директория
        if not os.path.isfile(file_path):
            print(f"Ошибка: '{file_path}' не является файлом!")
            return False

        # Сохраняем путь к файлу
        EmailWork = file_path
        print(f"Файл '{file_path}' успешно загружен.")

        # Проверяем, что файл не пустой
        if os.path.getsize(file_path) == 0:
            print("Предупреждение: Файл пустой!")
            return True

        with open(file_path, "r", encoding='utf-8', errors='ignore') as f:
            LenObj = len(f.readlines())

        print(f"Было найдено {LenObj} эмейлов")
        return True

    except PermissionError:
        print(f"Ошибка: Нет прав на чтение файла '{file_path}'!")
        return False
    except UnicodeDecodeError:
        print("Ошибка: Невозможно прочитать файл. Проверьте кодировку!")
        return False
    except Exception as e:
        print(f"Неожиданная ошибка при загрузке файла: {e}")
        return False


def UserSort():  # вытягивает с email-ов юзернеймы
    if not EmailWork:
        print("Сначала загрузите файл с email адресами!")
        return

    try:
        username = []  # хранение юзернеймов отсортированных от доменов

        # Проверка существования файла перед чтением
        if not os.path.exists(EmailWork):
            print(f"Ошибка: Файл '{EmailWork}' больше не существует!")
            return

        with open(EmailWork, "r", encoding='utf-8', errors='ignore') as f:
            content = f.readlines()

        if not content:
            print("Файл пустой!")
            return

        for line_num, line in enumerate(content, 1):
            line = line.strip()  # Удаляем лишние пробелы и переносы
            if not line:  # Пропускаем пустые строки
                continue

            if "@" in line:
                # Проверяем, что email содержит только один @
                if line.count("@") == 1:
                    sortmail = re.split(r"@", line)[0]  # Удаляем домены из емейла
                    # Проверяем, что username не пустой
                    if sortmail:
                        username.append(sortmail)  # добавляем юзер в список
                else:
                    print(f"Предупреждение: Строка {line_num} содержит некорректный email (несколько @): {line}")
            else:
                print(f"Предупреждение: Строка {line_num} не содержит @: {line}")

        if not username:
            print("Не найдено email адресов в файле.")
            return

        FileName = random.randint(1, 9999)
        filename = f"sortmail{FileName}.txt"

        # Проверка на существование файла и создание уникального имени при необходимости
        while os.path.exists(filename):
            FileName = random.randint(1, 9999)
            filename = f"sortmail{FileName}.txt"

        with open(filename, "w", encoding='utf-8') as output_file:
            for user in username:
                output_file.write(user + "\n")

        print(f"Сортировка выполнена успешно.")
        print(f"Было обработано {len(username)} адресов")
        print(f"Файлу присвоено имя {filename}")
        print(f"Путь к файлу: {os.path.abspath(filename)}")

    except PermissionError:
        print(f"Ошибка: Нет прав на запись файла!")
    except Exception as e:
        print(f"Неожиданная ошибка при сортировке: {e}")


def DomenSort():  # Сортировка почт по доменам
    if not EmailWork:
        print("Сначала загрузите файл с email адресами!")
        return

    try:
        domains = [
            # Основные международные (США/Запад)
            "gmail.com",
            "yahoo.com",
            "outlook.com",
            "hotmail.com",
            "aol.com",
            "icloud.com",
            "protonmail.com",
            "mail.com",
            "zoho.com",
            "gmx.com",

            # Европейские
            "web.de",  # Германия
            "gmx.de",  # Германия
            "t-online.de",  # Германия
            "freenet.de",  # Германия
            "online.de",  # Германия
            "arcor.de",  # Германия

            "orange.fr",  # Франция
            "free.fr",  # Франция
            "laposte.net",  # Франция
            "sfr.fr",  # Франция
            "wanadoo.fr",  # Франция

            "libero.it",  # Италия
            "alice.it",  # Италия
            "tin.it",  # Италия

            "telefonica.net",  # Испания
            "terra.es",  # Испания
            "yahoo.es",  # Испания

            "ziggo.nl",  # Нидерланды
            "kpnmail.nl",  # Нидерланды

            "skynet.be",  # Бельгия
            "telenet.be",  # Бельгия

            "bluewin.ch",  # Швейцария
            "sunrise.ch",  # Швейцария

            "chello.at",  # Австрия
            "aon.at",  # Австрия

            "centrum.cz",  # Чехия
            "seznam.cz",  # Чехия

            "o2.pl",  # Польша
            "wp.pl",  # Польша
            "interia.pl",  # Польша

            "freemail.hu",  # Венгрия
            "citromail.hu",  # Венгрия

            "mail.bg",  # Болгария
            "abv.bg",  # Болгария

            "yahoo.co.uk",  # Великобритания
            "btinternet.com",  # Великобритания
            "virginmedia.com",  # Великобритания
            "talktalk.net",  # Великобритания

            # Азиатские/Тихоокеанские
            "naver.com",  # Корея
            "daum.net",  # Корея
            "kakao.com",  # Корея

            "yahoo.co.jp",  # Япония
            "docomo.ne.jp",  # Япония
            "ezweb.ne.jp",  # Япония
            "softbank.ne.jp",  # Япония

            "qq.com",  # Китай
            "163.com",  # Китай
            "126.com",  # Китай
            "sina.com",  # Китай
            "sohu.com",  # Китай

            "yahoo.com.hk",  # Гонконг
            "yahoo.com.tw",  # Тайвань

            "outlook.ph",  # Филиппины
            "yahoo.com.ph",  # Филиппины

            "yahoo.com.sg",  # Сингапур
            "singnet.com.sg",  # Сингапур

            "yahoo.co.id",  # Индонезия
            "yahoo.com.my",  # Малайзия
            "yahoo.co.th",  # Таиланд
            "yahoo.com.vn",  # Вьетнам

            "rediffmail.com",  # Индия
            "indiatimes.com",  # Индия
            "yahoo.co.in",  # Индия

            # Австралия/Новая Зеландия
            "bigpond.com",  # Австралия
            "optusnet.com.au",  # Австралия
            "iinet.net.au",  # Австралия
            "yahoo.com.au",  # Австралия
            "xtra.co.nz",  # Новая Зеландия
            "clear.net.nz",  # Новая Зеландия

            # Канадские
            "rogers.com",  # Канада
            "bell.net",  # Канада
            "telus.net",  # Канада
            "shaw.ca",  # Канада
            "sympatico.ca",  # Канада

            # Латинская Америка
            "yahoo.com.ar",  # Аргентина
            "yahoo.com.br",  # Бразилия
            "uol.com.br",  # Бразилия
            "bol.com.br",  # Бразилия
            "terra.com.br",  # Бразилия
            "yahoo.com.mx",  # Мексика
            "yahoo.com.co",  # Колумбия
            "yahoo.com.ve",  # Венесуэла
            "yahoo.com.pe",  # Перу
            "yahoo.com.ec",  # Эквадор

            # Ближний Восток
            "yahoo.co.il",  # Израиль
            "walla.co.il",  # Израиль
            "012.net.il",  # Израиль

            "yahoo.com.tr",  # Турция
            "mynet.com",  # Турция
            "superonline.com",  # Турция

            "yahoo.com.sa",  # Саудовская Аравия
            "yahoo.com.eg",  # Египет
            "yahoo.com.ae",  # ОАЭ

            # Южная Африка
            "mweb.co.za",  # ЮАР
            "telkomsa.net",  # ЮАР
            "yahoo.co.za",  # ЮАР

            # Университетские/Образовательные (.edu)
            "harvard.edu",
            "stanford.edu",
            "mit.edu",
            "berkeley.edu",
            "ox.ac.uk",
            "cam.ac.uk",

            # Правительственные (.gov)
            "whitehouse.gov",
            "state.gov",
            "nih.gov",
            "nasa.gov",

            # Военные (.mil)
            "army.mil",
            "navy.mil",
            "airforce.mil",

            # Организации (.org)
            "wikipedia.org",
            "redcross.org",
            "greenpeace.org",
            "un.org",
            "who.int",

            # Бизнес/Технологические
            "amazon.com",
            "apple.com",
            "microsoft.com",
            "google.com",
            "meta.com",
            "twitter.com",
            "linkedin.com",
            "uber.com",
            "airbnb.com",
            "spotify.com",
            "netflix.com",
            "paypal.com",
            "ebay.com",
            "shopify.com",
            "salesforce.com",

            # Короткие/Популярные
            "me.com",
            "live.com",
            "msn.com",
            "passport.com",
            "email.com",
            "usa.com",
            "europe.com",
            "asia.com",
            "africa.com",

            # Специализированные
            "doctor.com",
            "lawyer.com",
            "engineer.com",
            "teacher.com",
            "writer.com",
            "artist.com",
            "musician.com",
            "photographer.com",
            "designer.com",
            "programmer.com"
        ]

        # Проверка существования файла перед чтением
        if not os.path.exists(EmailWork):
            print(f"Ошибка: Файл '{EmailWork}' больше не существует!")
            return

        with open(EmailWork, "r", encoding='utf-8', errors='ignore') as f:
            emails = []
            for line_num, line in enumerate(f.readlines(), 1):
                line = line.strip()
                if not line:
                    continue
                if "@" in line and line.count("@") == 1:
                    emails.append(line)
                else:
                    print(f"Предупреждение: Строка {line_num} не является корректным email: {line}")

        if not emails:
            print("Не найдено email адресов в файле.")
            return

        total_domains_found = 0

        # Для каждого домена создаем отдельный список
        for domain in domains:
            domain_emails = []  # Каждый домен - свой список
            for email in emails:
                email_domain = email.split("@")[-1].lower()
                if email_domain == domain:
                    domain_emails.append(email)

            # Создаем файл только если есть email для этого домена
            if domain_emails:
                DomenName = random.randint(1, 9999)
                filename = f"sortdomen_{domain}_{DomenName}.txt"

                # Проверка на существование файла
                while os.path.exists(filename):
                    DomenName = random.randint(1, 9999)
                    filename = f"sortdomen_{domain}_{DomenName}.txt"

                with open(filename, "w", encoding='utf-8') as output_file:
                    for user in domain_emails:
                        output_file.write(user + "\n")

                print(f"Создан файл для домена {domain}:")
                print(f"  Файл: {filename}")
                print(f"  Путь: {os.path.abspath(filename)}")
                print(f"  Найдено email: {len(domain_emails)}")
                total_domains_found += 1

        if total_domains_found == 0:
            print("Не найдено email для указанных доменов.")

    except PermissionError:
        print(f"Ошибка: Нет прав на чтение/запись файла!")
    except Exception as e:
        print(f"Неожиданная ошибка при сортировке по доменам: {e}")


def DetectTrigger():
    if not EmailWork:
        print("Сначала загрузите файл с email адресами!")
        return

    try:
        Triggers = ["Admin", "info", "HR"]
        TrueEmail = []  # Для хранения найденных email

        # Проверка существования файла перед чтением
        if not os.path.exists(EmailWork):
            print(f"Ошибка: Файл '{EmailWork}' больше не существует!")
            return

        with open(EmailWork, "r", encoding='utf-8', errors='ignore') as f:
            content = f.read()  # Читаем весь файл

            # Ищем все email адреса
            emails = re.findall(r'([\w\.-]+)@([\w\.-]+\.\w+)', content)

            if not emails:
                print("Не найдено email адресов в файле.")
                return

            for username, domain in emails:
                # Проверяем, что username и domain не пустые
                if not username or not domain:
                    continue

                # Проверяем каждый триггер в username
                for trigger in Triggers:
                    if trigger.lower() in username.lower():
                        email = f"{username}@{domain}"
                        print(f"Найден триггер '{trigger}' в email: {email}")
                        TrueEmail.append(email)
                        break  # Избегаем дублирования для одного email

        # Сохраняем результаты в файл
        if TrueEmail:
            TriggerName = random.randint(1, 9999)
            filename = f"sorttriger{TriggerName}.txt"

            # Проверка на существование файла
            while os.path.exists(filename):
                TriggerName = random.randint(1, 9999)
                filename = f"sorttriger{TriggerName}.txt"

            with open(filename, "w", encoding='utf-8') as output_file:
                for email in TrueEmail:
                    output_file.write(email + "\n")

            print(f"\nУспешная сортировка по триггерам.")
            print(f"Найдено email с триггерами: {len(TrueEmail)}")
            print(f"Файл: {filename}")
            print(f"Путь: {os.path.abspath(filename)}")
        else:
            print("Не найдено email с указанными триггерами.")

    except PermissionError:
        print(f"Ошибка: Нет прав на чтение/запись файла!")
    except Exception as e:
        print(f"Неожиданная ошибка при поиске триггеров: {e}")




def EmailPassword():
    """Отделение Email от пароля в формате email:password"""
    if not EmailWork:
        print("Сначала загрузите файл с email адресами!")
        return

    try:
        emailNotpass = []  # Отделение Емейла,от пароля.
        passNOTemail = []  # Отделение ПАРОЛЯ от домена

        # Проверка существования файла перед чтением
        if not os.path.exists(EmailWork):
            print(f"Ошибка: Файл '{EmailWork}' больше не существует!")
            return

        with open(EmailWork, "r", encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()

        if not lines:
            print("Файл пустой!")
            return

        valid_entries = 0
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            if not line:
                continue

            if ":" in line:
                # Проверяем, что строка содержит только одно двоеточие или берем первое
                parts = line.split(":", 1)
                leftside = parts[0].strip()
                rightsight = parts[1].strip() if len(parts) > 1 else ""

                # Проверяем, что email содержит @
                if "@" in leftside:
                    emailNotpass.append(leftside)
                    if rightsight:  # Проверяем, что пароль не пустой
                        passNOTemail.append(rightsight)
                    else:
                        print(f"Предупреждение: Строка {line_num} имеет пустой пароль: {line}")
                    valid_entries += 1
                else:
                    print(f"Предупреждение: Строка {line_num} не содержит email в левой части: {line}")
            else:
                print(f"Предупреждение: Строка {line_num} не содержит разделитель ':' : {line}")

        if valid_entries == 0:
            print("Не найдено валидных записей в формате email:password")
            return

        randomname = random.randint(1, 9999)

        # Создание файлов с проверкой на существование
        filename1 = f"SORT-email-{randomname}.txt"
        filename2 = f"SORT-password-{randomname}.txt"

        while os.path.exists(filename1) or os.path.exists(filename2):
            randomname = random.randint(1, 9999)
            filename1 = f"SORT-email-{randomname}.txt"
            filename2 = f"SORT-password-{randomname}.txt"

        with open(filename1, "w", encoding='utf-8') as f:
            for email in emailNotpass:
                f.write(email + "\n")

        with open(filename2, "w", encoding='utf-8') as f:
            for password in passNOTemail:
                f.write(password + "\n")

        print(f"Успешно отделено {len(emailNotpass)} Эмейлов.")
        print(f"Было создано 2 файла:")
        print(f"  {filename1} путь {os.path.abspath(filename1)} ({len(emailNotpass)} значений)")
        print(f"  {filename2} путь {os.path.abspath(filename2)} ({len(passNOTemail)} значений)")

    except PermissionError:
        print(f"Ошибка: Нет прав на чтение/запись файла!")
    except Exception as e:
        print(f"Неожиданная ошибка при обработке email:password: {e}")










