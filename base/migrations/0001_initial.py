# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogGameEvents',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('event_type', models.IntegerField()),
                ('event_data', models.TextField()),
                ('created', models.DateTimeField()),
            ],
            options={
                'db_table': 'log_game_events',
                'managed': False,
                'verbose_name_plural': 'Log game events',
            },
        ),
        migrations.CreateModel(
            name='PlayerAchievements',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('achievement_id', models.IntegerField()),
                ('created', models.DateTimeField()),
            ],
            options={
                'db_table': 'player_achievements',
                'managed': False,
                'verbose_name_plural': 'Player achievements',
            },
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nickname', models.CharField(unique=True, max_length=50)),
                ('xp', models.IntegerField()),
                ('email', models.CharField(unique=True, max_length=200)),
                ('password_hash', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'players',
                'managed': False,
                'verbose_name_plural': 'Players',
            },
        ),
        migrations.CreateModel(
            name='PlayerSessions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sid', models.CharField(unique=True, max_length=40)),
                ('ip_addr', models.CharField(max_length=25, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'player_sessions',
                'managed': False,
                'verbose_name_plural': 'Player sessions',
            },
        ),
        migrations.CreateModel(
            name='PlayerStats',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('stat_id', models.IntegerField()),
                ('value', models.IntegerField()),
            ],
            options={
                'db_table': 'player_stats',
                'managed': False,
                'verbose_name_plural': 'Player stats',
            },
        ),
        migrations.CreateModel(
            name='StatPlayerRegistration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('target_date', models.DateField()),
                ('register_count', models.IntegerField()),
                ('created', models.DateTimeField()),
            ],
            options={
                'db_table': 'stat_player_registration',
                'managed': False,
            },
        ),
    ]
