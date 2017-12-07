Bus Travel Discounts
********************

Simple SPA app for travellers to keep track of nice deals on bus tickets
in Europe region. It is a `Django <https://www.djangoproject.com/>`_ app, parser and client written in
`Mithril <https://mithril.js.org/>`_.

.. image:: https://badge.waffle.io/Iamthelaw/bus-travel-discounts.svg?columns=all
    :target: https://waffle.io/Iamthelaw/bus-travel-discounts
    :alt: 'Waffle.io - Columns and their card count'

.. image:: https://coveralls.io/repos/github/Iamthelaw/bus-travel-discounts/badge.svg?branch=dev
    :target: https://coveralls.io/github/Iamthelaw/bus-travel-discounts?branch=dev
    :alt: 'Coveralls.io - Code coverage status'

.. image:: https://travis-ci.org/Iamthelaw/bus-travel-discounts.svg?branch=dev
    :target: https://travis-ci.org/Iamthelaw/bus-travel-discounts
    :alt: 'Travis-ci.org - CI status'

.. image:: https://bettercodehub.com/edge/badge/Iamthelaw/bus-travel-discounts?branch=master
    :target: https://bettercodehub.com/results/Iamthelaw/bus-travel-discounts
    :alt: 'BetterCodeHub.com - Code health'

.. inclusion-marker-do-not-remove

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

Set up development version
--------------------------

For development steps are slightly different.

.. code-block:: console

    $ pip install -upgrade pipenv
    $ pipenv install --dev
    $ npm -i
    $ npm start
    $ cp .env.default .env
    $ pipenv run django-admin runserver

Code health
-----------

Linting is done via ``pylint`` package.


Tests
-----

Tests are run with ``pytest`` command.
