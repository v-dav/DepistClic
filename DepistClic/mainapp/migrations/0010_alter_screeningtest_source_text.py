# Generated by Django 4.2.5 on 2023-10-21 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_alter_screeningtest_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screeningtest',
            name='source_text',
            field=models.TextField(max_length=200),
        ),
    ]
