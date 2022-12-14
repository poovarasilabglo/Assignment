from django.urls import path
from . import views

urlpatterns = [
   path('',views.user_login, name='login'),
   path('listview/',views.list_view, name='listview'),
   path('jsondata/',views.jsondata, name='jsondata'),
   path('json/<int:id>',views.json, name='json'),
   path('logout/',views.user_logout, name='logout'),
   path('add/',views.student_add, name='add'),
   path('supdate/',views.student_update, name='supdate'),
   path('detail/<int:id>',views.detail_view, name = 'detail'),
   path('markadd/',views.mark_add, name = 'markadd'),
   path('markupdate/<int:id>',views.mark_update, name = 'markupdate'), 
   path('markdelete/<int:id>',views.mark_delete, name = 'markdelete'), 
   path('stu/<int:id>', views.student_update, name="su"),
   path('studentdelete/<int:id>/',views.student_delete, name = 'studentdelete'), 
]

