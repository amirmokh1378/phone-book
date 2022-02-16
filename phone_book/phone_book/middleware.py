import datetime
import random
import string
from django.contrib.auth.models import User
from phone_book_accounts.models import AnonymousAccount
from django.utils import timezone


def random_char(y=20):
    return ''.join(
        str(random.choice(list(string.ascii_letters) + [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '_'])) for x in range(y))


class UserCookieMiddleWare(object):
    """
    Middleware to set user cookie
    If user is authenticated and there is no cookie, set the cookie,
    If the user is not authenticated and the cookie remains, delete it
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)
        qu_user = AnonymousAccount.objects.all().filter(username=request.COOKIES.get('username'))
        if (not request.user.is_authenticated and request.COOKIES.get('username') is None) or not qu_user.exists():
            AnonymousAccount.objects.filter(expire_time__lt=timezone.now()).delete()
            while True:
                username = random_char()
                print(username)
                qu_user = AnonymousAccount.objects.all().filter(username=username)
                if not qu_user.exists():
                    response.set_cookie(key='username', value=f'{username}', max_age=172800)
                    AnonymousAccount(username=username).save()
                    break
        return response

