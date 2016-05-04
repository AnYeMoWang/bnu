# coding: utf-8
from django.db import models


class Practice(models.Model):
    type_choices = (
        (0, u'全部'),
        (1, u'弘文励教'),
        (2, u'社会观察'),
        (3, u'美丽中国'),
        (4, u'职涯体验'),
        (5, u'铭记历史'),
    )
    type = models.IntegerField(
        choices=type_choices, default=0, verbose_name=u'分类'
    )
    title = models.CharField(max_length=50, verbose_name=u'标题')
    content = models.TextField(verbose_name=u'正文内容')
    submit_time = models.DateTimeField(auto_now_add=True, verbose_name=u"添加时间")
    update_time = models.DateTimeField(auto_now_add=True, verbose_name=u"修改时间")
    view_count = models.IntegerField(default=0, verbose_name=u'浏览次数')

    def __unicode__(self):
        return '%s' % self.type

    def get_preview(self):
        return '</p>'.join(self.content.split('</p>')[:3]) + '</p>'

    def has_viewed(self):
        self.view_count += 1
        self.save()

    class Meta:
        verbose_name_plural = '实践内容'
