from django import forms
from django.core.exceptions import ValidationError
from .models import Student


class ScoreLookupForm(forms.Form):
    """Form for looking up student scores by registration number"""
    sbd = forms.CharField(
        max_length=8,
        label="Registration Number (SBD)",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter registration number (e.g., 01000001)',
            'pattern': '[0-9]{8}',
            'title': 'Please enter an 8-digit registration number'
        }),
        help_text="Enter your 8-digit registration number"
    )
    
    def clean_sbd(self):
        sbd = self.cleaned_data['sbd']
        
        # Check if SBD is exactly 8 digits
        if not sbd.isdigit() or len(sbd) != 8:
            raise ValidationError("Registration number must be exactly 8 digits.")
        
        return sbd


class SubjectFilterForm(forms.Form):
    """Form for filtering statistics by subject"""
    SUBJECT_CHOICES = [
        ('', 'All Subjects'),
        ('toan', 'Toán'),
        ('ngu_van', 'Ngữ Văn'),
        ('ngoai_ngu', 'Ngoại Ngữ'),
        ('vat_li', 'Vật Lý'),
        ('hoa_hoc', 'Hóa Học'),
        ('sinh_hoc', 'Sinh Học'),
        ('lich_su', 'Lịch Sử'),
        ('dia_li', 'Địa Lý'),
        ('gdcd', 'GDCD'),
    ]
    
    subject = forms.ChoiceField(
        choices=SUBJECT_CHOICES,
        required=False,
        label="Subject",
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )