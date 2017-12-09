"""
Money
*****

This Django app is supposed to hold data models for currency and
management command for getting exchange information from exteernal service.

For the time being I plan to use fixer.io, but it will be only in future
version, not in v1.0. To note abuse this service management command will be
storing exchange rates in database and operate during the day with it.

For today I plan to support only 3 currencies - USD, EUR, RUB. But it
can be changed in future releases, so I must make this part extendable
but constrains must exists.

.. automodule:: money.models
    :members:
"""
