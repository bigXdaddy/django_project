# Generated by Django 2.2.2 on 2019-06-22 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190622_1835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='book_pics'),
        ),
    ]
