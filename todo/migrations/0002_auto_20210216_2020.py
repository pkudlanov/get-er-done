# Generated by Django 3.1.6 on 2021-02-16 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]