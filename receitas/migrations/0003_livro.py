# Generated by Django 4.2.1 on 2023-06-14 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0002_log'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=400)),
                ('isbn', models.CharField(max_length=400)),
                ('editora', models.CharField(max_length=400)),
                ('autor', models.CharField(max_length=400)),
                ('versao_fisica', models.BooleanField(verbose_name=True)),
            ],
        ),
    ]
