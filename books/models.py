from django.db import models

# Create your models here.
class Book(models.Model):
    STATUS_CHOICES = [
        ('Published', 'Published'),
        ('Unpublished', 'Unpublished'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
    ]
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    language = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    image = models.ImageField(upload_to='book_images/', null=True, blank=True)
    added_by = models.ForeignKey('members.AuthUser', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    STATUS_CHOICES = [
        ('Published', 'Published'),
        ('Unpublished', 'Unpublished'),
        ('Pending', 'Pending'),
        ('Banned', 'Banned'),
    ]
    review = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    added_by = models.ForeignKey('members.AuthUser', on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)