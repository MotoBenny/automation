import re


phone_reg = r'\b\d{3}\D?\d{3}\D?\d{4}'
sub_reg = r"[.)]"
#
# email_reg
#
#
# match_obj = re.match(phone_reg, POTENTIAL CONTACTS DOC)
document = 'potential-contacts.txt'


def validate_phone_nums(doc):

    num_matches = []
    with open(doc) as f:
        # lines = f.readlines()
        # print(lines)
        for line in f:
            num_matches += re.findall(phone_reg, line)

    nums_formatted = []
    for num in num_matches:
        num = re.sub(sub_reg,"-",num)
        nums_formatted.append(num)

    for num in num_matches:
        for char in num:
            char.replace(".","-")
            char.replace(")", "-")
        if num[3] is not "-":
            num[3].insert('-')

    return print(nums_formatted)


validate_phone_nums(document)