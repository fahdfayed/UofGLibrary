from django.urls import path
from library import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'library'

urlpatterns = [
    path('', views.index, name='index'),
   
    path('about/', views.About, name='about'), 
    path('bookpage/', views.BookPage, name='bookpage'),
    path('bookp/<int:id>/', views.detail, name='detail'),
    path('bookpage/', views.BookPage, name='bookpage'),
    path('login/', views.LogIn, name='login'),
    path('register/', views.Register, name='register'),
    path('favouritesList/', views.Favourites_List, name ='Favourites_List'),
    path('<int:id>/favourites/', views.Favourites, name='favourites'),
    path('validate-username/', csrf_exempt(views.validateUserName), name="validate-username"),
    path('validate-email/', csrf_exempt(views.validateEmail), name ='validate_email'),
    path('<slug:genre_name_slug>/',views.show_genre, name='show_genre'),
    path('logout/', views.user_logout, name='logout'),
    path('addreview/<int:id>/', views.add_review, name = "add_review"),
   

]
