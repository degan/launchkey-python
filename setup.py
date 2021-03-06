import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

requires = [
    'pycrypto >= 2.6.1', 'pycrypto < 3.0.0',
    'requests >= 2.5.1', 'requests < 3.0.0',
    'six >= 1.10.0', 'six < 2.0.0',
    'python-dateutil >= 2.4.2', 'python-dateutil < 3.0.0'
    ]

setup(name='launchkey-python',
      version='2.0.1',
      description='LaunchKey Python SDK',
      long_description=README + '\n\n' + CHANGES + '\n',
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='LaunchKey',
      author_email='support@launchkey.com',
      url='https://launchkey.com',
      keywords='launchkey security authentication',
      license='MIT',
      py_modules=[
          'launchkey',
      ],
      zip_safe=False,
      test_suite='tests',
      install_requires=requires,
      tests_require=[
        'mock==1.3.0'
      ],
      )

