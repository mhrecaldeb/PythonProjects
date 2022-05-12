from gettext import lngettext
import urllib.request, urllib.parse, urllib.error
import json

# http://py4e-data.dr-chuck.net/json?address=Ann+Arbor%2C+MI&key=42

serviceurl = 'http://py4e-data.dr-chuck.net/json?'  #en lugar de usar el de google

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    address2 = urllib.parse.urlencode({'address': address})
    print(address2)

    url = serviceurl + urllib.parse.urlencode({'address': address}) + '&key=42' # last part is the key requiered to access this url

    print('Retrieving', url)

    uh = urllib.request.urlopen(url)

    data = uh.read().decode('utf-8')

    print("Retrieved", len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent = 4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]

    print('lat', lat, 'lng', lng)

    location = js['results'][0]['formatted_address']

    print(location)
