from django.db import models


class JobType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class ApplicationStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class ContractType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class ContractTime(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
