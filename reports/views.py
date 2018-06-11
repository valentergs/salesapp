from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from reports.models import Reports


class AuthorMixin(object):

    def get_queryset(self):
        qs = super(AuthorMixin, self).get_queryset()
        return qs.filter(author=self.request.user)

class AuthorEditMixin(object):

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AuthorEditMixin, self).form_valid(form)

class AuthorReportMixin(AuthorMixin, LoginRequiredMixin):
    model = Reports

class AuthorReportsEditMixin(AuthorReportMixin, AuthorEditMixin, LoginRequiredMixin):
    success_url = reverse_lazy('reports:list')
    template_name = 'reports/reports_form.html'
    fields = ['customer', 'content', 'status', 'business']

class ReportsListView(AuthorMixin, ListView):
    model = Reports

    def get_queryset(self):
        qs = super(ReportsListView, self).get_queryset()
        return qs.filter(author=self.request.user)

class ReportsDetailView(DetailView):
    model = Reports
    template_name = 'reports/reports_detail.html'
    context_object_name = 'reports_detail'

class ReportsCreateView(AuthorReportsEditMixin, CreateView, PermissionRequiredMixin):
    permission_required = 'reports.add_reports'
    fields = ['customer', 'content', 'status', 'business']
    # form_class = 'ReportsForm'

class ReportsUpdateView(AuthorEditMixin, UpdateView, PermissionRequiredMixin):
    permission_required = 'reports.change_reports'
    template_name = 'reports/reports_update_form.html'

class ReportsDeleteView(AuthorReportsEditMixin, DeleteView, PermissionRequiredMixin):
    template_name = 'reports/reports_delete.html'
    success_url = reverse_lazy('list')
    permission_required = 'reports.delete_reports'