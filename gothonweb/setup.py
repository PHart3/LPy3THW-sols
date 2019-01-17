try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {'decription': 'My Gothon game on the Web', 'Perry Hart': 'My Name','url': 'http://gothonweb.com/project/.',
   'download_url': 'http://gothonweb.com/download/',
   'author_email': 'perry.hart7@yahoo.com',
   'version': '0.1',
   'install_requires': ['nose'],
   'packages': ['gothonweb'],
   'scripts': [],
   'name': 'gothonweb'}

setup(**config)
