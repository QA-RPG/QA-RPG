# Generated by Django 4.1 on 2022-10-27 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("qa_rpg", "0010_question_max_currency_alter_question_currency"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="category",
            field=models.CharField(default="test", max_length=100),
        ),
    ]
