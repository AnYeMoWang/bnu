from django.contrib import admin
from .models import Trade


class TradeAdmin(admin.ModelAdmin):
    readonly_fields = ['view_count']
    list_display = ('id', 'title', 'submit_time', 'update_time')
    search_fields = ['id', 'title']

    class Media:
        js = (
            'js/editor/kindeditor-4.1.10/kindeditor-all.js',
            'js/editor/kindeditor-4.1.10/lang/zh_CN.js',
            'js/editor/kindeditor-4.1.10/config.js',
        )


admin.site.register(Trade, TradeAdmin)
