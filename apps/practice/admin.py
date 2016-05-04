from django.contrib import admin
from .models import Practice


class PracticeAdmin(admin.ModelAdmin):
    readonly_fields = ['view_count']
    list_display = ('type', 'title')
    search_fields = ['title', 'content']

    class Media:
        js = (
            'js/editor/kindeditor-4.1.10/kindeditor-all.js',
            'js/editor/kindeditor-4.1.10/lang/zh_CN.js',
            'js/editor/kindeditor-4.1.10/config.js',
        )


admin.site.register(Practice, PracticeAdmin)
