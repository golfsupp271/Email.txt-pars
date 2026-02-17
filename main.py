import sys
from banners import print_neon_style
from CheckMail import InputEmail
from CheckMail import UserSort
from CheckMail import DomenSort
from CheckMail import DetectTrigger
from CheckMail import EmailPassword
from PhoneNumbers import CheckNumber


def main():
    """Основная функция программы"""
    try:
        print_neon_style()


        InputEmail()

        while True:
            print("\n" + "=" * 50)
            print("Текущий файл:", getattr(sys.modules['CheckMail'], 'EmailWork', 'Не загружен'))
            print("=" * 50)
            print("Выберите действие:")
            print("1 - Отсеять Имя от Доменов")
            print("2 - Сортировать по доменам")
            print("3 - Поиск нужных почт по триггерным словам")
            print("4 - Сменить путь к файлу")
            print("5 - Отделить email от pass TXT ФОРМАТА EMAIL:PASSWORD")
            print("6 - Детект телефонных номеров в файле")
            print("7 - Google Dork поиск и извлечение email с результатов")
            print("0 - Выход")
            print("=" * 50)

            try:
                user_input = input("Ваш выбор: ").strip()

                if not user_input:
                    print("Ошибка: Ввод не может быть пустым!")
                    continue  #

                if not user_input.isdigit():
                    print("Ошибка: Введите число от 0 до 7!")
                    continue  #

                choice = int(user_input)

                if choice == 0:
                    print("Выход из программы...")
                    break
                elif choice == 1:
                    UserSort()
                elif choice == 2:
                    DomenSort()
                elif choice == 3:
                    DetectTrigger()
                elif choice == 4:
                    InputEmail()
                elif choice == 5:
                    EmailPassword()
                elif choice == 6:
                    from CheckMail import EmailWork
                    CheckNumber(EmailWork)

                else:
                    print("Ошибка: Число должно быть от 0 до 7!")


                print("\n" + "-" * 30)

            except KeyboardInterrupt:
                print("\n\nВыход по требованию пользователя...")
                break
            except Exception as e:
                print(f"Произошла ошибка: {e}")


    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем.")
    except Exception as e:
        print(f"Критическая ошибка: {e}")
    finally:
        print("\nСпасибо за использование программы!")


if __name__ == "__main__":
    main()