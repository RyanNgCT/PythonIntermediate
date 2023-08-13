# mutable data structure
scientists = [
    {'name': 'Ada Lovelace', 'field': 'Math', 'born': 1815,'nobelAwarded' : False},
    {'name': 'Emmy Noether', 'field': 'Math', 'born': 1882,'nobelAwarded' : False},
    {'name': 'Marie Curie', 'field': 'Physics', 'born': 1867,'nobelAwarded' : True},
    {'name': 'Tu Youyou', 'field': 'Chemistry', 'born': 1930,'nobelAwarded' : True},
    {'name': 'Ada Yonath', 'field': 'Chemistry', 'born': 1939,'nobelAwarded' : True},
    {'name': 'Vera Rubin', 'field': 'Astronomy', 'born': 1928,'nobelAwarded' : False},
    {'name': 'Sally Ride', 'field': 'Physics', 'born': 1951,'nobelAwarded' : False}
]

scientists[0]['name'] = 'Ed Lovelace' # modifiable

for scientist in scientists:
    if scientist['born'] > 1900:
        print(f"{scientist['name']} was born after the Year 1900.")
    else:
        print(f"{scientist['name']} was born before the Year 1900.")