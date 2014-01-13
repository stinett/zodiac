import os

from setuptools import setup, find_packages
from setuptools import Command
here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import pytest
        errno = pytest.main("")
        raise SystemExit(errno)

requires = ['pyramid==1.4', 'jinja2']
test_requires = requires + ["pytest"]
setup(name='zodiac',
      version='0.0',
      description='zodiac',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=test_requires,
      test_suite="zodiac",
      entry_points = """\
      """,
      paster_plugins=['pyramid'],
      cmdclass = {'test': PyTest},
      )

