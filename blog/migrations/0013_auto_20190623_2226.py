# Generated by Django 2.2.2 on 2019-06-23 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20190623_2222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='booksarewrittenbythewriter',
            new_name='the_writer',
        ),
    ]
