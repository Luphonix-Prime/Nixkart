#!/usr/bin/env python
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.utils import timezone

# Create superuser
try:
    admin_user = User.objects.create_superuser(
        username='luphonix_prime_admin',
        email='Luphoni.prime@gmail.com',
        password='keval_dhyey#2025',
        last_login=timezone.now(),
    )
    print("Superuser 'admin' created successfully.")
except IntegrityError:
    print("Superuser 'admin' already exists.")
except Exception as e:
    print(f"Error creating superuser: {e}")