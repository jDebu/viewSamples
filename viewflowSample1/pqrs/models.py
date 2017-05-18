from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from .managers import UserManager
from django.core.mail import send_mail


class Customers(AbstractBaseUser, PermissionsMixin):
    doc_type= models.CharField(_('tipo documento'),choices=(
        (1,'CODIGO'),
        (2,'DNI')
    ),max_length=1)
    doc_num= models.CharField(_('n° documento'),max_length=20)
    email = models.EmailField(_('correo'),max_length=50 ,unique=True)
    first_name = models.CharField(_('nombres'), max_length=100, blank=True)
    last_name = models.CharField(_('apellidos'), max_length=100, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('activo'), default=True)
    is_staff = models.BooleanField(_('personal'),default=False)
    #avatar = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    #phone_num=ArrayField(models.CharField(max_length=15), blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('cliente')
        verbose_name_plural = _('cliente')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Test(models.Model):
    texto=models.CharField(max_length=30)

