1.Чтобы установить проект к себе на локальный хостинг нужно:
    1.Клонируйте  проект с репозитория
      Ссылка на репозиторий: https://github.com/AnastasiaAlekseeva204/WEBproject.git
      git clone <адрес репозитория>

    2.Создайте виртуальную среду (если она не создана)
      -Перейдите в директорию проекта:
      cd <имя проекта>
      -Создайте виртуальную среду с помощью команды:
      python -m venv myenv
      -Активируем виртуальную среду:
      source myenv/bin/activate

    3.Установка зависимости
      установить необходимые библиоткеки из файла requirements.txt
      pip install -r  requirements.txt

    4.Конфигурирование базы данных
      Настройте файл settings.py (если это необходимо)
    
    5.Запуск проекта
      Перейдите в директорию проекта 
      Запустите с помощью команды:
      python manage.py runserver

    

2. Функционал сайта (поиск, сортировка, новинки, популярные книги):

Сайт включает в себя поиск, который работает засчет forms.html, где используется get параметр
Сортировка используется с помощью sort=asc(дешевле) and sort=desc(дороже)
Новинки, появляются засчет добавления галочки в базе данных isnew=Yes,No
Популярные книги, появляются с помощью счетчика просмотра добавленый в базу данных

3. Описание моделей, что в них входит:

Category
id
parent
title
content
enabled

Post
id
title
id_rubric
text
author
create_data

Author
title
image

Book
id
category
title
id_author
image
price
content
data_pub
enabled
reiting
count_view
isnew

New
id
name
image
mini_content
content
cur_date
enabled
