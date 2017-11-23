#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

import django

sys.path.insert(0, os.path.abspath('../../server'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'bus_travel.settings'
django.setup()

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']
autodoc_member_order = 'bysource'
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

# General information about the project.
project = 'Bus Travel'
copyright = '2017, iamthelaw'
author = 'iamthelaw'

# The version info
version = '1.0.0'
release = '1.0.0'

language = None
exclude_patterns = []
pygments_style = 'sphinx'
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------
html_theme = 'alabaster'
html_theme_options = {
    'show_related': True,
}
html_static_path = ['_static']
html_sidebars = {
    '**': [
        'relations.html',
        'globaltoc.html',
        'searchbox.html',
    ]
}

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'BusTraveldoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {}
latex_documents = [
    (master_doc, 'BusTravel.tex', 'Bus Travel Documentation',
     'iamthelaw', 'manual'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'bustravel', 'Bus Travel Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'BusTravel', 'Bus Travel Documentation',
     author, 'BusTravel', 'SPA app for discount deals for travellers.',
     'Travel'),
]



