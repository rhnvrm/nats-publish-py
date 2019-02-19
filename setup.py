from setuptools import setup
from os import path

def readme():
    this_directory = path.abspath(path.dirname(__file__))
    with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        return f.read()

setup(name='nats_publish',
      version='0.1.3',
      description='Minimal go-nats publisher package',
      url='http://github.com/rhnvrm/nats-publish-py',
      author='Rohan Verma',
      author_email='hello@rohanverma.net',
      license='MIT',
      packages=['nats_publish'],
      zip_safe=True,
      test_suite='nose.collector',
      long_description=readme(),
      long_description_content_type='text/markdown',
      tests_require=['nose'])