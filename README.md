# win11-morse-code-russian

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows%2011-0078D4?logo=windows&logoColor=white)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e.svg)](LICENSE)
[![Repo](https://img.shields.io/badge/GitHub-eflecto%2Fwin11--morse--code--russian-111827?logo=github)](https://github.com/eflecto/win11-morse-code-russian)

Утилита для Windows 11: перехватывает ввод с клавиатуры и **автоматически заменяет русские буквы на соответствующий код Морзе** (в любом приложении).

## Возможности

- Глобальный перехват клавиатуры (real-time)
- Русский алфавит (А–Я, Ё) + цифры (0–9)
- Пробел → `/` (разделитель слов)
- Горячая клавиша: **Alt + M** (вкл/выкл), **Esc** (выход)

## Установка

> Важно: запускай терминал/IDE **от имени администратора**, иначе глобальный хук клавиатуры может не работать.

```bash
pip install -r requirements.txt
python main.py
```

## Как пользоваться

1. Запусти: `python main.py
2. Нажми **Alt + M** чтобы включить перевод
3. Печатай русские буквы в любом приложении — ввод заменится на Морзянку
4. **Esc** — завершить программу

## Примечания

- Проект использует библиотеку [keyboard](https://pypi.org/project/keyboard/).
- В некоторых окружениях перехват клавиатуры может блокироваться политиками безопасности/антивирусом.

## Лицензия

MIT © 2026 eflecto
