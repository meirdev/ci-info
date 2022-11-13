import os
from unittest import mock

from ci_info import env


@mock.patch.dict(os.environ, {"CI_INFO_TEST": ""})
def test_env_exists():
    assert env.EnvExists("CI_INFO_TEST")


@mock.patch.dict(os.environ, {}, clear=True)
def test_env_not_exists():
    assert env.EnvNotExists("CI_INFO_TEST")


@mock.patch.dict(os.environ, {"CI_INFO_TEST": "true"})
def test_env_equal():
    assert env.EnvEqual("CI_INFO_TEST", "true")
    assert not env.EnvEqual("CI_INFO_TEST", "yes")


@mock.patch.dict(os.environ, {"CI_INFO_TEST": "false"})
def test_env_not_equal():
    assert not env.EnvNotEqual("CI_INFO_TEST", "false")
    assert env.EnvNotEqual("CI_INFO_TEST", "no")


@mock.patch.dict(os.environ, {"CI_INFO_TEST": "one two three"})
def test_env_includes():
    assert env.EnvIncludes("CI_INFO_TEST", "one")
    assert not env.EnvIncludes("CI_INFO_TEST", "four")


@mock.patch.dict(os.environ, {
    "CI_INFO_TEST1": "true",
    "CI_INFO_TEST2": "no",
    "CI_INFO_TEST3": "",
})
def test_env_all():
    assert env.EnvAll(
        env.EnvEqual("CI_INFO_TEST1", "true"),
        env.EnvNotEqual("CI_INFO_TEST2", "false"),
        env.EnvExists("CI_INFO_TEST3"),
    )

    assert not env.EnvAll(
        env.EnvExists("CI_INFO_TEST3"),
        env.EnvExists("CI_INFO_TEST4"),
    )


@mock.patch.dict(os.environ, {
    "CI_INFO_TEST1": "false",
    "CI_INFO_TEST2": "no",
    "CI_INFO_TEST3": "",
})
def test_env_any():
    assert env.EnvAny(
        env.EnvEqual("CI_INFO_TEST1", "true"),
        env.EnvNotEqual("CI_INFO_TEST2", "false"),
        env.EnvExists("CI_INFO_TEST3"),
    )

    assert not env.EnvAny(
        env.EnvEqual("CI_INFO_TEST1", "true"),
        env.EnvExists("CI_INFO_TEST4"),
    )
