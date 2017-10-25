"""Test functions for functions in mailroom.py."""
import pytest
est = [('chai', 50), '{} thank you for your kind donation of ${}'.format(chai, 50)]


@pytest.mark.parametrize('parm,result', Test)
def test_send_thankyou(parm, result):
    """."""
    from mailroom import send_thankyou
    assert send_thankyou(parm) == result


Test_2 = [([chai,bob,mob,taj],chai,bob,mob,taj)]


@pytest.mark.parametrize('parm,result', Test_2)
def test_donor_list(parm):
    """."""
    from mailroom import donor_list
    assert donor_list(parm) == result


trst_3 = [('chai', 50), '{} thank you for your kind donation of ${}'.format(chai, 50)]

@pytest.mark.parametrize('parm,result', Test_3)
def test_create_new_donor(parm):
    """."""
    from mailroom import create_new_donor
    assert create_new_donor(parm) == result


DONORS_2 = {
    'Chai': [300, 10, 15],
    'Bob': [10, 200, 50],
    'POP': [1000]}

Table = [
    'Chai            3         108.33   ',
    'Bob             3         86.67    ',
    'POP             1         1000.00   '
]


@pytest.mark.parametrize('string', Table)
def test_create_report(string):
    """Test to determine if the correct donor and donation."""
    from mailroom import create_report
    assert string in create_report(DONORS_2)
