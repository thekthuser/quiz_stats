# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-12 16:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_answer_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='project_id',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='question_id',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='next_question_id',
            new_name='next_question',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='project_id',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='relationship',
            old_name='project_id',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='relationship',
            old_name='question_id',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='relationship',
            old_name='token_id',
            new_name='token',
        ),
        migrations.RenameField(
            model_name='token',
            old_name='project_id',
            new_name='project',
        ),
    ]