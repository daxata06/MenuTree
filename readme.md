<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MenuTree - Инструкция по установке</title>
</head>
<body>
    <h1>Инструкция по установке MenuTree</h1>
    
    <h2>1. Клонирование репозитория</h2>
    <pre><code>git clone https://github.com/daxata06/MenuTree.git
cd MenuTree</code></pre>

    <h2>2. Создание виртуального окружения</h2>
    
    <h3>Для Windows:</h3>
    <pre><code>python -m venv venv
venv\Scripts\activate</code></pre>
    
    <h3>Для Linux/macOS:</h3>
    <pre><code>python3 -m venv venv
source venv/bin/activate</code></pre>

    <h2>3. Установка зависимостей</h2>
    <pre><code>pip install -r requirements.txt</code></pre>

    <h2>4. Применение миграций</h2>
    <pre><code>python manage.py migrate</code></pre>

    <h2>5. Загрузка тестовых данных</h2>
    <pre><code>python manage.py initialize</code></pre>

    <h2>6. Запуск сервера</h2>
    <pre><code>python manage.py runserver</code></pre>

    <p>После выполнения этих команд приложение будет доступно по адресу <a href="http://127.0.0.1:8000">http://127.0.0.1:8000</a></p>
</body>
</html>