from django.db import models


class SearchList(models.Model):
    title = models.CharField('책 제목', max_length=100)
    author = models.CharField('글쓴이', max_length=25)
    publisher = models.CharField('출판사', max_length=25)
    date = models.CharField('출판일', max_length=15)
    url = models.CharField('URL', max_length=200)
    updated = models.CharField('수정일', max_length=15)

    def __str__(self):
        return self.title
