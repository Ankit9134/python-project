import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
number =input("Enter the phone number with country code:  ")
pepnumber=phonenumbers.parse(number)
location=geocoder.description_for_number(pepnumber,"en")
ServiceProvider=carrier.name_for_number(pepnumber,"en")
print(location)
print(ServiceProvider)