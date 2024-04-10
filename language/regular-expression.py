import re

def common_log_format_example():
    line = '127.0.0.1 - rj [13/Nov/2019:14:34:30 -0000] "GET HTTP/1.0" 200'
    mch = re.search(r'\d.\d.\d.\d.\d.', line) # wrong, since \d means only 1 digit
    matched_ip = re.search(r'\d+[.]\d+[.]\d+[.]\d+', line) # this is correct for ip address
    # print('ip:', matched_ip)
    # print('ip.group():', matched_ip.group())

    # // matched_num = re.search(r'\d*')
    # // matched_num = re.search('\d*', line)
    matched_optional_num = re.search(r'\d*', line)
    print('mached_optional_num str:', matched_optional_num.group())

    matched_nums = re.findall(r'\d+', line)
    print('mached_nums:', matched_nums)

    matched_times = re.findall(r'\d+[/][a-zA-Z]{3}[/]\d+[:]\d+[:]\d+[:]\d+', line)
    print('matched_times:', matched_times)

    matched_special1 = re.findall(r'[a-zA-Z]*[/]', line)
    print('matched_special1:', matched_special1)


common_log_format_example()

