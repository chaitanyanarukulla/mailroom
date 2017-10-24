"""Mailroom Project"""
import sys
donor_data = {'AppaRao': [34,100,75], 'Angel':[35, 80, 90,76], 'Winafred':[56,85,90]}

def take_input():
    user_input = input('Enter ty for Thank You OR report for report: ')
    if user_input == 'ty':
        create_thank_you()
    elif user_input == 'report':
         create_report()
    elif user_input == 'Q':
        sys.exit()
    else:
        print('Please type a valid Input')
        take_input()


def create_thank_you():
    donor_name = input('Enter Full Name (First, Last): ')
    if donor_name == 'list':
        return donor_list()
    elif donor_name in donor_data:
        donation = input('Enter Amount to donate: ')
        donor_data[donor_name] = donation
        return send_thank_you(donor_name,donation)
    else:
        create_new_donor()


def send_thank_you(donor_name,donation):
   print('Thank You')
   return('{} thank you for your kind donation of ${}'.format(donor_name,donation))


def create_new_donor():
    new_name = input('Enter New Full name: ')
    donation = input('Enter Amount to donate: ')
    if donation.isalpha():
        print('\nPlease enter a number.\n')
    else:
        donor_data[new_name] = donation
        send_thank_you(new_name,donation)


def donor_list():
    for item in donor_data.keys():
        print(item)
        return item


def create_report():
    from tabulate import tabulate
    all_doner_list = []
    for key in donor_data:
        total = sum(donor_data[key])
        times_donated = len(donor_data[key])
        avg = total/times_donated
        all_doner_list.append([key, total, times_donated,avg])
        print(tabulate(all_doner_list, headers =['Name', 'Donated', '#Times', 'Avg Donation']))
        return(tabulate(all_doner_list, headers =['Name', 'Donated', '#Times', 'Avg Donation']))


take_input()