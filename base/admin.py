from django.contrib import admin

from base.models    import Players
from base.models    import LogGameEvents
from base.models    import PlayerAchievements
from base.models    import PlayerSessions
from base.models    import PlayerStats

admin.site.register(Players)
admin.site.register(LogGameEvents)
admin.site.register(PlayerAchievements)
admin.site.register(PlayerSessions)
admin.site.register(PlayerStats)
