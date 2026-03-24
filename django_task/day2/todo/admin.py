from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from todo.models import Todo, Comment

admin.site.register(Comment)

class CommentInline(admin.TabularInline):
    model = Comment
    fields = [
        'message',
    ]
    extra = 1




@admin.register(Todo)
class TodosAdmin(SummernoteModelAdmin):
    summernote_fields = ('description', )
    inlines = [CommentInline]
    #fieldsets
    fieldsets = [
        ('기본정보', {'fields': ('title', 'is_completed', )}),
        ('본문', {'fields': ('description', 'start_date', 'end_date')}),
        ('이미지', {'fields': ('completed_image',)}),
    ]