from django.contrib.auth.models import User

def protect_context(request):

  context = {
    'me': User.objects.first(),
  }

  return context