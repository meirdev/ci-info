import os
from unittest import mock

from ci_info import VendorName, get, is_ci


@mock.patch.dict(os.environ, {
    "CIRCLECI": "",
    "CIRCLE_PULL_REQUEST": "1",
})
def test_get():
    ci_info = get()

    assert ci_info.name == VendorName.CIRCLE
    assert ci_info.is_ci
    assert ci_info.is_pr


@mock.patch.dict(os.environ, {"HUDSON_URL": ""})
def test_get_pr_is_none():
    ci_info = get()

    assert ci_info.is_pr is None


@mock.patch.dict(os.environ, {}, clear=True)
def test_get_is_none():
    ci_info = get()

    assert ci_info is None


@mock.patch.dict(os.environ, {"CIRCLECI": ""})
def test_is_ci():
    assert is_ci()


@mock.patch.dict(os.environ, {"CI_APP_ID": ""}, clear=True)
def test_is_ci_common():
    assert is_ci()


@mock.patch.dict(os.environ, {}, clear=True)
def test_is_ci_false():
    assert not is_ci()
