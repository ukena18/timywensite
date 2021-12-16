from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=200)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=200)
    body_text = models.TextField()
    pub_date = models.DateTimeField()
    mod_date = models.DateTimeField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks= models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline


# creating an object
b = Blog(name="Beatles",tagline="all the songs")
b.save()

# if you want to do change in the existing database
b.name="queeens"
b.save()
# let say we crated an entry
entry = Entry.objects.get(pk=1)
cheese_blog = Blog.objects.get(name="cheese")
entry.blog = cheese_blog
entry.save()
# for manytomany relationship you can add author to entry
joe = Author.objects.create(name="joe")
entry.authors.add(joe)


# Retrieving objects >queryset
Blog.objects.all()
all_entries = Entry.objects.all()

# chaining filters






