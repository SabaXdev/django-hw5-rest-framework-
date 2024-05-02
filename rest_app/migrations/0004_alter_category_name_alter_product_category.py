# Generated by Django 5.0.4 on 2024-05-01 13:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app', '0003_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Enter the name of the category', max_length=100, verbose_name='Author name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(help_text='Enter the category of the product', on_delete=django.db.models.deletion.CASCADE, to='rest_app.category', verbose_name='Category'),
        ),
    ]
