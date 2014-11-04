from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='wi-sqlalchemy-formatter',
    version='0.2b',

    description='Pygments-powered logging formatter for SQLAlchemy',
    url='http://gitlab.qa.devwebinterpret.com/tools/wi-sqlalchemy-formatter',
    author='Bartek Rychlicki <bartek.r@webinterpret.com>',
    author_email='funky_chicken@webinterpret.com',
    # license='unknown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Dev Tools',
        'License :: OSI Approved :: Unknwon',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='development tools',
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        # no versions specified as projects this will be sed for ar diverse
        # but fear not, this is a debug library, the worst that could happen
        # is console logging error, then change back to normal handler.
        'sqlparse',
        'pygments',
        # 'sqlalchemy',  # disabled until further solution found
        # 'mysql-python',

    ],
)
