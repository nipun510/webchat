from chat import views
from django.conf.urls import url



urlpatterns = [ 
    url(r'^$', view=views.chat, name="chat"
    ),
    url(
        regex=r'^dialogs/(?P<username>[\w.@+-]+)$',
        view=views.DialogListView.as_view(),
        name='dialogs_detail'
    ),
    url(
        regex=r'^dialogs/$',
        view=views.DialogListView.as_view(),
        name='dialogs'
    ),
   
]