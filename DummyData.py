# pip install faker

from faker import faker 
fake = faker()
print(fake.name())
print(fake.address())
print(fake.text())
print(fake.email())
print(fake.country())
print(fake.latitude(),fake.longitude())
print(fake.url())