# Generated by Django 5.1.6 on 2025-02-22 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_name_person_person_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menuitems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('course', models.CharField(max_length=300)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
