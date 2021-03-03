from setuptools import setup

setup(
    name='disk-state-check',
    version='0.1',
    description='A disk state checker for write and read',
    author='Fatih Mehmet ARSLAN',
    author_email='contact@fmarslan.com',
    packages=['disk-state-check'],
    install_requires=['prometheus_client', 'tornado'],
    url='http://fmarslan.com'
    scripts=['main'],
    keywords='disk-state-check'
)
