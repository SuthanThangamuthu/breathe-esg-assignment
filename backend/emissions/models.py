from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class DataSource(models.Model):

    SOURCE_TYPES = [
        ('SAP', 'SAP'),
        ('UTILITY', 'Utility'),
        ('TRAVEL', 'Travel'),
    ]

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )

    source_type = models.CharField(
        max_length=20,
        choices=SOURCE_TYPES
    )

    uploaded_file = models.FileField(
        upload_to='uploads/'
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.company.name} - {self.source_type}"


class EmissionRecord(models.Model):

    CATEGORY_CHOICES = [
        ('SCOPE1', 'Scope 1'),
        ('SCOPE2', 'Scope 2'),
        ('SCOPE3', 'Scope 3'),
    ]

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )

    source = models.ForeignKey(
        DataSource,
        on_delete=models.CASCADE
    )

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    record_type = models.CharField(
        max_length=100
    )

    raw_value = models.FloatField()

    raw_unit = models.CharField(
        max_length=50
    )

    normalized_value = models.FloatField()

    normalized_unit = models.CharField(
        max_length=50
    )

    is_suspicious = models.BooleanField(
        default=False
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.record_type} - {self.company.name}"


class AuditLog(models.Model):

    ACTION_CHOICES = [
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
        ('EDITED', 'Edited'),
    ]

    record = models.ForeignKey(
        EmissionRecord,
        on_delete=models.CASCADE
    )

    action = models.CharField(
        max_length=20,
        choices=ACTION_CHOICES
    )

    performed_by = models.CharField(
        max_length=255
    )

    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    notes = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.action} - {self.record.id}"