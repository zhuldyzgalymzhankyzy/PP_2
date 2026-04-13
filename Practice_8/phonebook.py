import psycopg2
from config import load_config

def get_connection():
    try:
        return psycopg2.connect(**load_config())
    except Exception as error:
        print(f"Ошибка подключения: {error}")
        return None

def search_pattern(pattern):
    conn = get_connection()
    if not conn: return
    try:
        with conn, conn.cursor() as cur:
            cur.execute("SELECT * FROM get_contacts_by_pattern(%s)", (pattern,))
            results = cur.fetchall()
            print("\nРезультаты поиска:")
            for row in results:
                print(f"- {row[0]}: {row[1]}")
            if not results:
                print("Ничего не найдено.")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        conn.close()

def upsert_user(name, phone):
    conn = get_connection()
    if not conn: return
    try:
        with conn, conn.cursor() as cur:
            cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
        print(f"Контакт '{name}' добавлен/обновлен.")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        conn.close()


def bulk_insert(names, phones):
    conn = get_connection()
    if not conn: return
    try:
        with conn, conn.cursor() as cur:
            cur.execute("CALL bulk_insert_contacts(%s, %s)", (names, phones))
        print("Массовая вставка завершена.")
        print("Проверь pgAdmin (NOTICE сообщения для ошибок)")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        conn.close()

def paginated_query(limit, offset):
    conn = get_connection()
    if not conn: return
    try:
        with conn, conn.cursor() as cur:
            cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
            results = cur.fetchall()
            print(f"\nКонтакты (Limit: {limit}, Offset: {offset}):")
            for row in results:
                print(f"- {row[0]}: {row[1]}")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        conn.close()

def delete_user(search_val):
    conn = get_connection()
    if not conn: return
    try:
        with conn, conn.cursor() as cur:
            cur.execute("CALL delete_contact(%s)", (search_val,))
        print(f"🗑 Удалено: {search_val}")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        conn.close()

def main():
    while True:
        print("\n--- PHONEBOOK ---")
        print("1. Поиск")
        print("2. Добавить/Обновить")
        print("3. Массовая вставка")
        print("4. Pagination")
        print("5. Удалить")
        print("6. Выход")

        choice = input("Выбор: ")

        if choice == '1':
            pattern = input("Введите текст: ")
            search_pattern(pattern)

        elif choice == '2':
            name = input("Имя: ")
            phone = input("Телефон: ")
            upsert_user(name, phone)

        elif choice == '3':
            names = input("Имена: ").split(',')
            phones = input("Телефоны: ").split(',')

            if len(names) == len(phones):
                bulk_insert(
                    [n.strip() for n in names],
                    [p.strip() for p in phones]
                )
            else:
                print("Количество не совпадает")

        elif choice == '4':
            limit = int(input("Limit: ") or 5)
            offset = int(input("Offset: ") or 0)
            paginated_query(limit, offset)

        elif choice == '5':
            val = input("Имя или телефон: ")
            delete_user(val)

        elif choice == '6':
            print("Пока!")
            break

        else:
            print("Неверный ввод")

if __name__ == '__main__':
    main()