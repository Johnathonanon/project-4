# Generated by Django 3.2 on 2022-04-05 14:29

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_advert_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from=['title', 'description', 'seller'], unique=True),
        ),
    ]
