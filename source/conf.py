# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '开发日志'
copyright = '2025, Chen-jiangqiao'
author = 'joe'
release = 'v1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'recommonmark',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.imgconverter',
    'sphinx.ext.autosummary',
]

# 设置主题
html_theme = 'sphinx_rtd_theme'
language = 'zh_CN'

# 支持Markdown
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# 图片路径设置
html_static_path = ['_static']
html_js_files = ['svg-interaction.js',]

#响应式SVG的CSS
def setup(app):
    app.add_css_file('custom.css')
