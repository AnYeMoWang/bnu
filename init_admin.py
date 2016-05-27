#!/usr/bin/env python
import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bnu.settings")
    cmd = 'cd /opt/bnu && python manage.py syncdb --noinput && python manage.py collectstatic --noinput'
    os.system(cmd)
    from django.contrib.auth.models import User
    admin = User.objects.filter(username='admin')
    if admin.count():
        print 'admin Exists'
    else:
        init_admin = User()
        init_admin.username = 'admin'
        init_admin.is_superuser = True
        init_admin.is_active = True
        init_admin.set_password('1qaz_PL<@bnu')
        init_admin.save()
