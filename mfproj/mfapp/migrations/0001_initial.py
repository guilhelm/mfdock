# Generated by Django 3.2 on 2021-04-14 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Peak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('lat', models.DecimalField(decimal_places=5, max_digits=7, verbose_name='Latitude')),
                ('lon', models.DecimalField(decimal_places=5, max_digits=8, verbose_name='Longitude')),
                ('altitude', models.DecimalField(decimal_places=0, max_digits=4, verbose_name='Altitude')),
            ],
            options={
                'managed': True,
            },
        ),
    ]
