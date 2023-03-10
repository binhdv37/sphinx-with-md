# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sunteco sphinx'
copyright = '2023, binhdv'
author = 'binhdv'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx.ext.autosectionlabel', # to link to other section in whole project using its title {ref}
    'sphinxcontrib.mermaid' # to create diagram
    ]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

# html_theme_options = {
#     "light_css_variables": {
#         "color-brand-primary": "red",
#         "color-brand-content": "#CC3333",
#         "color-admonition-background": "orange",
#     },
# }

html_theme_options = {
    "sidebar_hide_name": True,
}

# html_theme_options = {
#     "navigation_with_keys": True,
# }

# html_theme_options = {
#     "top_of_page_button": "edit",
# }

html_logo = "_static/logo/logo-dark.png"