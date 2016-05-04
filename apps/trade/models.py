# coding: utf-8
from django.db import models


class Trade(models.Model):
    type_choices = (
        (1, u'新闻'),
        (2, u'公告'),
    )
    type = models.IntegerField(
        choices=type_choices, default=1, verbose_name=u'分类'
    )
    title = models.CharField(max_length=50, verbose_name=u'标题')
    content = models.TextField(verbose_name=u'正文内容')
    submit_time = models.DateTimeField(auto_now_add=True, verbose_name=u"添加时间")
    update_time = models.DateTimeField(auto_now_add=True, verbose_name=u"修改时间")
    view_count = models.IntegerField(default=0, verbose_name=u'浏览次数')

    def __unicode__(self):
        return '%s' % self.title

    def get_preview(self):
        return '</p>'.join(self.content.split('</p>')[:3]) + '</p>'

    def has_viewed(self):
        self.view_count += 1
        self.save()

    def get_first_img(self):
        if self.content.startswith('<img'):
            return self.content.split('src="')[1].split('"')[0]
        imgs = self.content.split('<img')
        if len(imgs) == 1:
            return None
        return imgs[1].split('src="')[1].split('"')[0]

    def get_first_content(self):
        ps = self.content.split('<p')
        if len(ps) == 1:
            return None
        return ''.join([p.split('</p>')[0][p.index('>') + 1:] for p in ps[1:]])

    class Meta:
        verbose_name_plural = '新闻/公告'
