# Generated by Django 3.1.3 on 2021-01-25 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_books_is_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]