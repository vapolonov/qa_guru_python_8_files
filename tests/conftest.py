import os
import pytest


@pytest.fixture(scope='session')
def dir_check():
    if not os.path.exists('../resources'):
        os.makedirs('../resources')


@pytest.fixture(scope='session')
def file_remove():
    if not os.path.exists('tmp'):
        os.makedirs('tmp')
    yield
    os.remove('./tmp/docs-pytest-org-en-latest.pdf')
    os.remove('./tmp/file_example_100.xlsx')
    os.remove('./tmp/username.csv')
    os.rmdir('tmp')