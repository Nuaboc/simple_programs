#!/usr/bin/env python3

# THIS PROGRAM IS ABOUT SAVING ALL YOUR COMPLICATED PASSWORDS TO A SAFE BOX
# AND ONLY USE A SINGLE PASSWORD (KEY) TO UNLOCK IT, THEN COPY AND PASTE
# THE SPECIFIC PASSWORD TO THE SPECIFIC ACCOUNT.

import sys, pyperclip


passwords = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '123456'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
