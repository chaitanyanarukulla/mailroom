from setuptools import setup


setup(
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'pytest-watch', 'tox'],
        'development': ['ipython']
    },
    # ...
    entry_points={
        'console_scripts': [
            "mailroom = mailroom:main"
        ]
    }
)