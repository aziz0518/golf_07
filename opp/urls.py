from django.urls import path
from .views.views import index, detail_event, listing, add_events, MemberAdd, PersonAddView
from .views.auth import login_page, RegisterPageView


urlpatterns = [
    path('',index, name='index'),
    path('detail/', detail_event, name='detail'),
    path('listing/', listing, name='listing'),
    path('member/', MemberAdd.as_view(), name='member'),
    # path('', Person.as_view(), name='person'),
    path('add-person/', PersonAddView.as_view(), name='add_person' ),
    path('add-event/', add_events, name='add_event'),




    # Login register pages
    path('login/', login_page, name='login'),
    path('register/', RegisterPageView.as_view(), name='register')


]