# Generated by Django 5.0.2 on 2024-03-16 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('brand', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
            ],
        ),
    ]
