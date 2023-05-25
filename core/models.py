import uuid
from django.db import models
from stdimage.models import StdImageField

#Função para imagens
def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename =  f'{uuid.uuid4()}.{ext}'
    return filename
class Base(models.Model):
    created = models.DateField('Creation', auto_now_add=True)
    modified = models.DateField('Modification', auto_now=True)
    active = models.BooleanField('Active?', default=True)

    class Meta:
        abstract = True

class Service(Base):
    ICON_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foquete'),
    )
    service = models.CharField('Service', max_length=50)
    description = models.TextField('Description', max_length=200)
    icon = models.CharField('Icon', max_length=12, choices=ICON_CHOICES)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.service

class JobTitle(Base):
    job_title = models.CharField('JobTitle', max_length=60)

    class Meta:
        verbose_name = 'Job Title'
        verbose_name_plural = 'Jobs Title'
        
    def __str__(self):
        return self.job_title

class Employee(Base):
    name = models.CharField('Name', max_length=70)
    job_title = models.ForeignKey('core.JobTitle', verbose_name='Job Title', on_delete=models.CASCADE)
    bio = models.CharField('Bio', max_length=200)
    image = StdImageField('Image',  upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop':True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')
    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Team'
    def __str__(self):
        return self.name

