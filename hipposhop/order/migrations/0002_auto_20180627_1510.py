# Generated by Django 2.0.6 on 2018-06-27 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='withdrawcash',
            name='alipay_account',
        ),
        migrations.AddField(
            model_name='withdrawcash',
            name='open_id',
            field=models.CharField(default='', max_length=50, verbose_name='openid'),
        ),
    ]
