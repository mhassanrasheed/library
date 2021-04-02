# Generated by Django 3.1.7 on 2021-04-02 10:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_auto_20210401_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='return_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='loan',
            name='status',
            field=models.CharField(choices=[('D', 'Due'), ('R', 'Returned')], default='D', max_length=20),
        ),
        migrations.AlterField(
            model_name='loan',
            name='check_out_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
