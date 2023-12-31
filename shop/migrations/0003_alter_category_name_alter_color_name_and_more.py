# Generated by Django 4.2 on 2023-10-07 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('SUMMER', 'Лето'), ('AUTUMN', 'Осень'), ('SPRING', 'Весна'), ('NEW', 'Новинки'), ('NEW_CATEGORY', 'Новая категория')], default='coat', max_length=20),
        ),
        migrations.AlterField(
            model_name='color',
            name='name',
            field=models.CharField(choices=[('BROWN', 'Коричневый'), ('WHITE', 'Белый'), ('PINK', 'Розовый'), ('ORANGE', 'Желтый')], default='brown', max_length=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount_price',
            field=models.DecimalField(decimal_places=4, max_digits=6, max_length=6, null=True, verbose_name='Цена со скидкой'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7, max_length=6, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='size',
            name='name',
            field=models.CharField(blank=True, choices=[('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45')], default='s', max_length=4),
        ),
    ]
