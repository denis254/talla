# Generated by Django 2.0.3 on 2018-06-04 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Talla_Global_Home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Cash_Balance',
            new_name='Cash_Invested',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='Point_Balance',
            new_name='Interest',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='User_Type',
        ),
        migrations.AddField(
            model_name='profile',
            name='Investment_Date',
            field=models.DateTimeField(null=True, verbose_name='Date Published'),
        ),
        migrations.AddField(
            model_name='profile',
            name='Phone_Number',
            field=models.CharField(max_length=30, null=True),
        ),
    ]