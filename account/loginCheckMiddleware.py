from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class LoginCheckMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        user = request.user
        if user.is_authenticated:
            if user.user_type == "2":
                if modulename == "account.admin_views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("home"))
        else:
            if request.path == reverse("login") or request.path == reverse("registration") or modulename == 'frontend.views':
                pass
            else:
                return HttpResponseRedirect(reverse("login"))
