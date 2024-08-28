from datetime import datetime

# pylint: disable=W0622
_logo = ''

project = 'DMARC Report Parser'
copyright = f'{datetime.now().year}, Rath Pascal'
author = 'Rath Pascal'
extensions = ['piccolo_theme', 'myst_parser']
templates_path = ['_templates']
exclude_patterns = []
html_theme = 'piccolo_theme'
html_static_path = ['_static']
html_logo = _logo
html_favicon = _logo
html_css_files = ['css/main.css']
master_doc = 'index'
display_version = True
sticky_navigation = True
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
html_theme_options = {
    'banner_text': '<a href="https://github.com/O-X-L/dmarc-report-parser">Repository on GitHub</a> | '
                   '<a href="https://github.com/O-X-L/dmarc-report-parser/issues/new">Report errors</a>'
}
html_short_title = 'DMARC Report Parser'
