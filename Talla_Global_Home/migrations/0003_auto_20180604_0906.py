# Generated by Django 2.0.3 on 2018-06-04 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Talla_Global_Home', '0002_auto_20180604_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Investment_Date',
            field=models.DateTimeField(null=True, verbose_name='Investment Date'),
        ),
    ]