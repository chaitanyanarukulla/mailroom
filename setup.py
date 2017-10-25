dependences = ['ipython']
extra_packages = {
    'testing': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']
}


setup(
    name='Mailroom Madness',
    description='401 Python project',
    version='0.1',
    authors='Chaitanya, Marco',
    author_email='chaitanyanarukulla@gmail.com',
    license='MIT',
    py_modules=['mailroom', 'test_mailroom'],
    package_dir={'': 'src'},
    install_requires=dependences,
    extras_require=extra_packages,
    entry_points={
        'console_scripts': [
            'mailroom=mailroom:main'
        ]
    }
)