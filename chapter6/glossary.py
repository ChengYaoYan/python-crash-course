glossaries = {
  'lists': 'Lists are used to store multiple items in a single variable',
  'variables': 'Variables are containers for storing data values',
  'dictionaries': 'Dictionaries are used to store data values in key:value pairs'
}

[print(f"{key.title()}: {glossaries[key]}.\n") for key in glossaries]
