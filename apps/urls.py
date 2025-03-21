from django.urls import path

from apps.forms import ChangePasswordModelForm
from apps.views import ProductDetailCreateView, ProductListView, CustomLoginView, CategoryListView, \
    CategoryObjectListView, \
    ProfileDetailView, ProfileUpdateView, LogoutView, DistrictListView, OrderDetailView, StreamListView, \
    StreamProductDetailView, MarketListView, OrderListView, ProductStatisticDetailView, StreamCreateView, \
    StreamStatusListView, AdminPageTemplateView, FavouriteView, FavouriteListView, OrderStreamRequestListView, \
    PaymentTemplateView, CompetitionListView

urlpatterns = [
    # Products
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<slug:slug>/', ProductDetailCreateView.as_view(), name='product_detail'),
    path('oqim/<int:pk>/', StreamProductDetailView.as_view(), name='stream_product'),

    # Categories
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/<slug:slug>/', CategoryObjectListView.as_view(), name='category_object_list'),

    # Orders
    path('success-product/<int:pk>/', OrderDetailView.as_view(), name='success_product'),
    path('profile/ordered-products/', OrderListView.as_view(), name='order_list'),

    # Profile
    path('profile/', ProfileDetailView.as_view(), name='profile'),
    path('profile/settings/', ProfileUpdateView.as_view(
        fields=('image', 'first_name', 'last_name', 'address', 'telegram_id', 'district', 'about')),
         name='profile_settings'),
    path('profile/update-password/', ProfileUpdateView.as_view(
        form_class=ChangePasswordModelForm
    ), name='update_password'),
    path('get-districts/', DistrictListView.as_view(), name='get_districts'),
    # Favourite
    path('favourite/<int:pk>/', FavouriteView.as_view(), name='favorite'),
    path('profile/liked-products/', FavouriteListView.as_view(), name='favorite_list'),

    # auth
    path('login/', CustomLoginView.as_view(), name='login_page'),
    path('logout/', LogoutView.as_view(), name='logout_page'),
    path('logout/', LogoutView.as_view(), name='logout_page'),

    # Admin page
    path('admin-page/', AdminPageTemplateView.as_view(), name='menu'),
    path('admin-page/market/', MarketListView.as_view(), name='market'),
    path('admin-page/product/<int:pk>/', ProductStatisticDetailView.as_view(), name='statistic_product'),
    path('admin-page/requests/', OrderStreamRequestListView.as_view(), name='order_stream_request_list'),
    path('admin-page/payment/', PaymentTemplateView.as_view(), name='payment'),
    path('admin-page/competition/', CompetitionListView.as_view(), name='competition'),

    # Stream
    path('admin-page/urls/', StreamListView.as_view(), name='stream_list'),
    path('admin-page/stats/', StreamStatusListView.as_view(), name='stream_status'),
    path('oqim/create/', StreamCreateView.as_view(), name='create_stream'),

]
