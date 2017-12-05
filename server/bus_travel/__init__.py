"""
Root package of this project
****************************

Contains the most important parts.

Modules
=======

.. automodule:: bus_travel.urls
    :members:

.. automodule:: bus_travel.wsgi
    :members:

.. automodule:: bus_travel.settings
    :members:

.. automodule:: bus_travel.helpers
    :members:

Static files
============

All compiled with webpack bundler client code is here. Also icons,
images

Templates
=========

Reallty only one template ``index.html`` - starting point
for SPA application

Management commands
===================

This is usefull django scripts that can be run periodically. For example
to clean up database from inactive records.

1. ``$ django-admin cleanup`` custom command for cleaning up database from
    old discounts that no longer available. I plan to run it once a week
    as this project goes live.
"""
