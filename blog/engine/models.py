from django.db import models


class Tag(models.Model):
    """
    Class provides model for Tag entity.
    Attributes:
        title: str - contains comment text
    """

    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Post(models.Model):
    """
    Class provides model for Post entity.
    Attributes:
        title: str - post topic text
        post_date: datetime - time of post creation
        text: str - post full text
        tags: inner key to Tag model, tags connected to post
    """

    title = models.CharField(max_length=150)
    post_date = models.DateTimeField(auto_now=True)
    text = models.TextField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Class provides model for Comment entity.
    Attributes:
        post: inner key to Post model, post connected to post
        text: str - comment full text
        created: datetime - time of comment creation
    """

    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Class provides sorting of comments by created field value
        """

        ordering = ('created',)

    def __str__(self):
        return '{} / {}'.format(self.post, self.created)
