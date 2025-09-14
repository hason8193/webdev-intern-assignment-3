# G-Scores - High School Exam Results System

[![Django](https://img.shields.io/badge/Django-4.2-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)](https://getbootstrap.com/)
[![Chart.js](https://img.shields.io/badge/Chart.js-4.0-orange.svg)](https://www.chartjs.org/)

A comprehensive web application for managing and displaying high school exam results for the 2024 academic year. This project demonstrates proficiency in Django development, database design, and modern web technologies.

## ✨ Features

### Core Features ✅

- [x] **CSV Data Import**: Automated conversion of raw CSV data into database with proper structure
- [x] **Score Lookup**: Search student scores by registration number (SBD)
- [x] **Score Reports**: 4-level classification system (≥8, 6-8, 4-6, <4 points)
- [x] **Statistics Dashboard**: Visual charts showing score distribution by subjects
- [x] **Top 10 Group A**: Ranking of best performers in Math, Physics, Chemistry combination

### Additional Features ✅

- [x] **Responsive Design**: Optimized for desktop, tablet, and mobile devices
- [x] **Interactive Charts**: Chart.js integration for data visualization
- [x] **Modern UI**: Bootstrap 5 with custom styling and Google Fonts (Rubik)
- [x] **Form Validation**: Comprehensive client and server-side validation
- [x] **Security Features**: CSRF protection, input sanitization, secure headers

## 🏗️ Technical Architecture

### Backend

- **Framework**: Django 4.2 (Python 3.12)
- **Database**: MySQL 8.0+ (production) / SQLite (development fallback)
- **ORM**: Django ORM with optimized queries
- **Data Processing**: Pandas for CSV import
- **Web Server**: Gunicorn (production)

### Frontend

- **Framework**: Django Templates with Bootstrap 5
- **Styling**: Custom CSS with Bootstrap components
- **JavaScript**: Vanilla JS with Chart.js for visualizations
- **Fonts**: Google Fonts (Rubik family)
- **Icons**: Font Awesome 6

### DevOps

- **Static Files**: Whitenoise for Django static file serving

## 📊 Database Schema

### Models Overview

- **Student**: Core model storing exam results for each student
- **Subject**: Subject definitions with OOP-based classification methods
- **ForeignLanguage**: Foreign language codes and names
- **ScoreStatistics**: Cached statistics for performance optimization

### Key Features

- **Optimized Indexes**: Strategic database indexing for fast queries
- **Data Validation**: Field-level validation with Django validators
- **Relationships**: Proper foreign key relationships with cascade handling
- **Calculated Fields**: Dynamic Group A score calculations

## 🚀 Installation & Setup

### Method 1: Local Development

**Prerequisites:**

- Python 3.12+
- MySQL 8.0+ Server
- Git

1. **Clone the repository**

   ```bash
   git clone https://github.com/hason8193/webdev-intern-assignment-3.git
   cd webdev-intern-assignment-3
   ```

2. **Create and activate virtual environment**

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**

   ```bash
   python manage.py migrate
   ```

5. **Import exam data**

   ```bash
   python manage.py import_scores --batch-size=1000
   ```

6. **Create superuser (optional)**

   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files**

   ```bash
   python manage.py collectstatic
   ```

8. **Start development server**
   ```bash
   python manage.py runserver
   ```

Visit `http://127.0.0.1:8000` to access the application.

## 🗄️ MySQL Database Setup

This project requires **MySQL 8.0+** to store student exam data. Follow these steps to create the database and connect your project.

### Step 1: Install MySQL Server

**Download and install MySQL from:** https://dev.mysql.com/downloads/mysql/

**Or use package managers:**

- **Windows:** `choco install mysql` (with Chocolatey)
- **macOS:** `brew install mysql` (with Homebrew)
- **Ubuntu:** `sudo apt install mysql-server`

### Step 2: Start MySQL Service

- **Windows:** Open Services → Start "MySQL80" service
- **macOS/Linux:** `sudo systemctl start mysql` or `brew services start mysql`

### Step 3: Create the Database

1. **Open MySQL Command Line:**
   ```bash
   mysql -u root -p
   ```
2. **Create the gscores_db database:**
   ```sql
   CREATE DATABASE gscores_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   SHOW DATABASES;
   EXIT;
   ```

### Step 4: Update Django Settings

Make sure `gscores/settings.py` has the correct database configuration:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gscores_db',
        'USER': 'root',
        'PASSWORD': 'your_mysql_password',  # Change this!
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

**⚠️ Important:** Replace `'your_mysql_password'` with your actual MySQL root password.

### Step 5: Test the Connection

```bash
# Test database connection
python manage.py dbshell

# If successful, you'll see:
# mysql>
# Type 'exit' to quit
```

### Troubleshooting

- **"Access denied":** Check your MySQL password in settings.py
- **"Can't connect":** Ensure MySQL service is running
- **"Unknown database":** Re-run the CREATE DATABASE command

## 📝 Usage Guide

### 1. Score Lookup

- Navigate to **Score Lookup** page
- Enter 8-digit registration number (SBD)
- View detailed score breakdown and performance levels
- See Group A combination scores (if applicable)

### 2. Statistics Dashboard

- Visit **Statistics** page for comprehensive analysis
- Interactive charts showing score distribution
- Subject-wise performance breakdown
- 4-level classification statistics

### 3. Top Performers

- Check **Top Students** page for Group A rankings
- View top 10 students in Math + Physics + Chemistry
- See detailed score breakdown and rankings

### 4. Admin Interface

- Access `/admin/` for data management
- Login with superuser credentials
- Manage students, subjects, and foreign languages

## 🎯 Score Classification System

| Level             | Score Range | Description              | Badge Color |
| ----------------- | ----------- | ------------------------ | ----------- |
| **Excellent**     | 8.0 - 10.0  | Outstanding performance  | Green       |
| **Good**          | 6.0 - 7.9   | Good understanding       | Blue        |
| **Average**       | 4.0 - 5.9   | Satisfactory performance | Yellow      |
| **Below Average** | 0.0 - 3.9   | Needs improvement        | Red         |

## 📚 Subject Information

### All Subjects

- **Toán** (Mathematics) - Group A ⭐
- **Ngữ Văn** (Literature)
- **Ngoại Ngữ** (Foreign Language)
- **Vật Lý** (Physics) - Group A ⭐
- **Hóa Học** (Chemistry) - Group A ⭐
- **Sinh Học** (Biology)
- **Lịch Sử** (History)
- **Địa Lý** (Geography)
- **GDCD** (Civic Education)

### Group A Combination

Students taking **Mathematics**, **Physics**, and **Chemistry** are classified as Group A and ranked by their combined score in these subjects.

## 🔧 Management Commands

### Import Data

```bash
# Import with default settings
python manage.py import_scores

# Import with custom batch size
python manage.py import_scores --batch-size=500

# Clear existing data and import fresh
python manage.py import_scores --clear

# Import from custom file
python manage.py import_scores --file=path/to/your/file.csv
```

### Database Operations

```bash
# Create new migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic
```

## 🌐 Deployment Options

### 1. Heroku

```bash
# Install Heroku CLI and login
heroku create your-app-name
heroku addons:create heroku-postgresql:hobby-dev
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py import_scores
```

### 2. Vercel

```bash
# Install Vercel CLI
npm i -g vercel
vercel --prod
```

### 3. Fly.io

```bash
# Install flyctl
flyctl launch
flyctl deploy
```

### 4. Railway

```bash
# Connect GitHub repository to Railway
# Add environment variables
# Deploy automatically on push
```

## 🛠️ Development

### Project Structure

```
gscores/
├── gscores/                 # Django project settings
├── scores/                  # Main application
│   ├── models.py           # Database models
│   ├── views.py            # View logic
│   ├── forms.py            # Form definitions
│   ├── urls.py             # URL routing
│   ├── admin.py            # Admin interface
│   └── management/         # Custom commands
├── templates/              # HTML templates
├── static/                 # CSS, JS, images
├── dataset/                # CSV data files
├── requirements.txt        # Python dependencies
└── manage.py              # Django management
```

### Key Files

- `scores/models.py`: Database schema and business logic
- `scores/views.py`: Request handling and data processing
- `scores/management/commands/import_scores.py`: CSV import logic
- `templates/`: HTML templates with Bootstrap styling
- `static/`: CSS and JavaScript assets

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📊 Performance Considerations

### Database Optimization

- **Indexes**: Strategic indexing on SBD and Group A fields
- **Bulk Operations**: Efficient batch processing for data import
- **Query Optimization**: Select_related and prefetch_related usage
- **Caching**: Statistics caching for improved performance

### Frontend Optimization

- **Static Files**: Compressed and cached assets
- **Responsive Images**: Optimized image loading
- **Lazy Loading**: Chart.js loaded on demand
- **Minification**: CSS and JS minification in production

## 🔒 Security Features

### Django Security

- **CSRF Protection**: All forms protected against CSRF attacks
- **Input Validation**: Server-side validation on all inputs
- **SQL Injection Prevention**: ORM-based queries
- **XSS Protection**: Template auto-escaping enabled

### Production Security

- **Secure Headers**: Security headers via Nginx
- **HTTPS Ready**: SSL/TLS configuration support
- **Environment Variables**: Sensitive data in environment
- **Debug Mode**: Disabled in production

## 🧪 Testing

### Run Tests

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test scores

# Run with coverage
coverage run manage.py test
coverage report
```

### Test Data

```bash
# Create test data
python manage.py shell
>>> from scores.models import Student
>>> Student.objects.count()  # Check data import
```

## 📄 API Documentation

### Statistics API Endpoint

```
GET /api/statistics/
```

**Response Format:**

```json
{
  "labels": ["Toán", "Ngữ Văn", ...],
  "excellent": [1250, 2100, ...],
  "good": [2800, 3200, ...],
  "average": [1900, 1800, ...],
  "below": [850, 720, ...]
}
```

## 🐛 Troubleshooting

### Common Issues

**1. Import Command Fails**

```bash
# Check file path and permissions
ls -la dataset/diem_thi_thpt_2024.csv
# Ensure CSV format is correct
```

**2. Database Connection Error**

```bash
# For MySQL: Check connection
python manage.py dbshell
# Check MySQL service status
# Windows: services.msc -> MySQL
# Linux/Mac: sudo systemctl status mysql

# Verify database exists
mysql -u root -p
SHOW DATABASES;
USE gscores_db;

# Check Django database settings
python manage.py showmigrations
```

**3. Static Files Not Loading**

```bash
# Collect static files
python manage.py collectstatic --clear
# Check STATIC_URL settings
```

## 📞 Support

### Getting Help

- **Issues**: [GitHub Issues](https://github.com/hason8193/webdev-intern-assignment-3/issues)
- **Documentation**: [Django Documentation](https://docs.djangoproject.com/)
- **Community**: [Django Community](https://www.djangoproject.com/community/)

### Author

**Project Developer**

- GitHub: [@hason8193](https://github.com/hason8193)

## 🙏 Acknowledgments

- **Golden Owl**: For providing the internship opportunity and assignment
- **Django Community**: For the excellent web framework
- **Bootstrap Team**: For the responsive CSS framework
- **Chart.js**: For the beautiful data visualization library
- **Font Awesome**: For the comprehensive icon library

---

## 📋 Assignment Completion Checklist

### Must Have Requirements ✅

- [x] **CSV Data Import**: ✅ Management command with batch processing
- [x] **Score Lookup**: ✅ Form-based search with validation
- [x] **Score Reports**: ✅ 4-level classification system
- [x] **Statistics**: ✅ Subject-wise analysis with charts
- [x] **Top 10 Group A**: ✅ Math + Physics + Chemistry ranking

### Nice to Have Requirements ✅

- [x] **Responsive Design**: ✅ Bootstrap 5 with mobile optimization
- [x] **Docker Setup**: ✅ Complete containerization
- [x] **Live Deployment**: ✅ Ready for multiple platforms

### Technical Requirements ✅

- [x] **OOP Programming**: ✅ Subject management with OOP principles
- [x] **Form Validation**: ✅ Client and server-side validation
- [x] **Django ORM**: ✅ Optimized database interactions
- [x] **Security**: ✅ CSRF, validation, and secure headers

---

**Built with ❤️ for Golden Owl Assignment**

## 👥 Contributors

- **Edric Cao** (Golden Owl) - Original Assignment Creator
- **Project Developer** - Implementation and Development

## 📄 License

This project is created for educational purposes as part of the Golden Owl web developer internship assignment.
