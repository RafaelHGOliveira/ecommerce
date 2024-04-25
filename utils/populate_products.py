import os
import sys
import django
import random
from pathlib import Path
from faker import Faker
from lorem.text import TextLorem  # Importa o gerador de texto Lorem Ipsum

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 1000

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'

django.setup()
from product.models import Category, Product

fake = Faker()
lorem = TextLorem(srange=(4, 8))  # Cria uma instância do gerador Lorem Ipsum


def create_fake_categories(num_categories):
    for _ in range(num_categories):
        name = fake.word()
        category = Category.objects.create(name=name)
        print(f"Categoria criada: {category}")


def create_fake_products(num_products):
    categories = Category.objects.all()
    for _ in range(num_products):
        name = fake.word()
        price = round(random.uniform(10, 1000), 2)
        stock = random.randint(0, 100)
        long_description = lorem.paragraph()  # Usa Lorem Ipsum para a descrição longa
        short_description = fake.sentence()
        category = random.choice(categories)
        product = Product.objects.create(
            name=name,
            price=price,
            stock=stock,
            long_description=long_description,
            short_description=short_description,
            category_ref=category
        )
        print(f"Produto criado: {product}")


if __name__ == '__main__':
    # create_fake_categories(10)
    create_fake_products(100)
