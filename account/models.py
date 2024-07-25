from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_student = models.BooleanField('Is student', default=False)
    is_employee = models.BooleanField('Is employee', default=False)
    
    
# class Course(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     syllabus = models.TextField()
#     instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class StudentRegistration(models.Model):
    FULL_NAME_MAX_LENGTH = 100
    PHONE_NUMBER_MAX_LENGTH = 15

    email = models.EmailField()
    full_name = models.CharField(max_length=FULL_NAME_MAX_LENGTH)
    date_of_birth = models.DateField()
    school = models.CharField(max_length=FULL_NAME_MAX_LENGTH)
    residence = models.CharField(max_length=FULL_NAME_MAX_LENGTH)
    grade = models.CharField(max_length=FULL_NAME_MAX_LENGTH)
    student_phone = models.CharField(max_length=PHONE_NUMBER_MAX_LENGTH, blank=True, null=True)
    code_camp = models.CharField(max_length=50, choices=[
        ('Form 6 Vacationers Code Camp (Mar - July)', 'Form 6 Vacationers Code Camp (Mar - July)'),
        ('51st Code Camp (MAY)', '51st Code Camp (MAY)'),
        ('Private Class', 'Private Class'),
        ('Easter Break Code Camp', 'Easter Break Code Camp'),
        ('Artificial Intelligence (Saturdays)', 'Artificial Intelligence (Saturdays)'),
        ('Summer Code Camp', 'Summer Code Camp'),
    ])
    mode_of_school = models.CharField(max_length=50, choices=[
        ('Day', 'Day'),
        ('Boarding', 'Boarding'),
    ])
    type_of_school = models.CharField(max_length=50, choices=[
        ('National', 'National'),
        ('International', 'International'),
        ('Semi-International', 'Semi-International'),
    ])
    course_module = models.CharField(max_length=50, choices=[
        ("Scratch Beginners", "Scratch Beginners"),
        ("2D Game Dev't with Scratch", "2D Game Dev't with Scratch"),
        ("Python Beginners", "Python Beginners"),
    ])
    preferred_class_type = models.CharField(max_length=50, choices=[
        ("Private Physical at the Client's home", "Private Physical at the Client's home"),
        ("Private Physical at Academy Offices", "Private Physical at Academy Offices"),
        ("Private Online (Via Zoom)", "Private Online (Via Zoom)"),
        ("General Physical (ICT House)", "General Physical (ICT House)"),
        ("General online (via Zoom)", "General online (via Zoom)"),
    ])
    next_term_start = models.DateField()
    parent_full_name = models.CharField(max_length=FULL_NAME_MAX_LENGTH)
    parent_title = models.CharField(max_length=10, choices=[
        ("Mr.", "Mr."),
        ("Mrs.", "Mrs."),
        ("Ms.", "Ms."),
        ("Miss.", "Miss."),
    ])
    parent_phone = models.CharField(max_length=PHONE_NUMBER_MAX_LENGTH)
    parent_occupation = models.CharField(max_length=FULL_NAME_MAX_LENGTH)
    referral_source = models.CharField(max_length=50, choices=[
        ("A Friend", "A Friend"),
        ("Twitter", "Twitter"),
        ("Facebook", "Facebook"),
        ("Instagram", "Instagram"),
        ("LinkedIn", "LinkedIn"),
        ("WhatsApp", "WhatsApp"),
        ("Google Search", "Google Search"),
        ("Youtube", "Youtube"),
        ("TikTok", "TikTok"),
        ("From School", "From School"),
        ("National Science Week 2023", "National Science Week 2023"),
        ("Other", "Other"),
    ])
    referral_detail = models.CharField(max_length=FULL_NAME_MAX_LENGTH, blank=True, null=True)
    agree_to_terms = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
    






class AdultRegistration(models.Model):
    FULL_NAME_MAX_LENGTH = 100
    PHONE_NUMBER_MAX_LENGTH = 15

    name = models.CharField(max_length=FULL_NAME_MAX_LENGTH)
    email = models.EmailField()
    contact = models.CharField(max_length=PHONE_NUMBER_MAX_LENGTH)
    class_type = models.CharField(max_length=50, choices=[
        ("Physical", "Physical"),
        ("Online via Zoom", "Online via Zoom"),
    ])
    class_time_slots = models.CharField(max_length=50, choices=[
        ("Weekly", "Weekly"),
        ("Weekend", "Weekend"),
    ])
    preferred_start_date = models.DateField()
    employer_name = models.CharField(max_length=FULL_NAME_MAX_LENGTH)
    position_at_work = models.CharField(max_length=FULL_NAME_MAX_LENGTH)
    owns_laptop = models.CharField(max_length=3, choices=[
        ("Yes", "Yes"),
        ("No", "No"),
    ])
    address = models.CharField(max_length=FULL_NAME_MAX_LENGTH)
    course_module = models.CharField(max_length=50, choices=[
        ("ICDL", "ICDL"),
        ("Web design (HTML, CSS, JS)", "Web design (HTML, CSS, JS)"),
        ("Web development with Python Django", "Web development with Python Django"),
    ])
    referral_source = models.CharField(max_length=50, choices=[
        ("A Friend", "A Friend"),
        ("Twitter", "Twitter"),
        ("Facebook", "Facebook"),
        ("Instagram", "Instagram"),
        ("LinkedIn", "LinkedIn"),
        ("WhatsApp", "WhatsApp"),
        ("Google Search", "Google Search"),
        ("Youtube", "Youtube"),
        ("TikTok", "TikTok"),
        ("From School", "From School"),
        ("National Science Week 2023", "National Science Week 2023"),
        ("Other", "Other"),
    ])
    referral_detail = models.CharField(max_length=FULL_NAME_MAX_LENGTH, blank=True, null=True)
    agree_to_terms = models.BooleanField(default=False)

    def __str__(self):
        return self.name    

