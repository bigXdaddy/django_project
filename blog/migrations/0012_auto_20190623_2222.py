# Generated by Django 2.2.2 on 2019-06-23 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20190623_2152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='writer',
            new_name='booksarewrittenbythewriter',
        ),
        migrations.AddField(
            model_name='writer',
            name='writerwrotethebooks',
            field=models.ManyToManyField(help_text='Select a genre for this book', to='blog.Book'),
        ),
    ]
