# Generated by Django 3.0.1 on 2020-05-04 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200505_0159'),
        ('feed', '0002_auto_20200504_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Student'),
        ),
    ]