# Generated by Django 5.0 on 2024-01-07 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['create']},
        ),
        migrations.AlterField(
            model_name='project',
            name='featured_image',
            field=models.CharField(blank=True, default='https://media.istockphoto.com/id/1305995602/fr/photo/conception-r%C3%A9active-flottante-r%C3%A9active.jpg?s=2048x2048&w=is&k=20&c=NQYG8GK8BdSKqDWsefpwJhcnUlC_ZJoALD-nGM_Tbgk=', max_length=300, null=True),
        ),
    ]