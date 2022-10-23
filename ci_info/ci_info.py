from typing import NamedTuple

from .env import EnvAny, EnvExists
from .vendors import VENDORS


class CIInfo(NamedTuple):
    name: str
    is_ci: bool
    is_pr: bool | None


def get() -> CIInfo | None:
    for vendor in VENDORS:
        if is_ci_ := bool(vendor.env):
            if (is_pr := vendor.pr) is not None:
                is_pr = bool(vendor.pr)
            return CIInfo(vendor.name, is_ci_, is_pr)
    return None


def is_ci() -> bool:
    if EnvAny(
        EnvExists("CI"),
        EnvExists("CONTINUOUS_INTEGRATION"),
        EnvExists("BUILD_NUMBER"),
        EnvExists("CI_APP_ID"),
        EnvExists("CI_BUILD_ID"),
        EnvExists("CI_BUILD_NUMBER"),
        EnvExists("RUN_ID"),
    ):
        return True

    if vendor := get():
        return vendor.is_ci

    return False
