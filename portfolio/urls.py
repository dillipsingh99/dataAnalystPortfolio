from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
<<<<<<< HEAD
from django.contrib.auth import views as auth_views
from users.views import login_view, register_view,logout_view
=======
>>>>>>> 1a729ec33828544cc42c545173254032db3c72c3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
<<<<<<< HEAD
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('register/', register_view, name="register"),
    # path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'), 
    #     name='password_change'),
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'), 
    #     name='password_change_done'),
    path('blog/', include('blog.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
] 
=======

]
>>>>>>> 1a729ec33828544cc42c545173254032db3c72c3

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
