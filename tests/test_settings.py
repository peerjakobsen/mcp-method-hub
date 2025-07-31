from django.conf import settings


def test_django_settings_configured():
    """Test that Django settings are properly configured."""
    assert settings.configured
    assert settings.SECRET_KEY is not None
    assert "django.contrib.admin" in settings.INSTALLED_APPS


def test_base_dir_exists():
    """Test that BASE_DIR is correctly set."""
    assert settings.BASE_DIR is not None
    assert settings.BASE_DIR.exists()


def test_database_configured():
    """Test that database settings are configured."""
    assert "default" in settings.DATABASES
    assert settings.DATABASES["default"]["ENGINE"] is not None
