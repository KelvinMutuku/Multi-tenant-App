from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from tenant_users.tenants.models import TenantBase, UserProfile

from core.models import TimeStampedModel


class Client(TenantMixin): # <--- Is it named 'Client'?
    name = models.CharField(max_length=100)
    paid_until = models.DateField()
    on_trial = models.BooleanField(default=True)
    created_on = models.DateField(auto_now_add=True)
    
class User(UserProfile):
    pass


class Tenant(TenantBase, TimeStampedModel):
    name = models.CharField(max_length=100)


class Domain(DomainMixin, TimeStampedModel):
    pass
