# Generated by Django 2.1.2 on 2019-06-23 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Display',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_shown', models.DateField(verbose_name='date shown')),
                ('highest_offer', models.IntegerField()),
                ('status', models.CharField(choices=[('A', 'Available'), ('S', 'Sold'), ('P', 'Sale Pending')], default='A', max_length=1)),
            ],
            options={
                'ordering': ['-date_shown'],
            },
        ),
        migrations.CreateModel(
            name='Emotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Gem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gem_type', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('location_found', models.CharField(max_length=100)),
                ('date_found', models.DateField(verbose_name='date found')),
                ('emotions', models.ManyToManyField(to='main_app.Emotion')),
            ],
        ),
        migrations.AddField(
            model_name='display',
            name='gem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Gem'),
        ),
    ]
