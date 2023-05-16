from xml.etree.ElementTree import parse
tree = parse('xmlEx_03.xml')
myroot = tree.getroot()
print(type(myroot))
print('-' * 40)

families = myroot.findall('가족')
print(type(families))
print('-' * 40)

for onefamily in families:
    for onesaram in onefamily:
        if len(onesaram) >= 1:
            print(onesaram[0].text)
        else:
            print(onesaram.attrib['이름'])
    print('-' * 40)
print('finished')