from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):  # __unicode__ on Python 2
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):  # __unicode__ on Python 2
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):  # __unicode__ on Python 2
        return self.headline


class Answer(models.Model):
    from_q = models.ForeignKey('Question', related_name='rel_q')
    to_q = models.ForeignKey('Question')
    entry = models.CharField(max_length=100)

    def __str__(self):  # __unicode__ on Python 2
        return self.entry


class Question(models.Model):
    rel = models.ManyToManyField('self', blank=True, through=Answer, symmetrical=False)
    entry = models.CharField(max_length=100)

    def __str__(self):  # __unicode__ on Python 2
        return self.entry
