import keyboard

# Русский алфавит (А–Я, Ё) + цифры (0–9) + пробел
# Пробел преобразуется в '/' как разделитель слов
MORSE_DICT = {
    'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..',
    'Е': '.', 'Ё': '.', 'Ж': '...-', 'З': '--..', 'И': '..',
    'Й': '.---', 'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.',
    'О': '---', 'П': '.--.', 'Р': '.-.', 'С': '...', 'Т': '-',
    'У': '..-', 'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.',
    'Ш': '----', 'Щ': '--.-', 'Ъ': '--.--', 'Ы': '-.--', 'Ь': '-..-',
    'Э': '..-..', 'Ю': '..--', 'Я': '.-.-',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/'
}

enabled = True


def on_press(event):
    global enabled

    # Alt+M — переключить режим
    if event.name == 'm' and keyboard.is_pressed('alt'):
        enabled = not enabled
        state = "ON" if enabled else "OFF"
        print(f"[win11-morse-code-russian] state: {state}")
        return

    if not enabled:
        return

    # event.name обычно строка (например 'a', 'space', '1').
    # Для русских букв keyboard может отдавать уже символ — зависит от раскладки/окружения.
    name = event.name

    # Нормализуем пробел
    if name == 'space':
        char = ' '
    else:
        # Берём первый символ, приводим к верхнему регистру
        char = str(name).upper()[:1]

    if char in MORSE_DICT:
        # Стираем введённый символ и печатаем морзянку
        keyboard.press_and_release('backspace')
        keyboard.write(MORSE_DICT[char] + ' ')


if __name__ == '__main__':
    print("win11-morse-code-russian started")
    print("Alt+M: toggle on/off")
    print("Esc: exit")

    keyboard.on_press(on_press)
    keyboard.wait('esc')
