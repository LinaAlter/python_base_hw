ids = {
    'user1': [213, 213, 213, 15, 213],
    'user2': [54, 54, 119, 119, 119],
    'user3': [213, 98, 98, 35]
}

unique_geotags = set()

for tags in ids.values():
    unique_geotags.update(tags)

print(unique_geotags)    

