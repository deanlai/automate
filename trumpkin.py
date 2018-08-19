#! /usr/bin/env python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

trumpRegex = re.compile(r'(Donald\s)?Trump')
ogText = str(pyperclip.paste())
newText = trumpRegex.sub('Lil\' Trumpkin', ogText)
pyperclip.copy(newText)
