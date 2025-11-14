#!/usr/bin/env python
"""Setup script for minimal Django admin demo"""
import os
import sys
import subprocess

def run_command(cmd, description):
    """Run a command and print status"""
    print(f"\n→ {description}...")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"✗ Error: {result.stderr}")
        sys.exit(1)
    print(f"✓ {description} complete")
    return result.stdout

def main():
    print("Setting up Django admin demo...\n")
    
    # Get the Python executable
    python = sys.executable
    
    # Run migrations
    run_command(
        f"{python} manage.py migrate --settings=mysite.settings",
        "Running database migrations"
    )
    
    # Create superuser
    run_command(
        f"{python} manage.py createsuperuser --username admin --email admin@example.com --noinput --settings=mysite.settings",
        "Creating superuser 'admin'"
    )
    
    # Set password
    run_command(
        f"{python} -c \"import os; os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings'); import django; django.setup(); from django.contrib.auth.models import User; u = User.objects.get(username='admin'); u.set_password('admin'); u.save()\"",
        "Setting password"
    )
    
    print("\n" + "="*50)
    print("Setup complete! 🎉")
    print("="*50)
    print("\nTo start the server, run:")
    print(f"  {python} manage.py runserver --settings=mysite.settings")
    print("\nThen visit:")
    print("  • http://127.0.0.1:8000/ - Hello World")
    print("  • http://127.0.0.1:8000/admin/ - Admin panel")
    print("\nLogin credentials:")
    print("  Username: admin")
    print("  Password: admin")

if __name__ == "__main__":
    main()
