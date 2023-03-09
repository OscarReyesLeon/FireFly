from django.contrib.auth.models import User
from crum import get_current_user
from django.db import models


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    user_create = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='%(class)s_user_create')
    user_update = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='%(class)s_user_update')

    class Meta:
        abstract=True
    
    def save(self, *args, **kwargs):
        if self.pk:
            self.usuario_modificacion = get_current_user()
        else: self.usuario_creacion = get_current_user()
        for field in self._meta.fields:
            if isinstance(field, models.CharField) or isinstance(field, models.TextField):
                #Valor que se va a guardar en la base de datos, en mayúsculas
                valor = getattr(self, field.name).upper() if getattr(self, field.name) else None
                setattr(
                    self, field.name, 
                    valor
                )
        return super().save(*args, **kwargs)