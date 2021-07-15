import phonenumbers
from phonenumbers import carrier


number = phonenumbers.parse(f'+255{input("phone number yako pls:: ")}', None)
print(carrier.name_for_number(number, lang="en"))