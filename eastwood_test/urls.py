"""eastwood_test URL Configuration
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from main.views.employees import Employees
from main.views.employee import Employee


urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

urlpatterns += [
    url(r'^employees/$', Employees.as_view(), name='employees'),
    url(r'^employee/(?P<pk>[0-9]+)/$', Employee.as_view(), name='employee'),
]

if settings.DEBUG:
    try:
        import debug_toolbar
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
    except ImportError:
        pass

