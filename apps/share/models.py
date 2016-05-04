# coding: utf-8
from django.db import models
import os

# Create your models here.


class ParentLessons(models.Model):

    title = models.CharField(max_length=50, verbose_name=u'标题')
    image = models.ImageField(
        upload_to='images/', verbose_name=u'课程封面图', null=True
    )
    description = models.CharField(max_length=255, verbose_name=u'课程描述')
    submit_time = models.DateTimeField(auto_now_add=True, verbose_name=u"添加时间")
    update_time = models.DateTimeField(auto_now_add=True, verbose_name=u"修改时间")

    def __unicode__(self):
        return '%s' % self.title

    class Meta:
        verbose_name_plural = '主课程'


class ChildLessons(models.Model):

    parent = models.ForeignKey(ParentLessons)
    title = models.CharField(max_length=50, verbose_name=u'标题')
    link = models.CharField(max_length=255, verbose_name=u'网课链接')
    submit_time = models.DateTimeField(auto_now_add=True, verbose_name=u"添加时间")
    update_time = models.DateTimeField(auto_now_add=True, verbose_name=u"修改时间")

    def __unicode__(self):
        return '%s' % self.title

    class Meta:
        verbose_name_plural = '子课程'


class Downloads(models.Model):
    title = models.CharField(max_length=50, verbose_name=u'文件标题')
    name = models.FileField(
        upload_to='downloads/',
        max_length=255, blank=False
    )
    link = models.CharField(max_length=255, blank=True)
    submit_time = models.DateTimeField(auto_now_add=True, verbose_name=u"添加时间")
    update_time = models.DateTimeField(auto_now_add=True, verbose_name=u"修改时间")

    def __unicode__(self):
        return '%s' % self.name

    def save(self, *args, **kwargs):
        super(self.__class__, self).save(*args, **kwargs)
        Downloads.objects.filter(id=self.id).update(
            link=os.path.join('/media', self.name.name)
        )

    class Meta:
        verbose_name_plural = '常用下载'


class Exercise(models.Model):
    title = models.CharField(max_length=50, verbose_name=u'视频标题')
    image = models.ImageField(
        upload_to='images/', verbose_name=u'视频封面图', null=True
    )
    description = models.CharField(max_length=255, verbose_name=u'视频描述')
    link = models.CharField(
        max_length=255, blank=True, null=False, verbose_name=u'视频链接'
    )
    submit_time = models.DateTimeField(auto_now_add=True, verbose_name=u"添加时间")

    def __unicode__(self):
        return '%s' % self.title

    class Meta:
        verbose_name_plural = '实践风采'


class Doc(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'资料标题')
    name = models.FileField(
        upload_to='downloads/',
        max_length=255, blank=False
    )
    submit_time = models.DateTimeField(auto_now_add=True, verbose_name=u"添加时间")

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        verbose_name_plural = '支教资料库'


class Frame(models.Model):
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

    class Meta:
        verbose_name_plural = '课程框架'
