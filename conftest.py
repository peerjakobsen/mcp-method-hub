import os

import django


def pytest_configure():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mcp_method_hub.settings.local")
    django.setup()
