from setuptools import setup

setup(
    name='intermittent_failure_tracker',
    version='0.1.0',
    author='The Servo Project Developers',
    url='https://github.com/servo/intermittent-failure-tracker/',
    description='A service that tracks instances of intermittent test failures',

    packages=['intermittent_failure_tracker'],
    install_requires=[
        'flask',
        'tinydb',
    ],
    entry_points={
        'console_scripts': [
            'intermittent_failure_tracker=intermittent_failure_tracker.flask_server:main',
        ],
    },
    zip_safe=False,
)
