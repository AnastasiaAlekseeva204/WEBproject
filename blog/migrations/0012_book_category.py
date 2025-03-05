# Generated by Django 5.1.6 on 2025-02-27 08:09

import django.db.models.deletion
import mptt.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=mptt.fields.TreeForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.category'),
        ),
    ]
