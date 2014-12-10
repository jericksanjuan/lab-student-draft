from django.core.urlresolvers import reverse
from braces.views import SetHeadlineMixin
from crudwrapper.views import (
    UpdateWithInlinesView, InlineFormSet
)
from tables2_extras import ModelSingleTableView
from .models import Lab
from students.models import Selection, StudentGroup


class SelectionInline(InlineFormSet):
    model = Selection
    fields = ('is_selected',)
    can_delete = False
    extra = 0


class SelectGroupView(SetHeadlineMixin, UpdateWithInlinesView):
    model = Lab
    fields = []
    inlines = [SelectionInline]
    template_name = 'labs/select_group.html'
    headline = 'Select Groups'

    def get_success_url(self):
        return reverse('select-group', kwargs=(dict(pk=self.object.pk)))

    def get_form_valid_message(self):
        return 'Thank you for your selection!'


select_group = SelectGroupView.as_view()
