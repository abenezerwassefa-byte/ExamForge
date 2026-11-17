from django.contrib import admin
from .models import Subject, Topic, Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'topic', 'difficulty')
    list_filter = ('difficulty', 'topic')
    search_fields = ('text',)
    inlines = [ChoiceInline]


admin.site.register(Subject)
admin.site.register(Topic)
admin.site.register(Choice)
