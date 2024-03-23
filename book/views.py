from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic import DeleteView

from book.forms import BookForm
from book.models import Schedule
from book.utils import check_available_tables_for_time
from django.contrib import messages


# Create your views here.
class ScheduleList(generic.ListView):
    model = Schedule
    template_name = "book/schedule_list.html"
    login_url = '/accounts/login//'
    book_form = BookForm()
    context_object_name = 'schedules'

    def get_queryset(self):
        # Get the current date and time
        now = timezone.now()
        user = self.request.user

        if not user.is_authenticated:
            return Schedule.objects.none()

        # Filter schedules to get those with date_of_visit today or later
        queryset = super().get_queryset().filter(
            Q(visitor=user) &  # Use & for AND operation with Q objects
            (Q(date_of_visit__gt=now.date()) | Q(date_of_visit=now.date(), time_of_visit__gte=now.time()))
        )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ScheduleList, self).get_context_data(**kwargs)
        context['form'] = BookForm()  # Add the form to the context
        return context

    def post(self, request, *args, **kwargs):
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            date_of_visit = book_form.cleaned_data['date_of_visit']
            start_time = book_form.cleaned_data['time_of_visit']
            duration_hours = book_form.cleaned_data['number_of_hours']
            number_of_visitors = book_form.cleaned_data['number_of_visitors']
            available, message = check_available_tables_for_time(date_of_visit, start_time, duration_hours, number_of_visitors)
            if available:
                new_schedule = book_form.save(commit=False)
                new_schedule.visitor = request.user
                new_schedule.save()
                return HttpResponseRedirect('/')  # Redirect to home or any other page
            messages.error(request, message)
            return HttpResponseRedirect('/')

            # If the form is not valid, render the page with form errors
        return HttpResponseRedirect('/')


class ScheduleDeleteView(LoginRequiredMixin, DeleteView):
    model = Schedule
    success_url = reverse_lazy('schedule_list')  # Adjust as necessary

    def get_queryset(self):
        # Ensure users can only delete their own schedules
        qs = super().get_queryset()
        return qs.filter(visitor=self.request.user)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Optional: Add additional checks here if needed
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)
