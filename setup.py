from setuptools import setup

def read_requirements():
    with open("requirements.txt", "r") as req:
        content = req.read()
        requirements = content.split('\n')

    return requirements

setup(
    name = 'trelloboard_cli',
    version = '0.1.0',
    packages = ['trello_cli'],
    author = 'Deborah Oni',
    install_requires = read_requirements(),
    entry_points = {
        'console_scripts': [
            'trello_cli = trello_cli.trello:cli'
        ]
    }
)