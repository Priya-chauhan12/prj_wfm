# Generated by Django 4.0.1 on 2022-03-04 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodForAll', '0003_feedback_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='image',
            field=models.ImageField(default='', upload_to='prc'),
        ),
    ]