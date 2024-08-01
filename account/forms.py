from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, StudentRegistration, AdultRegistration

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

class SignUpForm(UserCreationForm):
    USER_TYPE_CHOICES = [
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('employee', 'Employee'),
    ]
    user_type = forms.ChoiceField(
        choices=USER_TYPE_CHOICES, 
        widget=forms.RadioSelect,
        initial='student',  # default selected option
    )
    
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'user_type')

    def clean(self):
        cleaned_data = super().clean()
        user_type = cleaned_data.get("user_type")
        # You can add custom validation for the user_type if needed
        return cleaned_data

 
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from .models import User, StudentRegistration, AdultRegistration

# class LoginForm(forms.Form):
#     username = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#     password = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )

# class SignUpForm(UserCreationForm):
#     username = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#     password1 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#     password2 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#     email = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2', 'is_admin', 'is_employee', 'is_student')

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = StudentRegistration
        fields = [
            'email', 'full_name', 'date_of_birth', 'school', 'residence', 'grade', 'student_phone', 
            'code_camp', 'mode_of_school', 'type_of_school', 'course_module', 'preferred_class_type', 
            'next_term_start', 'parent_full_name', 'parent_title', 'parent_phone', 'parent_occupation', 
            'referral_source', 'referral_detail', 'agree_to_terms'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'next_term_start': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'grade': 'Class/Grade',
        }

class AdultRegistrationForm(forms.ModelForm):
    class Meta:
        model = AdultRegistration
        fields = [
            'name', 'email', 'contact', 'class_type', 'class_time_slots', 'preferred_start_date', 
            'employer_name', 'position_at_work', 'owns_laptop', 'address', 'course_module', 
            'referral_source', 'referral_detail', 'agree_to_terms'
        ]
        widgets = {
            'preferred_start_date': forms.DateInput(attrs={'type': 'date'}),
        }
