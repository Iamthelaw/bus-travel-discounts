"""
Helpers
=======
"""


def sanitize(text):
    """
    Sanitizes any text.

    Example usage

    .. doctest::

        >>> sanitize('Äêrtom')
        Aertom
    """
    cleaned_text = text
    #: Parts of words
    garbage = ('The ', )
    for item in garbage:
        cleaned_text = cleaned_text.replace(item, '')
    #: Europe language characters
    diacritics = {
        'A': 'ÄÀÁÂÃÅǍĄĂÆĀ',
        'a': 'äàáâãåǎąăæā',
        'C': 'ÇĆĈČ',
        'c': 'çćĉč',
        'D': 'ĎĐ',
        'd': 'đďð',
        'E': 'ÈÉÊËĚĘĖĒ',
        'e': 'èéêëěęėē',
        'G': 'ĜĝĢģĞğ',
        'g': 'ĜĝĢģĞğ',
        'H': 'Ĥ',
        'h': 'ĥ',
        'I': 'ÌÍÎÏĪĮ',
        'i': 'ìíîïıīį',
        'J': 'Ĵ',
        'j': 'ĵ',
        'K': 'Ķ',
        'k': 'ķ',
        'L': 'ĹĻŁĽ',
        'l': 'ĺļłľ',
        'N': 'ÑŃŇŅ',
        'n': 'ñńňņ',
        'O': 'ÖÒÓÔÕŐØŒ',
        'o': 'öòóôõőøœ',
        'R': 'ŔŘ',
        'r': 'ŕř',
        'S': 'ẞŚŜŞŠȘ',
        's': 'ßśŝşšș',
        'T': 'ŤŢÞȚ',
        't': 'ťţþț',
        'U': 'ÜÙÚÛŰŨŲŮŪ',
        'u': 'üùúûűũųůū',
        'W': 'Ŵ',
        'w': 'ŵ',
        'Y': 'ÝŸŶ',
        'y': 'ýÿŷ',
        'Z': 'ŹŽŻ',
        'z': 'źžż'
    }
    # Creates mapping like (..('ź', 'z'), ('ž', 'z'))
    mapping = (
        (value, key) for key, values in diacritics.items() for value in values
    )
    for key, value in mapping:
        if key in cleaned_text:
            cleaned_text = cleaned_text.replace(key, value)
    # Final touch, strip trailing spaces
    return cleaned_text.strip()
