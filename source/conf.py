project = '浦阳檀溪陈氏宗谱'
copyright = '2025, pyzpyjxh@163.com'
author = 'joe'
release = 'v1.0'

extensions = [
    'recommonmark',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.imgconverter',
    'sphinx.ext.autosummary',
    'sphinxcontrib.mermaid',
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
