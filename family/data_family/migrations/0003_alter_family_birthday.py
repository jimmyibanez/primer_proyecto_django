# Generated by Django 4.0.6 on 2022-07-29 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_family', '0002_family_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]
