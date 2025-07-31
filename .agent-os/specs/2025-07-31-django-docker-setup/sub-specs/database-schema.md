# Database Schema

This is the database schema implementation for the spec detailed in @.agent-os/specs/2025-07-31-django-docker-setup/spec.md

## Database Changes

### New Database Creation

```sql
-- Database initialization script
CREATE DATABASE mcpmethodhub;
CREATE USER mcpuser WITH PASSWORD 'mcppassword';
GRANT ALL PRIVILEGES ON DATABASE mcpmethodhub TO mcpuser;
ALTER USER mcpuser CREATEDB;
```

### Django Default Tables

The following Django system tables will be created through initial migration:

- `django_migrations` - Track applied database migrations
- `django_content_type` - Content type framework for generic relations
- `django_admin_log` - Admin interface action logging
- `auth_user` - User authentication and profile data
- `auth_group` - User groups and permissions
- `auth_permission` - System permissions
- `django_session` - Session data (if using database sessions)

### Database Configuration

```python
# Django database settings for Docker environment
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mcpmethodhub',
        'USER': 'mcpuser',
        'PASSWORD': 'mcppassword',
        'HOST': 'db',  # Docker service name
        'PORT': '5432',
        'OPTIONS': {
            'connect_timeout': 60,
        },
    }
}
```

### Indexes and Constraints

- Primary key indexes on all Django system tables (automatic)
- Unique constraints on username and email fields in auth_user table
- Foreign key constraints for user relationships and permissions

## Rationale

- PostgreSQL 17+ provides advanced features needed for SaaS applications including JSON fields, full-text search, and robust concurrency
- Separate database user with limited privileges follows security best practices
- Docker service networking allows database host to be referenced by service name 'db'
- Connection timeout prevents hanging connections during development restarts
