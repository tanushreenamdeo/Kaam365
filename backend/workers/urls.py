from django.urls import path
from . import views

app_name = 'workers'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('newuser/', views.newuser, name='newuser'),

    # User dashboard
    path('user/<int:worker_id>/', views.user_detail, name='user_detail'),

    # Admin
    path('admin-page/', views.admin_page, name='admin_page'),

    # General
    path('overview/', views.overview, name='overview'),
    path('setting/', views.setting, name='setting'),

    # Plumber
    path('plumber/', views.plumber, name='plumber'),
    path('plumber/job-site/', views.plumber_job_site, name='plumber_job_site'),
    path('plumber/payment/', views.plumber_payment, name='plumber_payment'),

    # Electrician
    path('electrician/', views.electrician, name='electrician'),
    path('electrician/job-site/', views.electrician_job_site, name='electrician_job_site'),
    path('electrician/payment/', views.electrician_payment, name='electrician_payment'),

    # Projects
    path('active-project/', views.active_project, name='active_project'),
    path('completed-projects/', views.completed_projects, name='completed_projects'),
]
