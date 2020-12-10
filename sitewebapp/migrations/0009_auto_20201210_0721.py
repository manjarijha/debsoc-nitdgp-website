# Generated by Django 2.2.15 on 2020-12-10 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitewebapp', '0008_auto_20200813_0324'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_status',
            field=models.CharField(choices=[('Upcoming', 'Upcoming'), ('Past', 'Past'), ('Live', 'Live')], default='Past', max_length=20),
        ),
        migrations.AddField(
            model_name='members',
            name='sno',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='post',
            field=models.CharField(blank=True, default='Senior Member', max_length=100, null=True),
        ),
    ]