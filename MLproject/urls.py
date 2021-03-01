
from django.urls import path
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from django.http import StreamingHttpResponse
# from MLapp.camera import *


from authentication.views import (
    login_view,
    logout_view,
    register_view,

)
from MLapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view),
    path('', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
    path('select_images/',  select_pic_view, name='select_image'),
    # path('monitor/', lambda r: StreamingHttpResponse(gen(some_function()),
    #                                                  content_type='multipart/x-mixed-replace; boundary=frame')),
    path('monitor/', camera, name='camera'),


    
]



if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)