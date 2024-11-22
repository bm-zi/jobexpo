from django.db import models
from .locations import Location
from .companies import Company
from .tags import Tag, Benefit, Skill
from .contacts import Contact
from .contracts import JobType, ApplicationStatus, ContractType, ContractTime


class Job(models.Model):
    job_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Tag, related_name='category_jobs',on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()

    # Normalized fields
    job_type = models.ForeignKey(JobType, on_delete=models.SET_NULL, null=True, blank=True)
    application_status = models.ForeignKey(ApplicationStatus, on_delete=models.SET_NULL, null=True, blank=True)
    contract_type = models.ForeignKey(ContractType, on_delete=models.SET_NULL, null=True, blank=True)
    contract_time = models.ForeignKey(ContractTime, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='tagged_jobs',blank=True)
    benefits = models.ManyToManyField(Benefit, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)

    # Additional fields
    application_deadline = models.DateField(null=True, blank=True)
    required_experience = models.IntegerField(null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    priority = models.IntegerField(null=True, blank=True)
    hiring_manager = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True, blank=True)
    favorite = models.BooleanField(default=False)
    image = models.ImageField(upload_to='job_images/', null=True, blank=True)
    redirect_url = models.URLField()
    application_count = models.PositiveIntegerField(default=0)
    posted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Job"
        verbose_name_plural = "Jobs"
        ordering = ["-posted_at"]

    def __str__(self):
        return f"{self.title} at {self.company} ({self.location})"
