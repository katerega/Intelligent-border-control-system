# Generated by Django 2.2 on 2019-04-19 09:24

from django.db import migrations, models
import django_postgres_extensions.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0007_auto_20190419_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wanted',
            name='encodings',
            field=django_postgres_extensions.models.fields.ArrayField(base_field=models.FloatField(), blank=True, default=list, null=True, size=None),
        ),
    ]
