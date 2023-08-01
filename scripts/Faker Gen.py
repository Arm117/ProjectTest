from faker import Faker
from faker.providers import address

faker = Faker()
faker.add_provider(address)

print(faker.address())