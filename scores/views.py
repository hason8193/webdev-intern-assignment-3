from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q, Count
from django.views.generic import TemplateView
from django.contrib import messages
from .models import Student, Subject
from .forms import ScoreLookupForm


class HomeView(TemplateView):
    """Home page view"""
    template_name = 'scores/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ScoreLookupForm()
        context['total_students'] = Student.objects.count()
        return context


def score_lookup(request):
    """View for looking up student scores"""
    student = None
    form = ScoreLookupForm()
    
    if request.method == 'POST':
        form = ScoreLookupForm(request.POST)
        if form.is_valid():
            sbd = form.cleaned_data['sbd']
            try:
                student = Student.objects.select_related('ma_ngoai_ngu').get(sbd=sbd)
                messages.success(request, f'Found student with registration number {sbd}')
            except Student.DoesNotExist:
                messages.error(request, f'No student found with registration number {sbd}')
    
    context = {
        'form': form,
        'student': student,
    }
    return render(request, 'scores/lookup.html', context)


def score_statistics(request):
    """View for displaying score statistics and reports"""
    subjects = ['toan', 'ngu_van', 'ngoai_ngu', 'vat_li', 'hoa_hoc', 'sinh_hoc', 'lich_su', 'dia_li', 'gdcd']
    subject_names = {
        'toan': 'Toán',
        'ngu_van': 'Ngữ Văn',
        'ngoai_ngu': 'Ngoại Ngữ',
        'vat_li': 'Vật Lý',
        'hoa_hoc': 'Hóa Học',
        'sinh_hoc': 'Sinh Học',
        'lich_su': 'Lịch Sử',
        'dia_li': 'Địa Lý',
        'gdcd': 'GDCD',
    }
    
    statistics = {}
    
    for subject in subjects:
        # Get statistics for each subject
        stats = Student.objects.filter(**{f'{subject}__isnull': False}).aggregate(
            excellent=Count('id', filter=Q(**{f'{subject}__gte': 8})),
            good=Count('id', filter=Q(**{f'{subject}__gte': 6, f'{subject}__lt': 8})),
            average=Count('id', filter=Q(**{f'{subject}__gte': 4, f'{subject}__lt': 6})),
            below=Count('id', filter=Q(**{f'{subject}__lt': 4})),
            total=Count('id')
        )
        
        # Calculate percentages
        total = stats['total']
        if total > 0:
            excellent_pct = (stats['excellent'] / total) * 100
            good_pct = (stats['good'] / total) * 100
            average_pct = (stats['average'] / total) * 100
            below_pct = (stats['below'] / total) * 100
        else:
            excellent_pct = good_pct = average_pct = below_pct = 0
        
        statistics[subject] = {
            'name': subject_names[subject],
            'excellent': stats['excellent'],
            'good': stats['good'],
            'average': stats['average'],
            'below': stats['below'],
            'total': stats['total'],
            'excellent_pct': excellent_pct,
            'good_pct': good_pct,
            'average_pct': average_pct,
            'below_pct': below_pct,
        }
    
    context = {
        'statistics': statistics,
        'subjects': subjects,
        'subject_names': subject_names,
    }
    return render(request, 'scores/statistics.html', context)


def top_group_a_students(request):
    """View for displaying top 10 Group A students"""
    # Get students who have all Group A subjects (Math, Physics, Chemistry)
    top_students = Student.objects.filter(
        toan__isnull=False,
        vat_li__isnull=False,
        hoa_hoc__isnull=False
    ).extra(
        select={'group_a_total': 'toan + vat_li + hoa_hoc'}
    ).order_by('-group_a_total')[:10]
    
    # Calculate statistics for the summary cards
    if top_students:
        # Calculate average of top 10 Group A scores
        total_score = sum(student.group_a_total for student in top_students)
        average_score = total_score / len(top_students)
        
        # Count students with excellent scores (average >= 8.0)
        excellent_count = sum(1 for student in top_students if student.get_group_a_average() >= 8.0)
        excellent_percentage = (excellent_count / len(top_students)) * 100
        
        # Get total number of Group A students in database
        total_group_a_students = Student.objects.filter(
            toan__isnull=False,
            vat_li__isnull=False,
            hoa_hoc__isnull=False
        ).count()
    else:
        average_score = 0
        excellent_count = 0
        excellent_percentage = 0
        total_group_a_students = 0
    
    context = {
        'top_students': top_students,
        'average_score': average_score,
        'excellent_count': excellent_count,
        'excellent_percentage': excellent_percentage,
        'total_group_a_students': total_group_a_students,
    }
    return render(request, 'scores/top_group_a.html', context)


def statistics_api(request):
    """API endpoint for statistics data (for charts)"""
    subjects = ['toan', 'ngu_van', 'ngoai_ngu', 'vat_li', 'hoa_hoc', 'sinh_hoc', 'lich_su', 'dia_li', 'gdcd']
    subject_names = {
        'toan': 'Toán',
        'ngu_van': 'Ngữ Văn',
        'ngoai_ngu': 'Ngoại Ngữ',
        'vat_li': 'Vật Lý',
        'hoa_hoc': 'Hóa Học',
        'sinh_hoc': 'Sinh Học',
        'lich_su': 'Lịch Sử',
        'dia_li': 'Địa Lý',
        'gdcd': 'GDCD',
    }
    
    data = {
        'labels': [],
        'excellent': [],
        'good': [],
        'average': [],
        'below': []
    }
    
    for subject in subjects:
        stats = Student.objects.filter(**{f'{subject}__isnull': False}).aggregate(
            excellent=Count('id', filter=Q(**{f'{subject}__gte': 8})),
            good=Count('id', filter=Q(**{f'{subject}__gte': 6, f'{subject}__lt': 8})),
            average=Count('id', filter=Q(**{f'{subject}__gte': 4, f'{subject}__lt': 6})),
            below=Count('id', filter=Q(**{f'{subject}__lt': 4}))
        )
        
        data['labels'].append(subject_names[subject])
        data['excellent'].append(stats['excellent'])
        data['good'].append(stats['good'])
        data['average'].append(stats['average'])
        data['below'].append(stats['below'])
    
    return JsonResponse(data)


class AboutView(TemplateView):
    """About page view"""
    template_name = 'scores/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_students'] = Student.objects.count()
        context['subjects_count'] = Subject.objects.count()
        context['languages_count'] = Student.objects.exclude(ma_ngoai_ngu__isnull=True).values('ma_ngoai_ngu').distinct().count()
        return context
