# Generated by Django 4.2.2 on 2023-06-15 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='level',
            field=models.CharField(choices=[(1, 'Junior'), (2, 'Middle'), (3, 'Senior')], default=1, max_length=10),
        ),
    ]