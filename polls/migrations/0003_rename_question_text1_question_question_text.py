# Generated by Django 4.1.5 on 2023-02-20 01:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0002_rename_question_text_question_question_text1"),
    ]

    operations = [
        migrations.RenameField(
            model_name="question",
            old_name="question_text1",
            new_name="question_text",
        ),
    ]
