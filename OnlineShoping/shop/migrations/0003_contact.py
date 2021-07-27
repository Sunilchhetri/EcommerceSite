# Generated by Django 3.2.4 on 2021-07-14 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210704_1017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone', models.IntegerField(default='')),
                ('desc', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
