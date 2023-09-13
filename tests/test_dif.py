import allure
from allure_commons.types import Severity


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "ebezgubenko")
@allure.feature("Telegram-bot")
def test_pass():
    pass


def test_pass1():
    pass


def test_pass2():
    pass


def test_pass3():
    pass


def test_pass4():
    pass


def test_fail():
    assert False


def test_fail1():
    assert False


def test_fail2():
    assert False


def test_fail3():
    assert False


def test_fail4():
    assert False
