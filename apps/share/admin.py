from django.contrib import admin
from .models import ChildLessons, ParentLessons, Downloads, Doc, Exercise, Frame


class ParentLessonsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'submit_time')
    search_fields = ['id', 'title']


class ChildLessonsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'link', 'submit_time')
    search_fields = ['id', 'title']


class DownloadsAdmin(admin.ModelAdmin):
    readonly_fields = ['link']
    list_display = ('id', 'name', 'link', 'submit_time')
    search_fields = ['id', 'name']


class DocAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'name', 'submit_time')
    search_fields = ['id', 'title']


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'link', 'submit_time')
    search_fields = ['id', 'title']


class FrameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'submit_time')
    search_fields = ['id', 'title']

    class Media:
        js = (
            'js/editor/kindeditor-4.1.10/kindeditor-all.js',
            'js/editor/kindeditor-4.1.10/lang/zh_CN.js',
            'js/editor/kindeditor-4.1.10/config.js',
        )

admin.site.register(ParentLessons, ParentLessonsAdmin)
admin.site.register(ChildLessons, ChildLessonsAdmin)
admin.site.register(Downloads, DownloadsAdmin)
admin.site.register(Doc, DocAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Frame, FrameAdmin)
