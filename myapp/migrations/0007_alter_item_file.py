# Generated by Django 4.2.14 on 2024-07-26 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_item_file_path_item_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='database/'),
        ),
    ]
