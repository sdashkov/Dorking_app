import os

# Установим язык и тему по умолчанию
def set_default_language():
    with open('logs/language.txt', 'w') as file:
        file.write("English")

def get_language():
    with open('logs/language.txt', 'r') as file:
        return file.read().strip()

def get_theme():
    with open('logs/theme.txt', 'r') as file:
        return file.read().strip()

def change_theme():
    current_theme = get_theme()
    new_theme = 'light' if current_theme == 'dark' else 'dark'
    with open('logs/theme.txt', 'w') as file:
        file.write(new_theme)
    print(f"Theme changed to {new_theme}")

def generate_request():
    request = ''
    tag = input("Enter tag (optional): ")
    phrase = input("Enter phrase (optional): ")
    site = input("Enter site (optional): ")
    link = input("Enter link (optional): ")
    inurl = input("Enter inurl (optional): ")
    cache = input("Enter cache (optional): ")
    related = input("Enter related (optional): ")
    filetype = input("Enter filetype (optional): ")

    if tag:
        request += f"@{tag} "
    if phrase:
        request += f'"{phrase}" '
    if site:
        request += f'site:{site} '
    if link:
        request += f'link:{link} '
    if inurl:
        request += f'inurl:{inurl} '
    if cache:
        request += f'cache:{cache} '
    if related:
        request += f'related:{related} '
    if filetype:
        request += f'filetype:{filetype} '

    print(f"Generated request: {request}")

    # Логируем запрос (в файл)
    with open('logs/recent.csv', 'a', newline='') as f:
        description = input("Enter request description (optional): ")
        f.write(f"{request};{description}\n")

def main():
    # Убедимся, что файлы конфигурации существуют
    if not os.path.exists('logs'):
        os.makedirs('logs')
    if not os.path.exists('logs/language.txt'):
        set_default_language()
    if not os.path.exists('logs/theme.txt'):
        with open('logs/theme.txt', 'w') as file:
            file.write('light')

    print(f"Current theme: {get_theme()}")
    print(f"Current language: {get_language()}")

    while True:
        print("\n1. Generate request")
        print("2. Change theme")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            generate_request()
        elif choice == '2':
            change_theme()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
