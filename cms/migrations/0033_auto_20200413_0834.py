# Generated by Django 2.2.7 on 2020-04-13 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0032_page_sitemap_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='title',
            field=models.CharField(default='beget', help_text='beget,regru,timeweb', max_length=50, verbose_name='Хостинг'),
        ),
    ]
