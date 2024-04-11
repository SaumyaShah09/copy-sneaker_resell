from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import *
from .views import *
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import views as auth_views


class MyPasswordResetForm(PasswordResetForm):
    pass






urlpatterns=[
    path("", views.home),
    path("about/", views.about,name="about"),
    path("contact/", views.contact,name="contact"),
    path("category/<slug:val>", views.CategoryView.as_view(),name="category"),
    path("product-detail/<int:pk>", views.ProductDetailView.as_view(),name="product-detail"),
    path("profile/",views.ProfileView.as_view(),name="profile"),
    path("address/",views.address,name="address"),
    path("updateAddress/<int:pk>", views.UpdateAddress.as_view(), name="updateAddress"),

    #login authentication
    path("registration/", views.CustomerRegistrationView.as_view(), name="customerregistration"),
    path("accounts/login/", auth_view.LoginView.as_view(template_name="sneaker/login.html",
         authentication_form=LoginForm),name='login'),
    # path("password- reset/", auth_view.PasswordResetView.as_view(
    #                 template_name="sneaker/password_reset.html",
    #                 form_class=MyPasswordResetForm
    #             ), name="password_reset"),
    path("passwordchange/",auth_view.PasswordChangeView.as_view(
        template_name="sneaker/changepassword.html",
        form_class=MyPasswordChangeForm,success_url='/passwordchangedone'
    ),name='passwordchange'),

    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view
    (template_name='sneaker/passwordchangedone.html'),name='passwordchangedone'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'),name='logout'),

    # ----------------------------------------------------------------------
    path('password-reset/', auth_view.PasswordResetView.as_view(
        template_name='sneaker/password_reset.html',form_class=MyPasswordResetForm)
         ,name='password_reset'),
    path('add/', views.add_product, name='add_product'),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(
        template_name='sneaker/password_reset_done.html'),name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>', auth_view.PasswordResetConfirmView.as_view(
        template_name='sneaker/password_reset_confirm.html',form_class=MySetPasswordForm),
         name='password_reset_confirm'),

    path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(
        template_name='sneaker/password_reset_complete.html')
         , name='password_reset_complete'),
    path('ngo-information/', views.ngo_information, name='ngo_information'),
    path('ngoregistration/', NGORegistrationView.as_view(), name='ngoregistration'),
    path('ngo/<int:pk>/', views.ngo_detail, name='ngo_detail'),
    path("", views.home, name="home"),
            ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

