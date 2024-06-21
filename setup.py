from setuptools import setup, find_packages

setup(
    name='prediction_model',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'rasa',
        'rasa-sdk',
        'requests',
        'Gunicorn',
    ],
)
