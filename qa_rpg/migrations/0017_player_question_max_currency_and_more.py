# Generated by Django 4.1.2 on 2022-11-08 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa_rpg', '0016_question_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='question_max_currency',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='player',
            name='question_rate_currency',
            field=models.IntegerField(default=5),
        ),
    ]
