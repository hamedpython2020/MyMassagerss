from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from account.models import Profile

class Post(models.Model):
    class Meta:
        verbose_name = 'مطلب'
        verbose_name_plural = 'مطالب'
        pass

    prof = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='کاربر')

    def get_name(self):
        user = self.prof.user
        name = user.get_full_name()
        return name
    data = models.FileField(verbose_name='محتوا', upload_to='posts/%Y-%d-%m', null=True, blank=True , )
    caption = models.TextField('توضیح', null=True, blank=True)
    share_date = models.DateTimeField('زمان انتشار', auto_now_add=True, null=False)
    views = models.IntegerField("بازدید", default=1)
    like = models.IntegerField("پسندیده", default=0)
    title = models.CharField('موضوع', null=False, max_length=50)

    def __str__(self):
        return 'prof_id : {} -make- post : ({}) '.format(self.prof.id, self.title)

    def add_view(self):
        self.views += 1
        self.save()
        return self.views

    def add_like(self):
        self.like += 1
        self.save()
        return self.like
    pass

#####################################


class viewer(models.Model):
    class Meta:
        verbose_name = 'بیننده'
        verbose_name_plural = 'بیننده ها'
        pass
    view_date = models.DateField('تاریخ دیده شدن', auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='محتوا', null=False)
    prof = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='بیننده', null=False)
    comment = models.TextField('نظر', null=True, blank=True)

    def __str__(self):
        return 'prof_id : {} -view- post_id : {}'.format(self.prof.id, self.post.id)

####################################

