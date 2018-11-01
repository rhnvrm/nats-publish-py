from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='nats_publish',
      version='0.1.1',
      description='Minimal go-nats publisher package',
      url='http://github.com/rhnvrm/nats-publish-py',
      author='Rohan Verma',
      author_email='hello@rohanverma.net',
      license='MIT',
      packages=['nats_publish'],
      zip_safe=True,
      test_suite='nose.collector',
tests_require=['nose'],)