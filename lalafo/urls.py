from django.urls import path, include
from rest_framework.routers import DefaultRouter
from.views.elan_views import ElanViewSet, elan_list, create_elan, update_elan, delete_elan
from.views.comment_views import CommentViewSet, comment_list, create_comment, update_comment, delete_comment

router = DefaultRouter()
router.register(r'elanlar',  ElanViewSet)
router.register(r'comments',  CommentViewSet)

urlpatterns = [
    path("elanlar/",  elan_list, name="elan_list"),
    path("create_elan/",  create_elan,  name="create_elan"),
    path("update_elan/<int:pk>/",  update_elan, name="update_elan"),
    path("delete_elan/<int:pk>/",  delete_elan, name="delete_elan"),

    path("comments/",  comment_list,  name="comment_list"),
    path("create_comment/", create_comment, name="create_comment"),
    path("update_comment/<int:pk>/",  update_comment, name="update_comment"),
    path("delete_comment/<int:pk>/",  delete_comment, name="delete_comment"),

    path("api/",  include(router.urls))
]
