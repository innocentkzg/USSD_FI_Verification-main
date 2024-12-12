from django.db import models

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    roleid = models.AutoField(primary_key=True)
    rolename = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.rolename




# Institution Model
class Institution(models.Model):
    tin = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ('Licensed', 'Licensed'),
        ('Revoked', 'Revoked'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    description = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name

    
# User Model
class User(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True)
    
    # Foreign keys to Category and Role
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
