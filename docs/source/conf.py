# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'My Portfolio Website'
copyright = '2025, Pannawat Whangvisith'
author = 'Pannawat Whangvisith'
release = '2025'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",                  # ใช้ Markdown ได้
    "sphinx.ext.autodoc",           # ดึง docstring อัตโนมัติ
    "sphinx.ext.napoleon",          # รองรับ Google/NumPy docstring
    "sphinx.ext.viewcode",          # ลิงก์ไปยังโค้ดต้นฉบับ
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


