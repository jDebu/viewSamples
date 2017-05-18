from django.contrib.auth.models import User
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from viewflow.models import Process

# Create your models here.
class Customer(models.Model):
    doc_type= models.CharField(_('tipo documento'),choices=(
        ('1','CODIGO'),
        ('2','DNI')
    ),max_length=1)
    doc_num= models.CharField(_('n° documento'),max_length=20,unique=True)
    email = models.EmailField(_('correo'),max_length=50 ,blank=True)
    first_name = models.CharField(_('nombres'), max_length=100, blank=True,null=True)
    last_name = models.CharField(_('apellidos'), max_length=100, blank=True)
    created_at = models.DateTimeField(_('creado'),auto_now_add=True)
    #avatar = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    #phone_num=ArrayField(models.CharField(max_length=15), blank=True)

    class Meta:
        verbose_name = _('usuario')
        verbose_name_plural = _('usuarios')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

class Claim(models.Model):
    customer=models.ForeignKey(Customer)
    reception_mean=models.IntegerField(_('medio'),choices=(
        (1,'Telefono'),
        (2,'correo')
    ))
    type=models.IntegerField(_('tipo'),choices=(
        (1,'Peticion'),
        (2,'Quejas'),
        (3,'Reclamos'),
        (4,'Sugerencias')
    ))
    cause=models.CharField(_('causa'),max_length=100)
    description=models.CharField(_('descripcion'),max_length=200,blank=True)
    #case_field=models.ImageField(_('archivo'),upload_to=user_directory_path,null=True,blank=True)
    inmediate_solution = models.BooleanField(_('solucion inmediata'),choices=(
        (True, 'Yes'),
        (False, 'No')
    ))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    taken_by = models.ForeignKey(User)

class ClaimProcess(Process):
    claim=models.ForeignKey(Claim)

    @property
    def pqr_required(self):
        return (self.claim.claim.type == 1 or
                self.claim.claim.type == 2 or
                self.claim.claim.type == 3)
    @property
    def s_required(self):
        return self.claim.claim.type == 4