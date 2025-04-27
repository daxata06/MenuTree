<div>
    <h2>Установка и запуск</h2>
    
    <h3>1. Клонировать репозиторий</h3>
    <pre><code>git clone https://github.com/daxata06/MenuTree.git
cd MenuTree</code></pre>

    <h3>2. Создать и активировать виртуальное окружение</h3>
    <p><strong>Для Windows:</strong></p>
    <pre><code>python -m venv venv
venv\Scripts\activate</code></pre>

    <p><strong>Для Linux/macOS:</strong></p>
    <pre><code>python3 -m venv venv
source venv/bin/activate</code></pre>

    <h3>3. Установить зависимости</h3>
    <pre><code>pip install -r requirements.txt</code></pre>

    <h3>4. Выполнить миграции</h3>
    <pre><code>python manage.py migrate</code></pre>

    <h3>5. Загрузить тестовые данные</h3>
    <pre><code>python manage.py initialize</code></pre>

    <h3>6. Запустить сервер</h3>
    <pre><code>python manage.py runserver</code></pre>
</div>