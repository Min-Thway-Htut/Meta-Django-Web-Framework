# Generated by Django 5.1.6 on 2025-03-10 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0002_reservation_delete_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductID', models.IntegerField()),
                ('name', models.TextField()),
                ('category', models.TextField()),
            ],
            options={
                'permissions': [('can_change_category', 'can change category')],
            },
        ),
    ]
