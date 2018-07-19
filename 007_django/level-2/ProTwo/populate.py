import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

# Fake pop JavaScript
import random
from AppTwo.models import Users
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):

        fake_f_name = fakegen.first_name()
        fake_l_name = fakegen.last_name()
        fake_email = fakegen.email()

        Users.objects.get_or_create(f_name = fake_f_name, l_name=fake_l_name, email=fake_email)[0]


if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete!")
