# Generated by Django 5.2.2 on 2025-06-06 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='email',
            new_name='customer_email',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='customer_name',
        ),
        migrations.AddField(
            model_name='customer',
            name='status',
            field=models.CharField(default='pending', max_length=20),
        ),
    ]
