# Generated by Django 3.2 on 2021-04-19 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='student_state',
            new_name='graduation_state',
        ),
    ]