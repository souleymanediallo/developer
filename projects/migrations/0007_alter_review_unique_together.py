# Generated by Django 5.0 on 2024-01-07 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_review_owner'),
        ('users', '0003_message'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('owner', 'project')},
        ),
    ]
