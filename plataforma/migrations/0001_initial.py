# Generated by Django 4.0.6 on 2022-08-04 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acidente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('local', models.TextField()),
                ('nome_funcionario', models.TextField()),
            ],
        ),
    ]