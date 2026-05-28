def validate_mpesa(number):
if number.startswith('254') and len(number) == 12:
return 'Valid Kenyan M-Pesa number'
elif number.startswith('07') and len(number) == 10:
return 'Valid but use 254 format for API'
else:
return 'Invalid M-Pesa number'
print(validate_mpesa('254712345678'))
print(validate_mpesa('0712345678'))
print(validate_mpesa('123456'))
