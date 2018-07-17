# Generated by Django 2.0.7 on 2018-07-17 12:56

from django.db import migrations, models
import django.db.models.deletion
import psqlextra.manager.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            managers=[
                ('objects', psqlextra.manager.manager.PostgresManager()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('bmi', models.FloatField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='users.Group')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            managers=[
                ('objects', psqlextra.manager.manager.PostgresManager()),
            ],
        ),
    ]