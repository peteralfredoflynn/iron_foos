# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-04 21:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_num', models.IntegerField()),
                ('game_num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tourney',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('players', models.ManyToManyField(to='foos.Player')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='player1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player1', to='foos.Player'),
        ),
        migrations.AddField(
            model_name='game',
            name='player2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player2', to='foos.Player'),
        ),
        migrations.AddField(
            model_name='game',
            name='tourney',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foos.Tourney'),
        ),
        migrations.AddField(
            model_name='game',
            name='winner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='foos.Player'),
        ),
    ]
