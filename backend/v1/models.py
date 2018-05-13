from django.db import models


class Author(models.Model):
    MAN = 0
    WOMAN = 1
    GENDER_CHOICES = (
        (MAN, "man"),
        (WOMAN, "woman")
    )
    name = models.CharField(max_length=31)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    description = models.TextField("自己紹介文")

    def __str__(self):
        return "{0.id} {0.name}".format(self)


class Tag(models.Model):
    """
    記事に対するタグ
    """

    name = models.CharField(max_length=31)


class Article(models.Model):
    author = models.ForeignKey(Author, models.SET_NULL, null=True)
    title = models.CharField(max_length=511)
    body = models.TextField("本文")
    main_image = models.ImageField(null=True)

