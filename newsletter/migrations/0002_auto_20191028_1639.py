# Generated by Django 2.2.5 on 2019-10-28 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertise',
            old_name='linkurl',
            new_name='link_url',
        ),
    ]
