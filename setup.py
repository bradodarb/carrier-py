from os import path

from setuptools import setup, find_packages

# To use a consistent encoding
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.rst')) as f:
    LONG_DESCRIPTION = f.read()

# Get the version number from the version.txt
with open(path.join(HERE, 'version.txt')) as f:
    VERSION = f.read()

with open(path.join(HERE, 'platform_serverless_test_lib/requirements.txt')) as f:
    requires = f.read().splitlines()

setup(name='platform-serverless-test-lib',
      version=VERSION,
      description='Common Utilities for Local and Remote testing of Serverless Developments',
      long_description=LONG_DESCRIPTION,
      classifiers=[
          'Programming Language :: Python :: 3'
      ],
      keywords='Lambda, Serverless, AWS, Dynamo, Integration Tests',
      author='Platform Serverless Team',
      author_email="dev@teamplatform.com",
      packages=find_packages(exclude=['test*']),
      include_package_data=True,
      package_dir={'.': ''},
      install_requires=requires,
      zip_safe=False)
