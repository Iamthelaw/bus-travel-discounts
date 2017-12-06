Intro
*****

This project is a attempt to code on a pet project for long time. I mean
it is not a "I make this project on a weekend" kind of thing. I thinking
of it as an opportunity to shape habits of long term development.

The main idea behind this project is that often big companies sets different
promotions for different regions. But what if you don't have a strong
plan about you trip destination. You just have a general idea that you need
to ste up a vacation in Europe an it must be cheap as possible.

Installation
============

I recommend yousing marvelous ``pipenv`` package for development. The project
is intentionally desined to work only on **python3** and last versions of
libraries. For so ``pipenv update --dev`` is ideal.

Frontend libraries is installed via ``npm`` package manager.

Recommended steps for installing and running project.

.. code-block:: console

    $ pip install --upgrade pipenv
    $ pipenv install
    $ npm -i --production
    $ npm run build
    $ cp .env.default .env
    $ pipenv run django-admin runserver

Development
===========

For development steps are slightly different.

.. code-block:: console

    $ pip install -upgrade pipenv
    $ pipenv install --dev
    $ npm -i
    $ npm start
    $ cp .env.default .env
    $ pipenv run django-admin runserver

Linting is done via ``pylint`` package.

Tests are run with ``py.test`` command.
