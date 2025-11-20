from django.urls import path, include
from workers import views
from django.contrib import admin


urlpatterns = [
     path('admin/', admin.site.urls),   # ✔ Django admin panel
     path('', include('workers.urls')), # ✔ Your application routes
    path("", views.index, name="index"),
    path("login/", views.login_user, name="login_user"),
    path("logout/", views.logout_user, name="logout_user"),

    path("register/", views.newuser, name="newuser"),

    path("admin-page/", views.admin_page, name="admin_page"),

    path("worker/<int:worker_id>/", views.user_detail, name="user_detail"),

    # Worker categories
    path("plumber/", views.plumber, name="plumber"),
    path("plumber/job-site/", views.plumber_job_site, name="plumber_job_site"),
    path("plumber/payment/", views.plumber_payment, name="plumber_payment"),

    path("electrician/", views.electrician, name="electrician"),
    path("electrician/job-site/", views.electrician_job_site, name="electrician_job_site"),
    path("electrician/payment/", views.electrician_payment, name="electrician_payment"),

    # Projects
    path("projects/active/", views.active_project, name="active_project"),
    path("projects/completed/", views.completed_projects, name="completed_projects"),

    # Settings
    path('settings/admin.html', views.admin_page, name='admin_html'),
    path("settings/", views.setting, name="setting"),
]
