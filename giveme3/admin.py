from django.contrib import admin

from .models import Item, Trait, VotedTrait


class VotedTraitInLine(admin.TabularInline):
    model = Item.traits.through
    extra = 3


class ItemAdmin(admin.ModelAdmin):
    inlines = [VotedTraitInLine]

admin.site.register(Item, ItemAdmin)
admin.site.register(Trait)
