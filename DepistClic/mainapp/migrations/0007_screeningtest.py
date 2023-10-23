# Generated by Django 4.2.5 on 2023-10-20 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScreeningTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200)),
                ('frequency', models.CharField(max_length=50)),
                ('source_text', models.CharField(max_length=50)),
                ('source_link', models.CharField(max_length=50)),
                ('info', models.TextField()),
            ],
        ),
    ]
