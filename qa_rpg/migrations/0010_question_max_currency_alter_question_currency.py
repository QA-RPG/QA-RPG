# Generated by Django 4.1 on 2022-10-27 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("qa_rpg", "0009_alter_player_current_hp_alter_player_max_hp_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="max_currency",
            field=models.IntegerField(default=20),
        ),
        migrations.AlterField(
            model_name="question",
            name="currency",
            field=models.IntegerField(default=0),
        ),
    ]