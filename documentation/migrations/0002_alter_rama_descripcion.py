# Generated by Django 4.0 on 2022-08-02 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rama',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
    ]