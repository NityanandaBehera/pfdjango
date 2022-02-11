# Generated by Django 4.0.2 on 2022-02-09 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('base', '0003_project_featured_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
    ]
