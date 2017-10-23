"""Mailroom Project"""



def take_input():
    user_input = input('Enter ty for Thank You OR report for report: ')
    if user_input == 'ty':
        return create_thankyou()
    if user_input == report:
        return create_report()


def create_thankyou():
    donor_name = input('Enter Full Name (First, Last): ')
    return donor_name


def create_report():
    print('Report')


take_input()
create_thankyou()
