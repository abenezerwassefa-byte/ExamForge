# ExamForge

### School Management System

ExamForge was intended to be web-based School Management System designed to centralize and simplify the administration of educational institutions.

The platform was conceived to provide a unified environment for school administrators, instructors, and students, bringing institutional administration, user management, course organization, student enrollment, and examination management into one system.

Built with Django and PostgreSQL, ExamForge uses a role-based architecture to organize relationships between schools, administrators, instructors, students, and academic activities.

The project establishes the foundations of an integrated school management platform, with examination management forming part of its broader functionality.

---

## Core Objectives

ExamForge was designed around the following objectives:

- Centralize school administration and academic organization.
- Establish structured relationships between schools, administrators, instructors, and students.
- Simplify instructor and student account management.
- Organize courses and student enrollment.
- Provide a structured question bank for academic assessments.
- Establish a foundation for examination administration and academic performance tracking.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Primary programming language |
| Django | Backend web framework |
| PostgreSQL | Relational database |
| Supabase | Database hosting infrastructure |
| HTML | Frontend structure |
| CSS | Interface styling |
| PyOTP | Time-based one-time password authentication |

### Backend Architecture

ExamForge uses Django's Model-View-Template (MVT) architecture.

The application is organized into separate Django applications, allowing different areas of the platform to maintain their own models, views, and application logic.

Django ORM handles database operations and relationships between application entities.

---

## Application Architecture

### 1. School Administration

The system includes a foundational structure for managing educational institutions.

Implemented components include:

- School records containing institutional information.
- School administrator accounts.
- Relationships between school administrators and their respective institutions.
- School-specific instructor associations.
- Active and inactive school status.

A school administrator is represented by an ordinary Django user account with an associated school record.

### 2. User and Account Management

ExamForge uses Django's authentication framework as the foundation for user management.

The application defines three primary user roles:

- **Platform Administrator:** Responsible for platform-level administration through Django's built-in superuser functionality.
- **School Administrator:** Responsible for managing their associated educational institution.
- **Instructor:** Associated with one or more schools.

Student accounts are also represented in the application's data model.

The account management implementation includes:

- User registration forms.
- Student and instructor registration interfaces.
- User profile records.
- Role identification.
- Login-protected dashboard views.
- Role-based dashboard routing.
- Access restrictions for selected dashboard views.

### 3. Instructor Management

The data model establishes relationships between instructors, schools, and school administrators.

Implemented structures include:

- Instructor records associated with schools.
- Relationships between instructors and school administrators.
- Support for an instructor having associations with multiple schools.
- A uniqueness constraint preventing duplicate instructor-school associations.

### 4. Student Management

The application includes a foundational student management structure.

Implemented data structures include:

- Student records associated with Django user accounts.
- Course enrollment relationships.
- Support for students enrolling in multiple courses.

The enrollment model supports the following statuses:

- Pending
- Active
- Rejected
- Cancelled

### 5. Course Management

ExamForge includes a course model designed to associate academic courses with instructors.
The course model provides the foundation for organizing academic activities within the platform.

### 6. Invitation Infrastructure

The application includes a course invitation data model.

Its structure supports:

- Email-based invitation records.
- Unique UUID invitation
