place = {
    'name': 'The Anchor',
    'post_code': 'E14 6HY',
    'street_number': '54',
    'location': {
        'longitude': 127,
        'latitude': 63,
    }
}

print(place['name']) 
print(place['post_code'])
print(place['street_number'])
print(place['location']['longitude'], place['location']['latitude'])

