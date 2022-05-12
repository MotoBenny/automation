import re

phone_reg = r'\b\d{3}\D?\d{3}\D?\d{4}'
sub_reg = r"[.)]"
email_reg = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}"
document = 'potential-contacts.txt'


def insert_tacs(phone_num):
    completed_num = phone_num[:3] + '-' + phone_num[3:6] + "-" + phone_num[6:]
    return completed_num


def validate_phone_nums(doc):
    num_matches = []
    with open(doc) as f:
        for line in f:
            num_matches += re.findall(phone_reg, line)

    nums_formatted = []
    for num in num_matches:
        num = re.sub(sub_reg, "-", num)
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


with open('phone_numbers.txt', 'w') as file:
    for number in completed_list:
        file.write(number)
        file.write('\n')


def validate_emails(doc):
    email_matches = []
    with open(doc) as f:
        for line in f:
            email_matches += re.findall(email_reg, line)

    return email_matches


completed_email = validate_emails(document)

with open('emails.txt', "w") as file:
    for email in completed_email:
        file.write(email)
        file.write('\n')