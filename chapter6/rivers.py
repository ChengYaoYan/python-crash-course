rivers = {
    'Sepik River': 'New Guinea',
    'Mississippi River': 'the United States',
    'Volga River': 'Europe',
    'Zambezi': 'Africa',
    'Mekong River': 'Tibetan Plateau',
    'Ganges': 'India',
    'Danube': 'Europe',
    'Yangtze River': 'China',
    'Nile': 'East Africa',
    'Amazon River': 'Peru'
}

[print(f"the {river} runs through {region}.") for river,region in rivers.items()]

print()
print("rivers:")
[print(f"{river}") for river in rivers.keys()]

print()
print("regions:")
[print(f"{region}") for region in rivers.values()]
