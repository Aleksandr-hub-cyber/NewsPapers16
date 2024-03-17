from django.urls import path
from .views import PostsList, PostDetail, PostCreate, PostSearch, PostEdit, PostDelete
from .views import IndexView
from django.views.decorators.cache import cache_page

urlpatterns = [
    path("", PostsList.as_view(), name='post_list'),
    path('<int:pk>/', cache_page(60 * 10)(PostDetail.as_view()), name='product_detail'),
    # добавим кэширование на детали товара. Раз в 10 минут товар будет записываться в кэш для экономии ресурсов.
    path('create/', PostCreate.as_view()),
    path('search/', PostSearch.as_view()),
    path("<int:pk>/edit/", PostEdit.as_view()),
    path("<int:pk>/delete/", PostDelete.as_view()),
    path('', IndexView.as_view()),

]
