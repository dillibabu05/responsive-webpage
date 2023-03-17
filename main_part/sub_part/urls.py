from django.urls import path
from . import views
urlpatterns=[path('',views.indexland,name='indexland'),
             
# register             
path('reg',views.reg,name='reg'),

#==================================== register_form_submission =================================
path('register_form_submission',views.register_form_submission,name='register_form_submission'),
#==================================== register form submission =================================

#==================================== login_form_submisssion =============================
path('login_form_submission',views.login_form_submission,name='login_form_submission'),
#==================================== login form submission ==============================

# login
path('login',views.login,name='login'),



#======================================== contact =====================================================
path('contact_form_submission',views.contact_form_submission,name='contact_form_submission'),
#========================================= contact ====================================================
]
