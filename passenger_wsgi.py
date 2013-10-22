import sys, os
INTERP = os.path.join(os.environ['HOME'], 'matteonardi.org', 'mysiteenv', 'bin', 'python')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())
sys.path.append(os.path.join(os.getcwd(),'mysite'))
os.environ['DJANGO_SETTINGS_MODULE'] = "mysite.settings"
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
