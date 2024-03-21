from django.urls import path

from appointments.views import AppointmentsListView, make_a_record, RecordsListView

app_name = 'appointments'

urlpatterns = [
    path('', AppointmentsListView.as_view(), name='index'),
    path('category/<int:category_id>', AppointmentsListView.as_view(), name='category'),
    path('appointment/add/<int:appointment_id>', make_a_record, name='appointment_add'),
    path('records/', RecordsListView.as_view(), name='records'),

]
