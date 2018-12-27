from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField('Nome', max_length=100)
    cpf_cnpj = models.CharField('CPF/CNPJ', max_length=18, unique=True)
    def __str__(self):
        return self.name

class Receipt(models.Model):
    person = models.ForeignKey('core.Person', related_name='person_item', on_delete=models.CASCADE,
                               verbose_name='Cliente')
    data=models.DateTimeField(auto_now=True)

