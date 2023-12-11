# Проект «Калькулятор стоимости изготовления сетки-рабицы»
# Описание
На этом сайте заказчик (частное лицо) может производить автоматический расчёт стоимости изготовления сетки-рабицы с учётом важных параметров заказа (характеристик требуемой сетки)

Стек: Python3, Django, Django REST framework

Проект доступен по доменному имени https://t701or.pythonanywhere.com/

# Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:alexrashkin/setka_calc.git
cd setka_calc
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас Windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

Автор: 
- Александр Рашкин  - https://github.com/alexrashkin
