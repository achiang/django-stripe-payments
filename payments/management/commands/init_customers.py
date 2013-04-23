from django.core.management.base import BaseCommand

try:
    from django.contrib.auth import get_user_model
except ImportError:  # django < 1.5
    from django.contrib.auth.models import User
else:
    User = get_user_model()

from payments.models import Customer


class Command(BaseCommand):
    
    help = "Create customer objects for existing users that don't have one"
    
    def handle(self, *args, **options):
        for user in User.objects.filter(customer__isnull=True):
            Customer.create(user=user)
            print "Created customer for %s" % user.email
