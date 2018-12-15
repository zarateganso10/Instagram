from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from twistter.views import DashBoardDetail, Home, SignUp, EditUser, PostCreate, edit_password,                              MakeFriends, RemoveFriends, Profile, Search
from django.urls import reverse_lazy


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('signin/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page= reverse_lazy('home')), name='logout'),
    path('dashboard/', DashBoardDetail.as_view(), name='dashboard'),
    path('dashboard/edit/<int:pk>/', EditUser.as_view(), name='edit'),
    path('dashboard/edit_password/', edit_password, name='edit_password'),
    path('dashboard/post/', PostCreate.as_view(), name='post_create'),
    path('dashboard/make_friend/<int:user_pk>/<int:friend_pk>/', MakeFriends.as_view(), name='make_friend'),
    path('dashboard/remove_friend/<int:user_pk>/<int:friend_pk>/', RemoveFriends.as_view(), name='remove_friend'),
    path('dashboard/profile/<int:pk>/',Profile.as_view(), name='profile'),
    path('dashboard/search/', Search.as_view(), name='search'),
    # path('dashboard/edit_biografia/<int:pk>/', EditBiografia.as_view(), name='edit_biografia'),
]