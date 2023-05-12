# Generated by Django 4.2.1 on 2023-05-12 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Taxon',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('parent_id', models.IntegerField(blank=True, editable=False, null=True)),
                ('slug', models.SlugField(editable=False, max_length=255)),
                ('scientific_name', models.CharField(max_length=200)),
                ('authority', models.CharField(blank=True, max_length=200, null=True)),
                ('rank', models.CharField(blank=True, max_length=64, null=True)),
                ('parent', models.JSONField(default=dict)),
                ('classification', models.JSONField(default=list)),
                ('children', models.JSONField(default=list)),
            ],
            options={
                'ordering': ('scientific_name',),
            },
        ),
    ]
