# Generated by Django 3.2.13 on 2022-10-07 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='grade',
            field=models.IntegerField(max_length=5),
        ),
    ]
