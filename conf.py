# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import datetime


# -- Project information -----------------------------------------------------

project = 'Python, Weather, and Climate Nerd'
copyright = f'2021-{datetime.datetime.now().year}. Heavily influenced by @andersy005'
author = 'Max Grover'

# The full version, including alpha/beta/rc tags


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_nb',
    'ablog',
    'sphinx_panels',
    'sphinx_comments',
    'sphinx_timeline'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'

# Add some more theme Options
html_theme_options = {
    'github_url': 'https://github.com/mgrover1',
    "twitter_url": "https://twitter.com/mgroverwx",
    'search_bar_text': 'Search this site... ',
    "analytics":{'google_analytics_id':'UA-179020619-2'},
    "logo": {
        "text": project,
    }
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_sidebars = {
    'index': ['hello.html'],
    'about': ['hello.html'],
    'faq': ['hello.html'],
    'communication': ['hello.html'],
    'timeline': ['hello.html'],
    'blog': ['tagcloud.html', 'archives.html'],
    'posts/**': ['postcard.html', 'recentposts.html', 'archives.html'],
}


blog_baseurl = 'https://blog.mgrover.dev'
blog_title = 'Max Grover'
blog_path = 'blog'
fontawesome_included = True
blog_post_pattern = 'posts/*/*'
post_redirect_refresh = 1
post_auto_imagec = 1
post_auto_excerpt = 2

# Panels config
panels_add_bootstrap_css = False

# MyST config
myst_enable_extensions = ['amsmath', 'colon_fence', 'deflist', 'html_image']
myst_url_schemes = ('http', 'https', 'mailto')


# Temporarily stored as off until we fix it
jupyter_execute_notebooks = 'off'


comments_config = {
    'utterances': {'repo': 'mgrover1/mgrover1.github.io', 'optional': 'config', 'label': '💬 comment'},
}


def setup(app):
    app.add_css_file('custom.css')
