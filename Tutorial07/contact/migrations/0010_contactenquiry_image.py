# Generated by Django 4.2.2 on 2023-07-15 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0009_alter_contactenquiry_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactenquiry',
            name='image',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='contact/'),
        ),
    ]