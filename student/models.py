# coding=utf-8

from django.db                  import models
from django.contrib.auth.models import User


GRADE = (
    ("5",  "5 класс"),
    ("6",  "6 класс"),
    ("7",  "7 класс"),
    ("8",  "8 класс"),
    ("9",  "9 класс"),
    ("10", "10 класс"),
    ("11", "11 класс"),
)

LETTER = (
    ("A",  "а"),
    ("B",  "б"),
)

SEX = (
		("M", "мужской"),
		("F", "женский"),
)

GTO = (
        ("1", "Зачет"),
        ("2", "Бронза"),
        ("3", "Серебро"),
        ("4", "Золото"),
        ("5", "Участие"),
)

CONF_SECTION = (
        ("INF", "Информатика"),
        ("MAT", "Математика"),
        # TODO: add others
)

SUBJECT = (
        ("MA", "математика"),
        ("CS", "информатика и ИКТ"),
        ("PH", "физика"),
        ("CH", "чимия"),
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

SPORT_SECTIONS = (
        ("ATH", "Легкая атлетика"),
        # TODO: add others
)

LEVEL = (
        ("1", "Школьный"),
        ("2", "Кустовой"),
        ("3", "Районный"),
        ("4", "Региональный"),
        ("5", "Республиканский"),
        ("6", "Всероссийский"),
        ("7", "Международный"),
)

CONF_RESULT = (
        ("1", "Лауреат"),
        ("2", "Дипломант 1 степени"),
        ("3", "Дипломант 2 степени"),
        ("4", "Дипломант 3 степени"),
)

OLYMP_RESULT = (
        ("1", "Первое место"),
        ("2", "Второе место"),
        ("3", "Третье место"),
)

SPORT_RESULT = (
        ("1", "Первое место"),
        ("2", "Второе место"),
        ("3", "Третье место"),
)

class Family(models.Model):
    momname    = models.CharField(max_length = 50)
    momwork    = models.CharField(max_length = 50)
    dadname    = models.CharField(max_length = 50)
    dadwork    = models.CharField(max_length = 50)
    childcount = models.CharField(max_length = 50)
    minorcount = models.CharField(max_length = 50)
    traditions = models.CharField(max_length = 50)

    def __unicode__(self):
		return self.momname

class ActivityOptions(models.Model):
    ntl     = models.BooleanField(default = False)
    cdntt   = models.BooleanField(default = False)
    cdod    = models.BooleanField(default = False)
    dyush   = models.BooleanField(default = False)
    ndshi   = models.BooleanField(default = False)
    kytalyk = models.BooleanField(default = False)
    custom  = models.CharField(max_length = 100)
    
    def __unicode__(self):
		return 'ActivityOptions'
		
class HobbyOptions(models.Model):
    reading   = models.BooleanField(default = False)
    science   = models.BooleanField(default = False)
    painting  = models.BooleanField(default = False)
    sport     = models.BooleanField(default = False)
    hunting   = models.BooleanField(default = False)
    cooking   = models.BooleanField(default = False)
    tecnology = models.BooleanField(default = False)
    art       = models.BooleanField(default = False)
    photo     = models.BooleanField(default = False)
    custom    = models.CharField(max_length = 100)
    
    def __unicode__(self):
		return 'HobbyOptions'

class OlympResult(models.Model):
    subject = models.CharField(max_length = 2, choices = SUBJECT)
    level   = models.CharField(max_length = 1, choices = LEVEL)
    result  = models.CharField(max_length = 1, choices = OLYMP_RESULT)
    
    def __unicode__(self):
		return 'OlympResult'

class ConferenceResult(models.Model):
    level   = models.CharField(max_length = 1, choices = LEVEL)
    section = models.CharField(max_length = 3, choices = CONF_SECTION)
    name    = models.CharField(max_length = 50)
    adviser = models.CharField(max_length = 50)
    result  = models.CharField(max_length = 1, choices = CONF_RESULT)
    
    def __unicode__(self):
		return 'ConferenceResult'

class SportSectionOptions(models.Model):
    athletics     = models.BooleanField(default = False)
    weightlifting = models.BooleanField(default = False)
    volleyball    = models.BooleanField(default = False)
    basketball    = models.BooleanField(default = False)
    football      = models.BooleanField(default = False)
    tennis        = models.BooleanField(default = False)
    national      = models.BooleanField(default = False)
    fitness       = models.BooleanField(default = False)
    judo          = models.BooleanField(default = False)
    box           = models.BooleanField(default = False)
    custom        = models.CharField(max_length = 100)
    
    def __unicode__(self):
		return 'SportSectionOptions'

class SportCompetitionResult(models.Model):
    name    = models.CharField(max_length = 20)
    section = models.CharField(max_length = 3, choices = SPORT_SECTIONS)
    trainer = models.CharField(max_length = 20)
    result  = models.CharField(max_length = 1, choices = SPORT_RESULT)
    
    def __unicode__(self):
		return 'SportCompetitionResult'

class StudentProfile(models.Model):
    user                      = models.OneToOneField(User, related_name = "student_profile")
    name                      = models.CharField(max_length = 100)
    grade                     = models.CharField(max_length = 2, choices = GRADE,blank = True)
    letter                    = models.CharField(max_length = 1, choices = LETTER,blank = True)
    avatar                    = models.ImageField(upload_to = "images", blank = True, null = True)
    birthdate                 = models.DateField(null = True, blank = True)
    address                   = models.CharField(max_length = 100,blank = True)
    sex                       = models.CharField(max_length = 1, choices = SEX,blank = True)
    activity_options          = models.OneToOneField(ActivityOptions, blank = True, null = True)
    family                    = models.OneToOneField(Family, blank = True, null = True)
    hobby_options             = models.OneToOneField(HobbyOptions, blank = True, null = True)
    olymp_results             = models.ForeignKey(OlympResult, blank = True, null = True)
    conference_results        = models.ForeignKey(ConferenceResult, blank = True, null = True)
    sport_section_options     = models.ForeignKey(SportSectionOptions, blank = True, null = True)
    sport_competition_results = models.ForeignKey(SportCompetitionResult, blank = True, null = True)
    my_success                = models.CharField(max_length = 500,blank = True)
    gto                       = models.CharField(max_length = 1, choices = GTO,blank = True)
    sections                  = models.CharField(max_length = 50,blank = True)
    verified                  = models.BooleanField(default = False,blank = True)
    
    def __unicode__(self):
        return str(self.user)
