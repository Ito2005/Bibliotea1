# Generated by Django 5.1.1 on 2024-10-31 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_autor"),
    ]

    operations = [
        migrations.RenameField(
            model_name="autor",
            old_name="descricao",
            new_name="nome",
        ),
        migrations.AddField(
            model_name="autor",
            name="email",
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
    ]
