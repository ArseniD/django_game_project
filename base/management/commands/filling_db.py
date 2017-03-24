# -*- coding: utf-8 -*-


import hashlib
import datetime
import random

from django.core.management.base import BaseCommand, CommandError
from base.models import Players, PlayerSessions, StatPlayerRegistration

from random import randrange
from datetime import timedelta
from datetime import date




def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


class Command(BaseCommand):
    help = 'Fill up db with data'
    def add_arguments(self, parser):
        parser.add_argument('--player-count',           default=10, type=int)
        parser.add_argument('--session-count-per-user', default=3,  type=int)
        parser.add_argument('--stat-count',             default=20,  type=int)

    def _create_session(self, player_object, session_index):
        session = PlayerSessions()
        session_unique_part = str(session_index) + str(datetime.datetime.now())
        session_uuid = hashlib.sha1(session_unique_part).hexdigest()
        session.player = player_object
        session.sid = session_uuid
        session.is_finished = bool(random.randint(0, 1))
        session_ttl = random.randint(10, 7200)
        session.updated = datetime.datetime.now() + datetime.timedelta(seconds=session_ttl)
        session.save()


    def _create_player(self, player_index, options):
        player = Players()
        nickname_unique_part = str(player_index) + str(datetime.datetime.now())
        nickname_unique_hash = hashlib.sha1(nickname_unique_part).hexdigest()[:10]
        player.nickname = "test_{}".format(nickname_unique_hash)
        player.email = "{}@tut.by".format(player.nickname)
        player.xp = 0
        player.save()
        for session_index in xrange(options["session_count_per_user"]):
            self._create_session(player, session_index)


    def _create_stat(self, stat_index, options):
        stat = StatPlayerRegistration()
        d1 = datetime.datetime(2015, 12, 1, 1, 30)
        d2 = datetime.datetime(2016, 2, 1, 1, 30)
        # Using function mentioned above
        stat.target_date = random_date(d1, d2)
        stat.register_count = random.randint(3, 100)
        stat_ttl = random.randint(10, 7200)
        stat.created = datetime.datetime.now() + datetime.timedelta(seconds=stat_ttl)
        # assuming which duplicate is removed doesn't matter
        for row in StatPlayerRegistration.objects.all():
            if StatPlayerRegistration.objects.filter(target_date=row.target_date).count() > 1:
                row.delete()
        stat.save()


    def handle(self, *args, **options):
        for i in xrange(options["player_count"]):
            self._create_player(i, options)
        for i in xrange(options["stat_count"]):
            self._create_stat(i, options)