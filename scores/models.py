from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class ForeignLanguage(models.Model):
    """Model for foreign language codes"""
    code = models.CharField(max_length=5, unique=True, help_text="Language code like N1, N2, etc.")
    name = models.CharField(max_length=50, help_text="Language name like English, French, etc.")
    
    def __str__(self):
        return f"{self.code} - {self.name}"
    
    class Meta:
        verbose_name = "Foreign Language"
        verbose_name_plural = "Foreign Languages"


class Subject(models.Model):
    """Model for subjects using OOP principles"""
    SUBJECT_CHOICES = [
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
    
    code = models.CharField(max_length=10, choices=SUBJECT_CHOICES, unique=True)
    name = models.CharField(max_length=50)
    is_group_a = models.BooleanField(default=False, help_text="True if subject is part of Group A")
    
    def __str__(self):
        return self.name
    
    def get_score_levels(self, score):
        """Determine score level for this subject"""
        if score is None:
            return "No score"
        if score >= 8:
            return "Excellent (>=8)"
        elif score >= 6:
            return "Good (6-8)"
        elif score >= 4:
            return "Average (4-6)"
        else:
            return "Below Average (<4)"
    
    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"


class Student(models.Model):
    """Model for student exam results"""
    sbd = models.CharField(
        max_length=8, 
        unique=True, 
        verbose_name="Registration Number",
        help_text="Student registration number (SBD)"
    )
    
    # Subject scores (nullable for students who didn't take certain subjects)
    toan = models.FloatField(
        null=True, blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        verbose_name="Toán"
    )
    ngu_van = models.FloatField(
        null=True, blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        verbose_name="Ngữ Văn"
    )
    ngoai_ngu = models.FloatField(
        null=True, blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        verbose_name="Ngoại Ngữ"
    )
    vat_li = models.FloatField(
        null=True, blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        verbose_name="Vật Lý"
    )
    hoa_hoc = models.FloatField(
        null=True, blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        verbose_name="Hóa Học"
    )
    sinh_hoc = models.FloatField(
        null=True, blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        verbose_name="Sinh Học"
    )
    lich_su = models.FloatField(
        null=True, blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        verbose_name="Lịch Sử"
    )
    dia_li = models.FloatField(
        null=True, blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        verbose_name="Địa Lý"
    )
    gdcd = models.FloatField(
        null=True, blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        verbose_name="GDCD"
    )
    
    # Foreign language code
    ma_ngoai_ngu = models.ForeignKey(
        ForeignLanguage,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name="Foreign Language"
    )
    
    # Calculated fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"SBD: {self.sbd}"
    
    def get_group_a_total(self):
        """Calculate total score for Group A subjects (Math, Physics, Chemistry)"""
        scores = [self.toan, self.vat_li, self.hoa_hoc]
        valid_scores = [score for score in scores if score is not None]
        return sum(valid_scores) if len(valid_scores) == 3 else None
    
    def get_group_a_average(self):
        """Calculate average score for Group A subjects"""
        total = self.get_group_a_total()
        return total / 3 if total is not None else None
    
    def has_complete_group_a(self):
        """Check if student has all Group A subject scores"""
        return all([self.toan is not None, self.vat_li is not None, self.hoa_hoc is not None])
    
    def get_all_scores(self):
        """Get dictionary of all subject scores"""
        return {
            'toan': self.toan,
            'ngu_van': self.ngu_van,
            'ngoai_ngu': self.ngoai_ngu,
            'vat_li': self.vat_li,
            'hoa_hoc': self.hoa_hoc,
            'sinh_hoc': self.sinh_hoc,
            'lich_su': self.lich_su,
            'dia_li': self.dia_li,
            'gdcd': self.gdcd,
        }
    
    def get_score_level(self, subject_name):
        """Get score level for a specific subject"""
        score = getattr(self, subject_name, None)
        if score is None:
            return "No score"
        if score >= 8:
            return "Excellent"
        elif score >= 6:
            return "Good"
        elif score >= 4:
            return "Average"
        else:
            return "Below Average"
    
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['sbd']),
            models.Index(fields=['toan', 'vat_li', 'hoa_hoc']),  # For Group A queries
        ]


class ScoreStatistics(models.Model):
    """Model to store calculated statistics for better performance"""
    subject_name = models.CharField(max_length=20)
    level_excellent = models.IntegerField(default=0)  # >=8
    level_good = models.IntegerField(default=0)       # 6-8
    level_average = models.IntegerField(default=0)    # 4-6
    level_below = models.IntegerField(default=0)      # <4
    total_students = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Statistics for {self.subject_name}"
    
    class Meta:
        verbose_name = "Score Statistics"
        verbose_name_plural = "Score Statistics"
        unique_together = ['subject_name']
