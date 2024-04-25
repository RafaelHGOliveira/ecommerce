from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from django.utils.text import slugify

class Base(models.Model):
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    modified_at = models.DateTimeField('Modificado em', auto_now=True)
    active = models.BooleanField('Ativo', default=True)


class Category(Base):
    name = models.CharField(max_length=254, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Product(Base):
    name = models.CharField('Nome', max_length=254, unique=True)
    price = models.FloatField('Preço', default=0)
    stock = models.IntegerField('Estoque', default=0)
    long_description = models.TextField('Descrição longa')
    short_description = models.TextField('Descrição curta')
    slug = models.SlugField(null=False, max_length=50)
    category_ref = models.ForeignKey(
        Category, on_delete=models.PROTECT, verbose_name='Categoria'
    )

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Picture(models.Model):
    picture = models.ImageField(
        'Foto', blank=True, upload_to='pictures/%Y/%m/')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='Produto')

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'


@receiver(post_save, sender=Picture)
def resize_image(sender, instance, **kwargs):
    if instance.picture:
        with Image.open(instance.picture.path) as img:
            img_resized = img.resize((480, 480))
            img_resized.save(instance.picture.path)
