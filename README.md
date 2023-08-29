
<h1>Music Catalog API</h1>

<p>Этот проект представляет собой API для управления каталогом музыкальных исполнителей, альбомов и песен с использованием Django Rest Framework.</p>

<h2>Установка</h2>

<ol>
<li>Клонируйте репозиторий:</li>
</ol>

<pre>
<code>git clone git@github.com:EVA666999/test_for_job_2.git</code>
</pre>

<ol start="2">
<li>Перейдите в директорию проекта:</li>
</ol>

<pre>
<code>cd catalog</code>
</pre>

<ol start="3">
<li>Создайте и активируйте виртуальное окружение:</li>
<li>python -m venv venv</li>
<li>source venv/Scripts/activate</li>

</ol>

<ol start="3">
<li>Установите зависимости из файла requirements.txt и выполните миграции</li>
<li>pip install requirenents.txt</li>
<li>python manage.py makemigrations</li>
<li>python manage.py migrate</li>
</ol>

<ol start="4">
<li>запустите сервер</li>
<li>python manage.py runserver</li>
</ol>

<ol start="4">
<li>Ссылка на swagger</li>
<li>http://127.0.0.1:8000/swagger/</li>
</ol>


<ol start="4">
<li>Доступные api</li>
<li>{
    "artists": "http://127.0.0.1:8000/artists/",
    "albums": "http://127.0.0.1:8000/albums/",
    "songs": "http://127.0.0.1:8000/songs/"
}</li>
</ol>