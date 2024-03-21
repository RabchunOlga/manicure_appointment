from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, render
from django.core.cache import cache
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from common.views import TitleMixin

from appointments.models import AppointmentCategory, AppointmentsListModel, Records

class IndexView(TitleMixin, TemplateView):
    template_name = 'appointments/index.html'
    title = 'Manicure'

class AppointmentsListView(TitleMixin, ListView):
    template_name = 'appointments/appointments.html'
    model = AppointmentsListModel
    title = 'Записаться'

    def get_queryset(self):
        queryset = super(AppointmentsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = cache.get('categories')
        if not categories:
            context['categories'] = AppointmentCategory.objects.all()
            cache.set('categories', context['categories'], 30)
        else:
            context['categories'] = categories

        # context['categories'] = AppointmentCategory.objects.all()

        return context

@login_required
def make_a_record(request, appointment_id):
    appointment = AppointmentsListModel.objects.get(id=appointment_id)
    record = Records.objects.filter(user=request.user, appointment=appointment)
    if not record.exists():
        Records.objects.create(user=request.user, appointment=appointment)

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

class RecordsListView(TitleMixin, ListView):
    model = Records
    template_name = 'appointments/records.html'
    title = 'Записи'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

