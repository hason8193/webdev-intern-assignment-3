import csv
import os
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.conf import settings
from scores.models import Student, ForeignLanguage, Subject


class Command(BaseCommand):
    help = 'Import student scores from CSV file'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            default='dataset/diem_thi_thpt_2024.csv',
            help='Path to CSV file (default: dataset/diem_thi_thpt_2024.csv)'
        )
        parser.add_argument(
            '--batch-size',
            type=int,
            default=1000,
            help='Number of records to process in each batch (default: 1000)'
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing data before import'
        )
    
    def handle(self, *args, **options):
        csv_file = options['file']
        batch_size = options['batch_size']
        clear_data = options['clear']
        
        # Check if file exists
        if not os.path.exists(csv_file):
            raise CommandError(f'File "{csv_file}" does not exist.')
        
        self.stdout.write(f'Starting import from {csv_file}...')
        
        # Clear existing data if requested
        if clear_data:
            self.stdout.write('Clearing existing data...')
            Student.objects.all().delete()
            ForeignLanguage.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Existing data cleared.'))
        
        # Create foreign languages and subjects
        self.create_initial_data()
        
        # Import students
        imported_count = self.import_students(csv_file, batch_size)
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully imported {imported_count} student records.'
            )
        )
    
    def create_initial_data(self):
        """Create initial foreign languages and subjects"""
        self.stdout.write('Creating initial data...')
        
        # Create foreign languages
        languages = [
            ('N1', 'English'),
            ('N2', 'Russian'),
            ('N3', 'French'),
            ('N4', 'Chinese'),
            ('N5', 'German'),
            ('N6', 'Japanese'),
        ]
        
        for code, name in languages:
            ForeignLanguage.objects.get_or_create(
                code=code,
                defaults={'name': name}
            )
        
        # Create subjects
        subjects = [
            ('toan', 'Toán', True),
            ('ngu_van', 'Ngữ Văn', False),
            ('ngoai_ngu', 'Ngoại Ngữ', False),
            ('vat_li', 'Vật Lý', True),
            ('hoa_hoc', 'Hóa Học', True),
            ('sinh_hoc', 'Sinh Học', False),
            ('lich_su', 'Lịch Sử', False),
            ('dia_li', 'Địa Lý', False),
            ('gdcd', 'GDCD', False),
        ]
        
        for code, name, is_group_a in subjects:
            Subject.objects.get_or_create(
                code=code,
                defaults={'name': name, 'is_group_a': is_group_a}
            )
        
        self.stdout.write(self.style.SUCCESS('Initial data created.'))
    
    def import_students(self, csv_file, batch_size):
        """Import student data from CSV file"""
        students_to_create = []
        imported_count = 0
        
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row_num, row in enumerate(reader, start=1):
                try:
                    student = self.create_student_from_row(row)
                    if student:
                        students_to_create.append(student)
                    
                    # Batch insert
                    if len(students_to_create) >= batch_size:
                        self.bulk_create_students(students_to_create)
                        imported_count += len(students_to_create)
                        students_to_create = []
                        self.stdout.write(f'Processed {imported_count} records...')
                
                except Exception as e:
                    self.stdout.write(
                        self.style.WARNING(
                            f'Error processing row {row_num}: {str(e)}'
                        )
                    )
                    continue
            
            # Insert remaining students
            if students_to_create:
                self.bulk_create_students(students_to_create)
                imported_count += len(students_to_create)
        
        return imported_count
    
    def create_student_from_row(self, row):
        """Create Student object from CSV row"""
        # Get foreign language
        foreign_language = None
        if row.get('ma_ngoai_ngu'):
            try:
                foreign_language = ForeignLanguage.objects.get(
                    code=row['ma_ngoai_ngu']
                )
            except ForeignLanguage.DoesNotExist:
                pass
        
        # Convert empty strings to None for numeric fields
        def safe_float(value):
            if value == '' or value is None:
                return None
            try:
                return float(value)
            except (ValueError, TypeError):
                return None
        
        student = Student(
            sbd=row['sbd'],
            toan=safe_float(row.get('toan')),
            ngu_van=safe_float(row.get('ngu_van')),
            ngoai_ngu=safe_float(row.get('ngoai_ngu')),
            vat_li=safe_float(row.get('vat_li')),
            hoa_hoc=safe_float(row.get('hoa_hoc')),
            sinh_hoc=safe_float(row.get('sinh_hoc')),
            lich_su=safe_float(row.get('lich_su')),
            dia_li=safe_float(row.get('dia_li')),
            gdcd=safe_float(row.get('gdcd')),
            ma_ngoai_ngu=foreign_language
        )
        
        return student
    
    def bulk_create_students(self, students):
        """Bulk create students with transaction"""
        try:
            with transaction.atomic():
                Student.objects.bulk_create(students, ignore_conflicts=True)
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(
                    f'Error bulk creating students: {str(e)}'
                )
            )
            raise