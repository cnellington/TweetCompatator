# Generated by Django 2.2.2 on 2019-07-15 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comparison',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user1', models.CharField(max_length=128)),
                ('user2', models.CharField(max_length=128)),
                ('user1_stats', models.TextField()),
                ('user2_stats', models.TextField()),
            ],
        ),
    ]
