from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from transliterate import translit


class Size(models.Model):
    XS = '40'
    S = '41'
    M = '42'
    L = '43'
    XL = '44'
    XXL = '45'
    SIZE_CHOICES = [
        (XS, '40'),
        (S, '41'),
        (M, '42'),
        (L, '43'),
        (XL, '44'),
        (XXL, '45'),
    ]
    name = models.CharField(max_length=4, null=False, default='s', blank=True, choices=SIZE_CHOICES)
    slug = models.SlugField(default='', null=False, max_length=150)

    def __str__(self):
        for color in self.SIZE_CHOICES:
            if color[0] == self.name:
                return color[1]
        return self.name


class Color(models.Model):
    BROWN = 'BROWN'
    WHITE = 'WHITE'
    PINK = 'PINK'
    ORANGE = 'ORANGE'

    COLOR_CHOICES = (
        (BROWN, 'Коричневый'),
        (WHITE, 'Белый'),
        (PINK, 'Розовый'),
        (ORANGE, 'Желтый'),
    )
    name = models.CharField(max_length=6, null=False, default='brown', choices=COLOR_CHOICES)
    slug = models.SlugField(default='', null=False, max_length=150)

    def __str__(self):
        for color in self.COLOR_CHOICES:
            if color[0] == self.name:
                return color[1]
        return self.name

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(translit(self.name, 'ru', reversed=True))
    #     super(Color, self).save(*args, **kwargs)


class Category(models.Model):
    SUMMER = 'SUMMER'
    AUTUMN = 'AUTUMN'
    SPRING = 'SPRING'
    NEW = 'NEW'
    NEW_CATEGORY = 'NEW_CATEGORY'

    CATEGORY_CHOICES = (
        (SUMMER, 'Лето'),
        (AUTUMN, 'Осень'),
        (SPRING, 'Весна'),
        (NEW, 'Новинки'),
        (NEW_CATEGORY, 'Новая категория'))

    name = models.CharField(max_length=20, null=False, default='coat', choices=CATEGORY_CHOICES)
    slug = models.SlugField(default='', null=False, max_length=150)

    def __str__(self):
        for choice in self.CATEGORY_CHOICES:
            if choice[0] == self.name:
                return choice[1]
        return self.name  # fallback, если не нашли название в CHOICES

    def get_slug_category(self):
        return f"/shop/{self.slug}"

    def save(self, *args, **kwargs):
        self.slug = slugify(translit(self.name, 'ru', reversed=True))
        super(Category, self).save(*args, **kwargs)

    def get_url_category(self):
        return reverse('category', args=[self.slug])


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.PROTECT, null=True)
    cover = models.ImageField(upload_to='', verbose_name='Фото')
    price = models.DecimalField(max_digits=7, verbose_name='Цена', decimal_places=2, null=True, max_length=6)
    percentage = models.DecimalField(max_digits=5, decimal_places=5, null=True, verbose_name='Процент скидки',
                                     blank=True)
    discount_price = models.DecimalField(max_digits=6, verbose_name='Цена со скидкой', decimal_places=4, null=True,
                                         max_length=6)
    size = models.ManyToManyField(Size, verbose_name='Размер')
    color = models.ManyToManyField(Color, verbose_name='Цвет')
    slug = models.SlugField(default='', null=False, max_length=150)

    @property
    def image_url(self):
        try:
            url = self.cover.url
        except:
            url = ''
        return url

    # def __str__(self):
    #     return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(translit(self.title, 'ru', reversed=True))
        super(Product, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('one-item', args=[self.slug])

    # def get_url_category(self):
    #     return reverse('product-category', args=[self.category.slug])

    # def get_url_add_product(self):
    #     return reverse('all-category', args=[self.category])
