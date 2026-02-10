import urllib.request
import urllib.parse
import json

serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'

location = input('Enter location: ')
if not location:
    print("No location entered.")
else:
    params = urllib.parse.urlencode({'q': location})
    url = serviceurl + params
    print('Retrieving', url)

    response = urllib.request.urlopen(url)
    data = response.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except json.JSONDecodeError:
        print("Failed to parse JSON response.")
        exit()

    # Navigate to the first plus_code in the features list
    features = js.get('features', [])
    if not features:
        print("No features found in response.")
    else:
        plus_code = features[0].get('properties', {}).get('plus_code')
        if plus_code:
            print('Plus code', plus_code)
        else:
            print("No plus_code found in first feature.")
