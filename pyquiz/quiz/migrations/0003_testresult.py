# Generated by Django 3.0.8 on 2020-08-08 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20200808_0837'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='quiz.Test')),
            ],
        ),
    ]