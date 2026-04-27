from django.db import models


class HabitGroup(models.Model):
    name  = models.CharField(max_length=100)
    icon  = models.CharField(max_length=10, default='📌')
    color = models.CharField(max_length=20, default='#2ecc71')
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'created_at']

    def __str__(self):
        return f"{self.icon} {self.name}"


class Todo(models.Model):
    group = models.ForeignKey(HabitGroup, on_delete=models.CASCADE, related_name='todos')
    text  = models.CharField(max_length=300)
    done  = models.BooleanField(default=False)
    memo  = models.TextField(blank=True, default='')
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'created_at']

    def __str__(self):
        return self.text
