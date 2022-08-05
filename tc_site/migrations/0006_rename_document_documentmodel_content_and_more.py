# Generated by Django 4.0.6 on 2022-08-05 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tc_site', '0005_companymodel_app_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documentmodel',
            old_name='document',
            new_name='content',
        ),
        migrations.AddField(
            model_name='documentmodel',
            name='document_type',
            field=models.CharField(default='TC', max_length=10),
            preserve_default=False,
        ),
    ]