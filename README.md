# G-Scores - High School Exam Results System# G-Scores

[![Django](https://img.shields.io/badge/Django-4.2-green.svg)](https://www.djangoproject.com/)This is the instruction for web developer intern assignment at [Golden Owl](https://goldenowl.asia). You will build a simple web.

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)

[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)](https://getbootstrap.com/)Web template example. Hope you will make it more beautiful !!!

[![Chart.js](https://img.shields.io/badge/Chart.js-4.0-orange.svg)](https://www.chartjs.org/)

![template example](./screenshots/mockup-ui.png)

This is a comprehensive web application for managing and displaying high school exam results for the 2024 academic year. Built as part of the Golden Owl web developer intern assignment, it demonstrates proficiency in Django development, database design, and modern web technologies.# Requirements

1. From the raw data file ([diem_thi_thpt_2024.csv](./dataset/diem_thi_thpt_2024.csv)) save it into the database with the appropriate structure

![G-Scores Demo](./screenshots/mockup-ui.png)

2. Your application should have at least features in [Must have](#must-have), things in [Nice to have](#nice-to-have) is optional (but yeah, it's attractive if you have).

## 🚀 Live Demo

### Must have:

[**Live Application**](http://your-deployment-url.com) (Replace with actual deployment URL)- The conversion of raw data into the database must be coded and located in this source code. (**hint**: recommend use migration and seeder)

- Write a feature to check score from registration number input

## ✨ Features- Write a feature report. There will be 4 levels including: >=8 points, 8 points > && >=6 points, 6 points > && >= 4 points, < 4 points

    - Statistics of the number of students with scores in the above 4 levels by subjects. (Chart)

### Must Have Features ✅- List top 10 students of group A including (math, physics, chemistry)

- [x] **CSV Data Import**: Automated conversion of raw CSV data into database with proper structure### Nice to have:

- [x] **Score Lookup**: Search student scores by registration number (SBD)

- [x] **Score Reports**: 4-level classification system (≥8, 6-8, 4-6, <4 points)- Responsive design (look good on all devices: desktops, tablets & mobile phones).

- [x] **Statistics Dashboard**: Visual charts showing score distribution by subjects- Setup project use Docker.

- [x] **Top 10 Group A**: Ranking of best performers in Math, Physics, Chemistry combination- Deploy the application to go live.

### Nice to Have Features ✅# Technical Requirements

- [x] **Responsive Design**: Optimized for desktop, tablet, and mobile devices

- [x] **Docker Support**: Complete containerization for easy deployment### Frontend

- [x] **Interactive Charts**: Chart.js integration for data visualizationYou can use any front-end library/framework like React, Angular, Vue, ... or just simple things with HTML + CSS + Javascript (JQuery).

- [x] **Modern UI**: Bootstrap 5 with custom styling and Google Fonts (Rubik)- For JS intern use React you need to have:

- [x] **Form Validation**: Comprehensive client and server-side validation \* React Hooks

- [x] **Security Features**: CSRF protection, input sanitization, secure headers- Fonts (optional);

  - [https://fonts.google.com/specimen/Rubik?query=Rubik](https://fonts.google.com/specimen/Rubik?query=Rubik)

## 🏗️ Technical Architecture- You can use some available interfaces such as: [AdminLTe](https://adminlte.io/), [TailAdmin](https://tailadmin.com/)...

### Backend### Backend:

- **Framework**: Django 4.2 (Python 3.12)Choose one of your applied back-end libraries/frameworks: Maybe Laravel(PHP), Ruby on Rails, NestJS (NodeJs), Django (Python), unlimited framework... or a structure that you come up with yourselt.

- **Database**: SQLite (development) / PostgreSQL (production)- **Mandatory** use of **OOP programming** for managing subjects.

- **ORM**: Django ORM with optimized queries- Need form validation and logic tightening.

- **Data Processing**: Pandas for CSV import- For NodeJs, use TypeScript is a plus.

- **Web Server**: Gunicorn (production)- Use ORM for interacting with Database.

- Database: You can use postgreSQL, Mysql, mongoDB... to manage or cache the data.

### Frontend

- **Framework**: Django Templates with Bootstrap 5### Deployment

- **Styling**: Custom CSS with Bootstrap componentsSome providers allow free deployment for the trial version (note: Maybe some suppliers will update their policies and prices)

- **JavaScript**: Vanilla JS with Chart.js for visualizations

- **Fonts**: Google Fonts (Rubik family)- Heroku - https://heroku.com - Deploying Front & Backend

- **Icons**: Font Awesome 6- Vercel (Zeit) - https://vercel.com - Deploying Front & Backend apps at free of cost

- Fly - https://fly.io - Deploying Front & Backend apps at free of cost

### DevOps- Deta - https://deta.sh - Deploying Node.js and Python apps and APIs. They support most web frameworks like Express, Koa, Flask, and FastAPI. They also provide a very fast and powerful NoSQL database for free.

- **Containerization**: Docker with multi-stage builds- Heliohost - https://heliohost.org - PHP, Ruby on rails, perl, django, java(jsp)

- **Web Server**: Nginx (reverse proxy)- `...`

- **Database**: PostgreSQL (containerized)# Submission

- **Static Files**: Whitenoise for Django static file serving

After completing the assignment, please push the source code to remote repository (github/gitlab), then send us the link to your repository.

## 📊 Database Schema

Don't forget to add `README.md` which includes guide to run your project locally and demo link.

### Models Overview

- **Student**: Core model storing exam results for each student

- **Subject**: Subject definitions with OOP-based classification methods**GOOD LUCK!!!**

- **ForeignLanguage**: Foreign language codes and names

- **ScoreStatistics**: Cached statistics for performance optimization![Your Code Work](./screenshots/meme.png)

### Key Features# Contributors

- **Optimized Indexes**: Strategic database indexing for fast queries

- **Data Validation**: Field-level validation with Django validators- Edric Cao (from GO)

- **Relationships**: Proper foreign key relationships with cascade handling
- **Calculated Fields**: Dynamic Group A score calculations

## 🚀 Installation & Setup

### Method 1: Local Development

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/webdev-intern-assignment-3.git
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

4. **Set up environment variables**

   ```bash
   # Copy and modify .env file
   cp .env.example .env
   # Edit .env with your settings
   ```

5. **Run database migrations**

   ```bash
   python manage.py migrate
   ```

6. **Import exam data**

   ```bash
   python manage.py import_scores --batch-size=1000
   ```

7. **Create superuser (optional)**

   ```bash
   python manage.py createsuperuser
   ```

8. **Collect static files**

   ```bash
   python manage.py collectstatic
   ```

9. **Start development server**
   ```bash
   python manage.py runserver
   ```

Visit `http://127.0.0.1:8000` to access the application.

### Method 2: Docker Development

1. **Clone and navigate to project**

   ```bash
   git clone https://github.com/yourusername/webdev-intern-assignment-3.git
   cd webdev-intern-assignment-3
   ```

2. **Build and run with Docker**

   ```bash
   # Development mode (SQLite)
   docker-compose -f docker-compose.dev.yml up --build

   # Production mode (PostgreSQL + Nginx)
   docker-compose up --build
   ```

3. **Access the application**
   - Development: `http://localhost:8000`
   - Production: `http://localhost`

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

## 🐳 Docker Commands

### Development

```bash
# Start development environment
docker-compose -f docker-compose.dev.yml up

# Rebuild and start
docker-compose -f docker-compose.dev.yml up --build

# Stop containers
docker-compose -f docker-compose.dev.yml down
```

### Production

```bash
# Start production environment
docker-compose up -d

# View logs
docker-compose logs -f

# Scale web workers
docker-compose up --scale web=3

# Stop all services
docker-compose down
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
├── Dockerfile              # Docker configuration
├── docker-compose.yml      # Docker services
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
# Check database settings
python manage.py dbshell
# Verify migrations
python manage.py showmigrations
```

**3. Static Files Not Loading**

```bash
# Collect static files
python manage.py collectstatic --clear
# Check STATIC_URL settings
```

**4. Docker Build Issues**

```bash
# Clear Docker cache
docker system prune -a
# Rebuild without cache
docker-compose build --no-cache
```

## 📞 Support

### Getting Help

- **Issues**: [GitHub Issues](https://github.com/yourusername/webdev-intern-assignment-3/issues)
- **Documentation**: [Django Documentation](https://docs.djangoproject.com/)
- **Community**: [Django Community](https://www.djangoproject.com/community/)

### Author

**Your Name**

- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com
- LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)

## 📜 License

This project is created for the Golden Owl web developer intern assignment. All rights reserved.

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

![Your Code Work](./screenshots/meme.png)

# Contributors

- Edric Cao (from GO) - Original Assignment Creator
- Your Name - Implementation
