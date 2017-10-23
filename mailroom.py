"""Mailroom Project"""

donor_data = {'AppaRao': '33.00', 'Angel': '40.00', 'Winafred': '50.00'}

def take_input():
    user_input = input('Enter ty for Thank You OR report for report: ')
    if user_input == 'ty':
        return create_thankyou()
    if user_input == report:
        return create_report()


def create_thank_you():
    donor_name = input('Enter Full Name (First, Last): ')
    if donor_name == 'list':
        return donor_list()
    if donor_name in donor_data:
        return send_thank_you()
    else:
        create_new_donor()


def send_thank_you():


def create_new_donor():
    new_name = input('Enter new Full name')
    donations = input('Enter Amount to donate')
    donor_data[new_name] = donations


def donor_list():
    # return keys of donor_data


def create_report():
    print('Report')


take_input()

