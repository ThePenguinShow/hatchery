from django.contrib import admin

from models import Team, Player

class TeamAdmin(admin.ModelAdmin):
   search_fields = ('name', 'players__name', )

class PlayerAdmin(admin.ModelAdmin):
list_display = ('name', 'number', 'team', )
search_fields = ('name', 'number', 'team__name', )
list_filter = ('team', )

admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
