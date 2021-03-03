from setuptools import setup

setup(
    name='disk_state_check',
    version='0.1',
    description='A disk state checker for write and read',
    author='Fatih Mehmet ARSLAN',
    author_email='contact@fmarslan.com',
    packages=['disk_state_check'],
    install_requires=['prometheus_client', 'tornado'],
    url='http://fmarslan.com'
    entry_points={
        'console_scripts': [
            'disk-state-check= disk_state_check.main:run',
        ],
    },
    keywords='disk-state-check'
)
