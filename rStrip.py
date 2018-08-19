import re

def rStrip(string, toStrip = None):
    if toStrip == None:
        stripRegex = re.compile(r'^\s+|\s+$')
    else:
        stripRegex = re.compile(r'^[%s]+|[%s]+$' % (re.escape(toStrip), re.escape(toStrip)))
    return stripRegex.sub('', string)

str1 = 'There once was a man from Gilnaes.'
str2 = '     Agent Alex and Agent Sean are really big fans of James Bond.   '
str3 = '     1234898abc923840293abc      '

print(str1.strip('sea.'))
print(rStrip(str1, '.sae'))
print(str2.strip('Agent'))
print(rStrip(str2, 'Agent'))
print(str2.strip())
print(rStrip(str2))
print(str3.strip('abc'))
print(rStrip(str3, 'abc'))
print(str3.strip().strip('abc'))
print(rStrip(str3).strip('abc'))
