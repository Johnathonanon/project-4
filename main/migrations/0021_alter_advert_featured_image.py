# Generated by Django 3.2 on 2022-07-15 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_delete_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]