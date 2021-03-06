# This file was automatically generated by Shore. Do not edit manually.
# For more information on Shore see https://pypi.org/project/nr.shore/

import io
import re
import setuptools
import sys

with io.open('src/pydoc_markdown/__init__.py', encoding='utf8') as fp:
  version = re.search(r"__version__\s*=\s*'(.*)'", fp.read()).group(1)

with io.open('README.md', encoding='utf8') as fp:
  long_description = fp.read()

requirements = ['click >=7.0,<8.0.0', 'nr.collections >=0.0.1,<0.1.0', 'nr.databind.core >=0.0.10,<0.1.0', 'nr.databind.json >=0.0.9,<0.1.0', 'six >=1.11.0,<2.0.0', 'PyYAML >=5.3,<6.0.0', 'watchdog >=0.10.2,<1.0.0']

setuptools.setup(
  name = 'pydoc-markdown',
  version = version,
  author = 'Niklas Rosenstein',
  author_email = 'rosensteinniklas@gmail.com',
  description = 'Create Python API documentation in Markdown format.',
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/NiklasRosenstein/pydoc-markdown',
  license = 'MIT',
  packages = setuptools.find_packages('src', ['test', 'test.*', 'docs', 'docs.*']),
  package_dir = {'': 'src'},
  include_package_data = True,
  install_requires = requirements,
  extras_require = {},
  tests_require = [],
  python_requires = None, # TODO: '>=3.6,<4.0.0',
  data_files = [],
  entry_points = {
    'console_scripts': [
      'pydoc-markdown = pydoc_markdown.main:cli',
    ],
    'pydoc_markdown.interfaces.Loader': [
      'python = pydoc_markdown.contrib.loaders.python:PythonLoader',
    ],
    'pydoc_markdown.interfaces.Processor': [
      'crossref = pydoc_markdown.contrib.processors.crossref:CrossrefProcessor',
      'filter = pydoc_markdown.contrib.processors.filter:FilterProcessor',
      'google = pydoc_markdown.contrib.processors.google:GoogleProcessor',
      'pydocmd = pydoc_markdown.contrib.processors.pydocmd:PydocmdProcessor',
      'smart = pydoc_markdown.contrib.processors.smart:SmartProcessor',
      'sphinx = pydoc_markdown.contrib.processors.sphinx:SphinxProcessor',
    ],
    'pydoc_markdown.interfaces.Renderer': [
      'markdown = pydoc_markdown.contrib.renderers.markdown:MarkdownRenderer',
      'mkdocs = pydoc_markdown.contrib.renderers.mkdocs:MkdocsRenderer',
    ]
  },
  cmdclass = {},
  keywords = ['documentation', 'docs', 'generator', 'markdown', 'pydoc'],
  classifiers = ['Development Status :: 3 - Alpha', 'Intended Audience :: Developers', 'Intended Audience :: End Users/Desktop', 'Topic :: Software Development :: Code Generators', 'Topic :: Utilities', 'License :: OSI Approved :: MIT License', 'Programming Language :: Python :: 2', 'Programming Language :: Python :: 2.7', 'Programming Language :: Python :: 3', 'Programming Language :: Python :: 3.3', 'Programming Language :: Python :: 3.4', 'Programming Language :: Python :: 3.5'],
)
