# Generated by Django 4.2.11 on 2024-04-15 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorialapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200, null=True)),
                ('lastname', models.CharField(max_length=200, null=True)),
                ('roomnumber', models.CharField(max_length=200, null=True)),
                ('subject', models.CharField(choices=[('Fine Art', 'Fine Art'), ('Math', 'Math'), ('PE/Health', 'PE/Health'), ('practical Art', 'Practical Art'), ('English', 'English'), ('Social Studies', 'Social Studies'), ('Science', 'Science')], max_length=200, null=True)),
            ],
        ),
    ]
