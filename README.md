# Afisha_yandex - Study Project

- [Demo version of the site](https://mikayel.pythonanywhere.com/)
- [Administrator panel](https://mikayel.pythonanywhere.com/admin)
- [Project on GitHub](https://github.com/michaelmatasyants/afisha_yandex)

# Where to go - Moscow through Artyom's eyes

A website about the most interesting places in Moscow.

![Screenshot of the main page](/assets/screenshot.png)


## How to add a new location

- Open the [admin panel](https://mikayel.pythonanywhere.com/admin)
- In the left column, select `Места`
- You can add a new location and edit existing locations

## How to run

Python3 should already be installed. Ideally version `3.11`.<br>

Check the python version:
```
python3 --version
```

To upgrade python to verion `3.11`:
```
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install python3.11
```

Then use `pip` (or `pip3` if there is a conflict with Python2) to install the dependencies:
```
pip install -r requirements.txt
```

* Clone the code from [GitHub](https://github.com/michaelmatasyants/afisha_yandex)

    Before launching, environment variables must be set up. The repository contains     a file `.env.example` with the following contents:

    ```
    SECRET_KEY=<put here your secret key>
    ALLOWED_HOSTS=localhost,127.0.0.1,<add here your website address>
    DEBUG=<set False for development and True for production>
    ```

* Rename it to `.env` and put your site settings into it

    ```
    SECRET_KEY=<secret key used to encrypt your site's user passwords>
    ALLOWED_HOSTS=<[List of strings representing hostnames/domains that this  Django site can serve.]>
    DEBUG=<Set to True to see debugging information when developing the site. False is the default value>
    ```

* Put all static files (js, css, images, etc.) in assets and after to collect all static files in static type:
    ```
    python3 manage.py collectstatic
    ```

* Do a database migration
    ```
    python3 manage.py makemigrations places
    python3 manage.py migrate
    ```

* Run the server using `manage.py`
    ```
    python3 manage.py runserver
    ```

* In your browser, open the page with the data of visitors to the repository at the following address: `127.0.0.1:8000`

## Test data

Load test data to see how it works. Test data can be obtained on the page [GitHub](https://github.com/devmanorg/where-to-go-places).

To do this, run the command:
```
python manage.py load_place http://example.com/sample_place_file.json
```
**Note that the link leads to files directly from Github (raw.github).**

Also you can pass multiple addresses at once.

A [sample of a json file](sample_place_file.json) can be found in the project main directory.<br> It should be in the following format:


```
{
    "title": "Антикафе Bizone",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1f09226ae0edf23d20708b4fcc498ffd.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6e1c15fd7723e04e73985486c441e061.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/be067a44fb19342c562e9ffd815c4215.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/f6148bf3acf5328347f2762a1a674620.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/b896253e3b4f092cff47a02885450b5c.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/605da4a5bc8fd9a748526bef3b02120f.jpg"
    ],
    "description_short": "Настольные и компьютерные игры, виртуальная реальность и насыщенная программа мероприятий — новое антикафе Bizone предлагает два уровня удовольствий для вашего уединённого отдыха или радостных встреч с родными, друзьями, коллегами.",
    "description_long": "<p>Рядом со станцией метро «Войковская» открылось антикафе Bizone, в котором создание качественного отдыха стало делом жизни для всей команды. Создатели разделили пространство на две зоны, одна из которых доступна для всех посетителей, вторая — только для совершеннолетних гостей.</p><p>В Bizone вы платите исключительно за время посещения. В стоимость уже включены напитки, сладкие угощения, библиотека комиксов, большая коллекция популярных настольных и видеоигр. Также вы можете арендовать ВИП-зал для большой компании и погрузиться в мир виртуальной реальности с помощью специальных очков от топового производителя.</p><p>В течение недели организаторы проводят разнообразные встречи для меломанов и киноманов. Также можно присоединиться к английскому разговорному клубу или посетить образовательные лекции и мастер-классы. Летом организаторы запускают марафон настольных игр. Каждый день единомышленники собираются, чтобы порубиться в «Мафию», «Имаджинариум», Codenames, «Манчкин», Ticket to ride, «БЭНГ!» или «Колонизаторов». Точное расписание игр ищите в группе антикафе <a class=\"external-link\" href=\"https://vk.com/anticafebizone\" target=\"_blank\">«ВКонтакте»</a>.</p><p>Узнать больше об антикафе Bizone и забронировать стол вы можете <a class=\"external-link\" href=\"http://vbizone.ru/\" target=\"_blank\">на сайте</a> и <a class=\"external-link\" href=\"https://www.instagram.com/anticafe.bi.zone/\" target=\"_blank\">в Instagram</a>.</p>",
    "coordinates": {
        "lng": "37.50169",
        "lat": "55.816591"
    }
}
```

## Project Objectives

The code is written for educational purposes
