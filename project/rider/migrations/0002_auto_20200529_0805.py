# Generated by Django 3.0.6 on 2020-05-29 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rider', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rider',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]