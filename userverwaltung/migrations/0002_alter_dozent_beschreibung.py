# Generated by Django 4.2.2 on 2023-06-20 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userverwaltung', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dozent',
            name='beschreibung',
            field=models.TextField(blank=True, verbose_name='Beschreibung'),
        ),
    ]