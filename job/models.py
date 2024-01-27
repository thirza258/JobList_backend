from django.db import models
import os

def lowercase_filename(instance, filename):
    # Get the file extension
    ext = filename.split('.')[-1]

    # Generate a new filename in lowercase
    new_filename = f"{instance.logo_name.lower()}.{ext}"

    # Return the new path
    return os.path.join('app/src/main/res/drawable', new_filename)

# Create your models here.
class Job(models.Model):
    logo = models.ImageField(upload_to=lowercase_filename, null=True, blank=True)
    logo_name = models.CharField(max_length=100, null=True, blank=True)
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    job_description = models.TextField()
    salary = models.IntegerField()
    location = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    job_type = models.CharField(max_length=100)
    work_hours = models.IntegerField()
    status = models.CharField(max_length=100, null=True, blank=True, choices=[('open', 'Open'), ('closed', 'Closed')])
    new = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    link = models.CharField(max_length=100, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        # Convert logo_name to lowercase before saving
        if self.logo_name:
            self.logo_name = self.logo_name.lower()

        # Call the original save method
        super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.company_name

class Requirement(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    requirement = models.CharField(max_length=100)

    def __str__(self):
        return self.requirement