# Generated by Django 2.2.2 on 2019-06-28 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0035_auto_20190627_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publication',
            field=models.CharField(default='none', max_length=200),
        ),
    ]
