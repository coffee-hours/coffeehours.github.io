# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'Coffee Hours'
copyright = '2022'
author = 'Coffee Hours'

# -- General configuration ---------------------------------------------------

extensions = [
    "myst_nb",
    "ablog",
]

templates_path = ['_templates']

exclude_patterns = ['_build', "README.md"]

# -- Options for HTML output -------------------------------------------------

html_theme = 'pydata_sphinx_theme'

html_theme_options = {
  "github_url": "https://github.com/coffee-hours/coffeehours.github.io",
  "search_bar_text": "Search this site...",
  "navbar_end": ["search-field.html", "navbar-icon-links"],
}

html_favicon = "_static/favicon.ico"
html_static_path = ['_static']
html_sidebars = {
    "posts/**": ['postcard.html', 'recentposts.html', 'archives.html'],
    "blog": ['tagcloud.html', 'archives.html'],
    "blog/**": ['postcard.html', 'recentposts.html', 'archives.html']
}
blog_baseurl = "https://coffeehours.net"
blog_title = "Coffee Hours"
blog_path = "blog"
fontawesome_included = True
blog_post_pattern = "posts/*/*"
post_redirect_refresh = 1
post_auto_image = 1
post_auto_excerpt = 2

myst_enable_extensions = [
    "deflist",
    "colon_fence",
]

jupyter_execute_notebooks = "off"

def setup(app):
    app.add_css_file("custom.css")
