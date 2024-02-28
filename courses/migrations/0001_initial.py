# Generated by Django 5.0.1 on 2024-01-27 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=250, null=True)),
                ('price', models.IntegerField(default=499)),
                ('discount', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=False)),
                ('thumbnail', models.ImageField(upload_to='flies/tumbnail')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('resourse', models.FileField(upload_to='flies/resourse')),
                ('length', models.IntegerField()),
            ],
        ),
    ]