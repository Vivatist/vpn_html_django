# Generated by Django 4.2.5 on 2023-09-25 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0003_settings'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockedSites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(auto_created=True, verbose_name='Активно')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('url', models.URLField(verbose_name='URL заблокированного ресурса')),
                ('description', models.CharField(max_length=200, verbose_name='Описание')),
                ('favicon', models.ImageField(upload_to='blocked_icons/', verbose_name='Иконка')),
            ],
            options={
                'verbose_name': 'Заблокированные сайты',
                'verbose_name_plural': 'Заблокированные сайты',
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='settings',
            name='url_support',
            field=models.URLField(verbose_name='URL телеграм-канала техподдержки'),
        ),
    ]
