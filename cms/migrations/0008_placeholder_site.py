# Generated by Django 2.2.7 on 2019-11-28 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0007_placeholder'),
    ]

    operations = [
        migrations.AddField(
            model_name='placeholder',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cms.Site'),
            preserve_default=False,
        ),
    ]
