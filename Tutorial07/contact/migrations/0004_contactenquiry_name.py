# Generated by Django 4.2.2 on 2023-07-15 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_remove_contactenquiry_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactenquiry',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]