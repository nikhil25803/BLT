# Generated by Django 3.0.7 on 2020-06-21 12:21

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0053_auto_20200619_0551'),
    ]

    operations = [
        migrations.AddField(
            model_name='hunt',
            name='name',
            field=models.CharField(default='1', max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hunt',
            name='description',
            field=mdeditor.fields.MDTextField(blank=True, null=True),
        ),
    ]