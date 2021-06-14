from django.contrib import admin
from .models import Note, Comment

class CommentAdmin(admin.ModelAdmin):
        raw_id_fields = ['note']

try:
        admin.site.unregister(Comment)
except: pass
admin.site.register(Comment,CommentAdmin)
admin.site.register(Note)
