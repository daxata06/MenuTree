<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
</head>
<body>
  <h1>Запуск и установка</h1>

  <h2>📥 Клонирование репозитория</h2>
  <p>Склонируйте проект с GitHub:</p>
  <pre><code>git clone https://github.com/daxata06/MenuTree.git</code></pre>
  <p>Перейдите в директорию проекта:</p>
  <pre><code>cd MenuTree</code></pre>

  <h2>📦 Установка и запуск</h2>

  <h3>1. 🔧 Создание виртуального окружения</h3>
  <p>Откройте терминал и выполните:</p>
  <pre><code>python -m venv venv</code></pre>

  <p><strong>Активация виртуального окружения:</strong></p>
  <ul>
    <li><strong>Windows:</strong> <code>venv\Scripts\activate</code></li>
    <li><strong>macOS/Linux:</strong> <code>source venv/bin/activate</code></li>
  </ul>

  <h3>2. 🧪 Установка зависимостей</h3>
  <p>Установите необходимые зависимости:</p>
  <pre><code>pip install -r requirements.txt</code></pre>

  <h3>3. 🛠 Применение миграций</h3>
  <pre><code>python manage.py migrate</code></pre>

  <h3>4. 🌱 Загрузка тестовых данных</h3>
  <pre><code>python manage.py initialize</code></pre>

  <h2>🚀 Запуск сервера</h2>
  <pre><code>python manage.py runserver</code></pre>
  <p>Приложение будет доступно по адресу: <a href="http://127.0.0.1:8000">http://127.0.0.1:8000</a></p>
</body>
</html>