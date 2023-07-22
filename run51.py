def format_date (date):
    a = date.split('/')[::-1]
    return ''.join (a)
print(format_date("1997/10/16"))