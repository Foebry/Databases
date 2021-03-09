from setuptools import setup
setup(
    name = 'Databases',
    version = 1.0,
    packages=['mysql'],
    requirements = [
        'git+https://github.com/Foebry/Logger.git#egg=Logger',
        ],
    url = 'https://github.com/Foebry/Databases',
    author = 'Foebry',
    author_email = 'rain_fabry@hotmail.com',
    description = ''
)
