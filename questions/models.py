from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name='topics'
    )

    def __str__(self):
        return self.name


class Question(models.Model):

    DIFFICULTY_LEVELS = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    text = models.TextField()
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name='questions'

    )

    difficulty = models.CharField(
        max_length=10,
        choices=DIFFICULTY_LEVELS,
        default='medium'
    )

    def __str__(self):
        return self.text[:80]


class Choice(models.Model):
    is_correct = models.BooleanField(default=False)
    text = models.TextField()
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='choices'

    )

    def __str__(self) -> str:
        return self.text[:80]
