# Generated by Django 3.1 on 2020-08-19 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_cab', '0002_expenses_exp_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ODR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ODR_title', models.CharField(blank=True, max_length=100)),
                ('realization', models.CharField(blank=True, max_length=100)),
                ('right_exp', models.CharField(blank=True, max_length=100)),
                ('gross_profit', models.CharField(blank=True, max_length=100)),
                ('opex', models.CharField(blank=True, max_length=100)),
                ('com_exp', models.CharField(blank=True, max_length=100)),
                ('prod_exp', models.CharField(blank=True, max_length=100)),
                ('admin_exp', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]