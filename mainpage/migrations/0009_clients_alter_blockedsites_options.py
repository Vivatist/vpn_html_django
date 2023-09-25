# Generated by Django 4.2.5 on 2023-09-25 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0008_delete_links_alter_blockedsites_favicon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('url', models.URLField(verbose_name='Ссылка на скачивание')),
                ('logo', models.ImageField(upload_to='upload/', verbose_name='Логотип клиента')),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.AlterModelOptions(
            name='blockedsites',
            options={'ordering': ['name'], 'verbose_name': 'Заблокированный сайт', 'verbose_name_plural': 'Заблокированные сайты'},
        ),
    ]
