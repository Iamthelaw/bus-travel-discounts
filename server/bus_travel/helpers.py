"""
Helpers
=======

Here are definitions that commonly used in two or more django apps
"""
import unicodedata


# This is here because geo_data and service both need it
def serialize(text):
    """
    Cleanup any text (but designed for city names).

    Unfortunately, name of the city can contain special for European
    languages symbols - diacritics, that can interfere with
    geo(de)coding process.

    >>> serialize('The françois')
    'Francois'

    Can be extended with more ``.replace()`` calls if needed.
    Also decided that creating a variable for every
    processing steps will be a waste of resources.

    P.S. I love this clean representation of chained methods.
    Javascript is not ugly, but prejudices are.
    """
    if isinstance(text, str):
        return (
            unicodedata
            .normalize('NFD', text)
            .encode('ascii', 'ignore')
            .decode('utf-8')
            .replace('The ', '')
            .title()
            .strip()
        )
    # Whatever it was, push it back if it wasn't a string
    return text
