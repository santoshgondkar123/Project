# import phonenumbers
# from location import number

# from phonenumbers import geocoder

# pepnumber = phonenumbers.parse(number,)
# location = geocoder.description_for_number(pepnumber,"en")
# print(location)


import phonenumbers
import opencage
import folium
from phonenumbers import geocoder

# Use international format with country code
number = "+919876543210"  # Example: Indian number

# Parse the number
parsed_number = phonenumbers.parse(number, None)

# Get location description (e.g., "Maharashtra", "India")
location = geocoder.description_for_number(parsed_number, "en")

print("Location:", location)

from phonenumbers import carrier
service_pro =phonenumbers.parse(number)
print(carrier.name_for_number(service_pro,'en'))

from opencage.geocoder import OpenCageGeocode
key ="77397213003a4c0bb561e7ae342bf7a0"
geocoder =OpenCageGeocode(key)
query =str(location)
results =geocoder.geocode(query)
# print(results) 

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat , lng)


myMap = folium.Map(location=[lat,lng],ZOOM_start=9)
folium.Marker([lat , lng ], popup=location).add_to(myMap)
myMap.save("mylocation.html")