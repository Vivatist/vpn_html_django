# Generated by Django 4.2.5 on 2023-09-25 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0006_alter_blockedsites_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockedsites',
            name='favicon',
            field=models.ImageField(upload_to='mainpage/static/mainpage/images/blocked_icons/', verbose_name='Иконка'),
        ),
    ]
