# Generated by Django 3.0.5 on 2020-04-18 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Titanic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survived', models.IntegerField()),
                ('pclass', models.IntegerField()),
                ('sex', models.IntegerField()),
                ('age', models.FloatField()),
                ('sibsp', models.IntegerField()),
                ('parch', models.IntegerField()),
                ('fare', models.FloatField()),
                ('embarked', models.IntegerField()),
                ('title', models.IntegerField()),
            ],
        ),
    ]