# Generated by Django 4.1 on 2022-11-06 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa_rpg', '0012_inventory_reportandcommend_remove_report_question_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='log_report_question',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
