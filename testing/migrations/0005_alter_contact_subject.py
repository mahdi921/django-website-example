# Generated by Django 4.2.17 on 2025-01-04 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0004_alter_contact_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]
