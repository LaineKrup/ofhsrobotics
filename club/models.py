from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    likes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Resource(models.Model):
    CATEGORY_CHOICES = [
        ('students', 'For Students'),
        ('ideas', 'Project Ideas'),
        ('tools', 'Engineering Tools'),
        ('cs', 'CS Resources'),
    ]

    title = models.CharField(max_length=200)
    url = models.URLField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self) -> str:
        return f'{self.get_category_display()}: {self.title}'


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Contact from {self.name} at {self.sent_at:%Y-%m-%d %H:%M:%S}'
