from utils.imports import *


def generate_fake_paste(locale='RU'):
    faker = Faker(locale)
    name = faker.name()
    adress = faker.address()
    email = faker.free_email()
    job = faker.job()
    phone = faker.phone_number()
    pasport = faker.passport_dob()
    print(f'Имя: {name}\nАдрес:{adress}\nЭл.почта:{email}\nНомер телефона:{phone}\nРабота:{job}\nПаспорт:{pasport}')

