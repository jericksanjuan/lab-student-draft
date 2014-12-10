from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from braces.views import SetHeadlineMixin, LoginRequiredMixin, SuperuserRequiredMixin
from crudwrapper.views import (
    UpdateWithInlinesView, InlineFormSet, BaseInlineFormSet
)
from tables2_extras import ModelSingleTableView

from .models import Lab
from students.models import Selection, StudentGroup


class LabRequiredMixin(LoginRequiredMixin):

    def get_lab_group(self):
        try:
            lab = self.request.user.lab
        except:
            raise PermissionDenied
        return lab

    def get_object(self):
        return self.get_lab_group()


class SelectionFormSet(BaseInlineFormSet):
    def get_queryset(self):
        if not hasattr(self, '_queryset'):
            qs = super(SelectionFormSet, self).get_queryset().filter(student_group__lab=None)
            self._queryset = qs
        return self._queryset


class SelectionInline(InlineFormSet):
    model = Selection
    fields = ('is_selected',)
    can_delete = False
    extra = 0
    formset_class = SelectionFormSet


class SelectGroupView(LabRequiredMixin, SetHeadlineMixin, UpdateWithInlinesView):
    model = Lab
    fields = []
    inlines = [SelectionInline]
    template_name = 'labs/select_group.html'
    headline = 'Select Groups'

    def get_success_url(self):
        return reverse('select-group',)

    def get_form_valid_message(self):
        return 'Thank you for your selection!'


class LabResultsView(LabRequiredMixin, SetHeadlineMixin, ModelSingleTableView):
    model = StudentGroup
    table_fields = ('user', 'students')
    headline = 'Assigned Student Groups'
    orderable = False

    def get_queryset(self):
        lab = self.get_lab_group()
        return StudentGroup.objects.filter(lab=lab)


class LabSlotsListView(SuperuserRequiredMixin, SetHeadlineMixin, ModelSingleTableView):
    model = Lab
    table_fields = ('name', 'groups_picked', 'slots_taken', 'desired_groups')
    headline = 'Lab Slot Status'


select_group = SelectGroupView.as_view()
lab_results = LabResultsView.as_view()
lab_slots = LabSlotsListView.as_view()
