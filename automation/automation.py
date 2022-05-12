import re
import os

phone_reg = r'\b\d{3}\D?\d{3}\D?\d{4}'
sub_reg = r"[.)]"

document = 'potential-contacts.txt'


def insert_tacs(phone_num):
    completed_num = phone_num[:3] + '-' + phone_num[4:7] + "-" + phone_num[7:]
    return completed_num


def validate_phone_nums(doc):
    num_matches = []
    with open(doc) as f:
        for line in f:
            num_matches += re.findall(phone_reg, line)

    nums_formatted = []
    for num in num_matches:
        num = re.sub(sub_reg,"-",num)
        nums_formatted.append(num)

    completed_nums = []
    for phone_num in nums_formatted:
        if phone_num[3] != '-':
            taced_num = insert_tacs(phone_num)
            completed_nums.append(taced_num)
        else:
            completed_nums.append(phone_num)

    completed_nums = list(dict.fromkeys(completed_nums))
    return completed_nums

completed_list = validate_phone_nums(document)
print(os.getcwd())
with open('phone_numbers.txt', 'w') as phone_doc:
    for item in completed_list:
        phone_doc.write("%s\n" % item)
