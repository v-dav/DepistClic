# Generated by Django 4.2.5 on 2023-10-21 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_alter_screeningtest_source_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='screeningtest',
            name='type',
            field=models.CharField(choices=[('Systématique', 'Systématique'), ('Conditionnel', 'Conditionnel')], default='Systématique', max_length=15),
        ),
    ]
