# Make several dictionaries, where each
# dictionary represents a different pet. In each
# dictionary, include the kind of animal and the
# owner's name. Store these dictionaries in a list
# named pets. Next, loop through your list and as
# you do, print everything you know about each
# pet.

pets = {
    "a_apollo": {
        "age": 1,
        "type": "canine",
        "likes": "keep away",
    },
    "a_hercules": {
        "age": 15,
        "type": "canine",
        "likes": "keep away",
    },
}

for key, value in pets.items():
    print(f"Pets Username: {key}")
    print(f"Pets Information: {value}")
