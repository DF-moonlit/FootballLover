# Generated by Django 2.1.8 on 2020-03-03 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20191110_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='fnsuser',
            name='sessionId',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
