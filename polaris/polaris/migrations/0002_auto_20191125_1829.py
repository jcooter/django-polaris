# Generated by Django 2.2.4 on 2019-11-25 18:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polaris", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="status_message",
            field=models.TextField(blank=True, null=True),
        )
    ]
