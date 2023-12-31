# Generated by Django 4.2 on 2023-04-30 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ByersData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.PositiveIntegerField()),
                ('country', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=60)),
                ('street', models.CharField(max_length=60)),
                ('house', models.PositiveIntegerField()),
                ('flat', models.PositiveIntegerField()),
                ('message', models.TextField()),
            ],
        ),
    ]
