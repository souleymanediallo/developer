# Generated by Django 5.0 on 2024-01-07 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_project_options_alter_project_featured_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='projet',
            new_name='project',
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('project', 'id')},
        ),
    ]