# Generated by Django 4.0.4 on 2022-05-03 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=50)),
                ('description', models.TextField(max_length=250)),
                ('price', models.PositiveIntegerField()),
                ('category', models.IntegerField(choices=[(1, 'mobile'), (2, 'electric'), (3, 'household')])),
            ],
        ),
    ]
