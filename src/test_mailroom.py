"""Test functions for functions in mailroom.py."""
import pytest


Test = [("Chai", 50, "Chai thank you for your kind donation of $50"),
        ("Bob", 90, "Bob thank you for your kind donation of $90"),
        ("Rob", 60, "Rob thank you for your kind donation of $60"),
        ("Chad", 90, "Chad thank you for your kind donation of $90")]

TEST2 = [('222'), ('2456'), ('555'), ('10'), ('20'), ('40'), ('100')]
TEST3 = [('10'), ('20'), ('40'), ('100'), ('50'), ('1000'), ('76'), ('1400')]


@pytest.mark.parametrize('parm,parm2,result', Test)
def test_send_thank_you(parm, parm2, result):
    """Testsing send tahbk_you function"""
    from mailroom import send_thank_you
    assert send_thank_you(parm, parm2) == result


def test_donor_list():
    """Testing the Donor List"""
    from mailroom import donor_list
    assert donor_list()


@pytest.mark.parametrize('check', TEST2)
def test_avg_donation_in_create_report(check):
    """Test if the average  amount in create_report()."""
    from mailroom import create_report
    out = create_report()
    assert out.find(check)


@pytest.mark.parametrize('donation', TEST3)
def test_donation_amounts_in_create_report(donation):
    """Test if donation is  in create_report()."""
    from mailroom import create_report
    out = create_report()
    assert out.find(donation)
