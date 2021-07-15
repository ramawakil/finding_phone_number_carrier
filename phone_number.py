import phonenumbers
from phonenumbers import carrier


number = phonenumbers.parse(input("phone number yako pls: "), None)
print(carrier.name_for_number(number, lang="en"))