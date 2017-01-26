# coding=utf-8

from django.db                  import models
from django.contrib.auth.models import User


SEX = (
    ("M", "мужской"),
    ("F", "женский"),
)

POSITION = (
    ("TE", "учитель"),
    ("TS", "педагог дополнительного образования"),
    ("TP", "педагог-психолог"),
    ("TB", "педагог-библиотекарь"),
    ("MP", "МПО"),
    ("HO", "РДО"),
    ("ST", "социальный педагог"),
)

QUALIFICATION = (
    ("NO", "нет категории"),
    ("BA", "соответствие занимаемой должности"),
    ("FI", "первая категория"),
    ("HI", "высшая категория"),
)

SUBJECT = (
    ("MA", "математика"),
    ("CS", "информатика и ИКТ"),
    ("PH", "физика"),
    ("CH", "химия"),
    ("BI", "биология"),
    ("GE", "география"),
    ("RL", "русский язык и литература"),
    ("SL", "якутский язык и литература"),
    ("FL", "иностранный язык"),
    ("HI", "история"),
    ("SS", "обществознание"),
    ("MU", "музыка и искусство"),
    ("DR", "ИЗО и черчение"),
    ("TE", "технология"),
    ("LS", "ОБЖ"),
    ("PC", "физкультура"),
    ("AU", "автодело"),
    ("CU", "КНРС(Я)"),
)

EDUCATION = (
    ("SE", "среднее (полное) общее"),
    ("TF", "начальное профессиональное"),
    ("TS", "среднее профессиональное"),
    ("HE", "высшее профессиональное"),
    ("PE", "послевузовское профессиональное"),
)

class TeacherProfile(models.Model):
    user                    = models.OneToOneField(User, related_name = "teacher_profile")
    verified                = models.BooleanField(default = False)
    name                    = models.CharField(max_length = 100)
    sex                     = models.CharField(max_length = 1, choices = SEX, blank = True)
    birthdate               = models.DateField(null = True, blank = True)
    avatar                  = models.ImageField(upload_to = 'images', blank = True)
    position                = models.CharField(max_length = 2, choices = POSITION, blank = True)
    qualification           = models.CharField(max_length = 2, choices = QUALIFICATION, blank = True)
    subject                 = models.CharField(max_length = 2, choices = SUBJECT, blank = True)
    education               = models.CharField(max_length = 2, choices = EDUCATION, blank = True)
    educational_institution = models.CharField(max_length = 100, blank = True)
    work_experience         = models.IntegerField(null = True, blank = True)
    teaching_experience     = models.IntegerField(null = True, blank = True)

    def __unicode__(self):
        return self.name
