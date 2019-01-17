try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {'decription': 'My Project', 'Perry Hart': 'My Name', 'url': 'URL to get it at.',
   'download_url': 'Where to download it.',
   'author_email': 'perry.hart7@yahoo.com',
   'version': '0.1',
   'install_requires': ['nose'],
   'packages': ['ex47'],
   'scripts': [],
   'name': 'projectname'}

setup(**config)
