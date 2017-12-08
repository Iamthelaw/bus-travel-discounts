Bus Travel Discounts
********************

    Simple SPA app for travellers to keep track of nice deals on bus tickets
    in Europe region. It is a `Django <https://github.com/django/django>`_ app, parser and client written in
    `Mithril <https://github.com/MithrilJS/mithril.js>`_.

.. image:: https://readthedocs.org/projects/bus-travel-discounts/badge/?version=latest
    :target: http://bus-travel-discounts.readthedocs.io/?badge=latest
    :alt: Documentation Status

.. image:: https://coveralls.io/repos/github/Iamthelaw/bus-travel-discounts/badge.svg?branch=dev
    :target: https://coveralls.io/github/Iamthelaw/bus-travel-discounts?branch=dev
    :alt: 'Coveralls.io - Code coverage status'

.. image:: https://travis-ci.org/Iamthelaw/bus-travel-discounts.svg?branch=dev
    :target: https://travis-ci.org/Iamthelaw/bus-travel-discounts
    :alt: 'Travis-ci.org - CI status'

.. image:: https://bettercodehub.com/edge/badge/Iamthelaw/bus-travel-discounts?branch=master
    :target: https://bettercodehub.com/results/Iamthelaw/bus-travel-discounts
    :alt: 'BetterCodeHub.com - Code health'

**Documentation**
    available on `readthedocs.io <http://bus-travel-discounts.readthedocs.io>`_

.. inclusion-marker-do-not-remove

Installation
============

I recommend yousing marvelous `pipenv <https://github.com/pypa/pipenv>`_
package for development. The project is intentionally desined to work only on **python3** and last versions of libraries.

Frontend libraries is installed via ``npm`` package manager.

Recommended steps for installing and running project.

.. code-block:: console

    $ make start

After this head to `localhost:8000 <http://127.0.0.1:8000>`_ address in your
browser and all should work as expected.

``make start`` is just a bunch commands as here:

.. code-block:: console

    $ pip install --upgrade pipenv
    $ pipenv install
    $ npm i --production
    $ npm run build
    $ cp .env.default .env
    $ pipenv run django-admin runserver

Development
===========

Set up development version
--------------------------

For development steps are slightly different.

.. code-block:: console

    $ make start-dev

or

.. code-block:: console

    $ pip install --upgrade pipenv
    $ pipenv install --dev
    $ npm i
    $ npm start
    $ cp .env.default .env
    $ pipenv run django-admin runserver

Code health
-----------

Linting is provided by `pylint <https://github.com/PyCQA/pylint>`_
package. Configuration for this tool also can be found in ``setup.cfg``
file in the root folder of this project.

.. code-block:: console

    $ make lint

Tests
-----

Tests are organized in **testing** directory andseparated by app. I prefer `pytest <https://github.com/pytest-dev/pytest>`_, the most pythonic test
runner. Configuration for pytest framework can be found in ``setup.cfg``
file in the root folder of this project.

.. code-block:: console

    $ pytest

This command will run all tests and also provide overall coverage info in
compact and simple manner.


Documentation
-------------

Documentations is organized in ``docs`` folder, in classic rSt format.
To compile documentation run this command.

.. code-block:: console

    $ make docs

Or if you plan to do serious business with docs better run that command.
It will rebuild docs on every change in existing files. This feature is
available with help of `watchdog <https://github.com/gorakhargosh/watchdog>`_
package.

.. code-block:: console

    $ make watch-docs

.. note::

    This command will watch for new changes in doc files and rebuild it,
    but be aware that watchmedo can only look for changes in already
    existing files, not new!

Release History
===============

* 1.0
    * Initial MWP release

Meta
====

Anton Alekseev – @arobotehnik – hi@arobotehnik.me

Distributed under the MIT license. See LICENSE for more information.

https://github.com/iamthelaw/bus-travel-discounts

Contributing
============

* Fork it (https://github.com/iamthelaw/bus-travel-discounts/fork)
* Create your feature branch (git checkout -b feature/fooBar)
* Commit your changes (git commit -am 'Add some fooBar')
* Push to the branch (git push origin feature/fooBar)
* Create a new Pull Request
