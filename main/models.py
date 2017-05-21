from django.db import models
from django.utils import timezone

class Position(models.Model):
    name = models.CharField('Наименование', max_length=40)
    def __str__(self):
        return self.name
    class Meta:
        managed = False
        db_table = 'position'
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

class Department(models.Model):
    name = models.CharField('Наименование', max_length=40)
    def __str__(self):
        return self.name
    class Meta:
        managed = False
        db_table = 'department'
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

class Employee(models.Model):
    first_name = models.CharField('Имя', max_length=40)
    second_name = models.CharField('Фамилия', max_length=40)
    birthday = models.DateField('Дата рождения')
    email = models.CharField('Email', max_length=40)
    start_date = models.DateField('Дата начала работы', default=timezone.now)
    finish_date = models.DateField('Дата окончания работы', blank=True, null=True)
    position = models.ForeignKey('Position', on_delete=models.DO_NOTHING, verbose_name='Должность')
    department = models.ForeignKey('Department', on_delete=models.DO_NOTHING, verbose_name='Отдел')
    def __str__(self):
        return self.first_name + ' ' + self.second_name
    class Meta:
        managed = False
        db_table = 'employee'
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
