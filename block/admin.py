from django.contrib import admin

from models import Block


class BetterShowAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'owner', 'create_timestamp', 'last_update_timestamp')

admin.site.register(Block, BetterShowAdmin)
