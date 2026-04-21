from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    # API routes
    path('api/', include('vault.urls')),

    # React app (ONLY for non-api, non-static)
    re_path(r'^(?!api/|static/).*$', TemplateView.as_view(template_name='index.html')),
]