# test open and load of default page
import pytest
import validators

def pageloader():
    page = "http://127.0.0.1:8000/home/"
    return page

def test_load():
    assert validators.url(pageloader())