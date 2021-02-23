motocrycles = ['Yamaha', 'Suzuki', 'Honda', 'Kawasaki']
message = f"I would like to own a {motocrycles[3]} motocrycles"

print(message)

motocrycles.append('Ducati')
print(motocrycles)

motocrycles.insert(2, 'Ducati')
print(motocrycles)

del motocrycles[2]
print(motocrycles)

print(motocrycles)
poped_motocycle = motocrycles.pop()
print(poped_motocycle)
print(motocrycles)

motocrycles.pop(2)
print(motocrycles)

too_expensive = 'Yamaha'
motocrycles.append('Yamaha')
print(motocrycles)
# only remove the first found one
motocrycles.remove(too_expensive)
print(motocrycles)
