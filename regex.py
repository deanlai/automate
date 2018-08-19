import re

phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumberRegex.search('My number is 503-593-0437.')
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)
