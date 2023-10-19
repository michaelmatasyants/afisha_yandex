# Afisha_yandex - Study Project

- [Demo version of the site](https://mikayel.pythonanywhere.com/)
- [Administrator panel](https://mikayel.pythonanywhere.com/admin)
- [Project on GitHub](https://github.com/michaelmatasyants/afisha_yandex)

 # Where to go - Moscow through Artyom's eyes

A website about the most interesting places in Moscow.

![Screenshot of the main page]()


## How to add a new location

- Open the [admin panel](https://mikayel.pythonanywhere.com/admin)
- In the left column, select `Места`
- You can add a new location and edit existing locations

## How to run

Python3 should already be installed.

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

* Do a database migration
    ```
    python3 manage.py migrate
    ```

* Run the server using `manage.py`

    ```
    python3 manage.py runserver
    ```

* In your browser, open the page with the data of visitors to the repository at the following address: `127.0.0.1:8000`

## Test data

Test data can be obtained on the page [GitHub](https://github.com/devmanorg/where-to-go-places).

## Project Objectives

The code is written for educational purposes