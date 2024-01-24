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
import pathlib
from textwrap import dedent
import yaml
from sphinx.application import Sphinx
from sphinx.util import logging

LOGGER = logging.getLogger('conf')


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
    'sphinx_design',
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
    'teaching': ['hello.html'],
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

def build_teaching_gallery(app: Sphinx):
    LOGGER.info('Building teaching gallery')
    path = pathlib.Path(app.srcdir) / 'config_data/teaching.yaml'
    teaching = yaml.safe_load(path.read_text())
    teaching = sorted(teaching, key=lambda item: item['date'], reverse=True)
    grid_items = []
    for item in teaching:
        if not item.get('video'):
            item['video'] = '...'

        repo_text = ''
        star_text = ''

        if item['repository']:
            repo_text = f'{{bdg-link-secondary}}`repo <{item["repository"]}>`'

            try:
                url = urlparse(item['repository'])
                if url.netloc == 'github.com':
                    _, org, repo = url.path.rstrip('/').split('/')
                    link = f'https://img.shields.io/github/stars/{org}/{repo}?style=social'
                    star_text = f"[![GitHub Repo stars]({link})]({item['repository']})"
            except Exception:
                pass

        grid_items.append(
            f"""\
        `````{{grid-item-card}} {" ".join(item["name"].split())}
        :text-align: center
        {item["video"]}
        +++
        ````{{grid}} 2 2 2 2
        :margin: 0 0 0 0
        :padding: 0 0 0 0
        :gutter: 1
        ```{{grid-item}}
        :child-direction: row
        :child-align: start
        :class: sd-fs-5
        {repo_text}
        ```
        ```{{grid-item}}
        :child-direction: row
        :child-align: end
        {star_text}
        ```
        ````
        `````
        """
        )
    grid_items = '\n'.join(grid_items)

    panels = f"""``````{{grid}} 2
:class-container: full-width
{dedent(grid_items)}
``````
    """
    (pathlib.Path(app.srcdir) / 'teaching_gallery.md').write_text(panels)


def build_talks_gallery(app: Sphinx):
    LOGGER.info('Building talks gallery')
    path = pathlib.Path(app.srcdir) / 'config_data/talks.yaml'
    talks = yaml.safe_load(path.read_text())
    talks = sorted(talks, key=lambda item: item['conference']['date'], reverse=True)
    LOGGER.info(f'Found {len(talks)} talks')
    content = [
        """\
```{panels}
:card: text-center
"""
    ]
    for index, item in enumerate(talks):
        content.append(
            f"""\
[{item['title']}]({item['slides']})
^^^
{item['video']}
+++
{item['conference']['name']} | {item['conference']['location']} | {item['conference']['date']}
"""
        )

        if index < len(talks) - 1:
            content.append(
                """\
---
"""
            )

    content.append(
        """\
```"""
    )

    content = dedent('\n'.join(content))
    out_path = pathlib.Path(app.srcdir) / 'talks_gallery.md'
    out_path.write_text(content)


def setup(app):
    app.add_css_file('custom.css')
    app.connect('builder-inited', build_talks_gallery)
    app.connect('builder-inited', build_teaching_gallery)
