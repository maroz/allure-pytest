import pytest

from hamcrest import assert_that, contains, all_of, has_entry, has_property, has_properties


@pytest.mark.parametrize('package', ['pytest.allure', 'allure'])
def test_doctests(report_for, package):
    report = report_for("""
    import pytest
    import allure

    def hello_world():
        %s.description('hello world')
    """ % package)

    assert_that(report.findall('.//test-case'), contains(
        has_property('description', 'test_doctests.hello_world')))
