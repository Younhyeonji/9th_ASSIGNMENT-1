# Generated by Django 3.2.5 on 2021-07-16 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('content', models.CharField(max_length=200)),
            ],
        ),
    ]
