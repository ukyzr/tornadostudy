# -*- coding: utf-8 -*-
# __file__  : test_example.py
# __time__  : 2020/7/3 6:42 PM

# content of test_example.py
import pytest


@pytest.fixture
def error_fixture():
    assert 0


def test_ok():
    print("ok")


def test_fail():
    assert 0


def test_error(error_fixture):
    pass


def test_skip():
    pytest.skip("skipping this test")


def test_xfail():
    pytest.xfail("xfailing this test")


@pytest.mark.xfail(reason="always xfail")
def test_xpass():
    pass
