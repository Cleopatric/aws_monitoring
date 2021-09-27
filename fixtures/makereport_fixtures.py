import pytest
import os.path
import datetime

FILE_NAME = 'report.log'


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    mode = 'a' if os.path.exists(FILE_NAME) else 'w'
    with open(FILE_NAME, mode) as file:
        date = datetime.datetime.now()
        if rep.when == "call" and rep.failed:
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            error = str(call.excinfo._excinfo[1])
            results = f"| FAIL |{date}|{rep.nodeid}{extra}|\n\n{error}\n\n"
            file.write(results)
        elif rep.when == "call" and rep.nodeid:
            results = f"| PASS |{date}|{rep.nodeid}|\n"
            file.write(results)
