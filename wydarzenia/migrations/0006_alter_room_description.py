# Generated by Django 4.1.6 on 2023-03-21 09:35

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):
    dependencies = [
        ("wydarzenia", "0005_rename_price_message_cena_remove_message_body_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="description",
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
