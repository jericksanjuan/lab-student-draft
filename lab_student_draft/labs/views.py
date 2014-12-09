from django.core.urlresolvers import reverse
from crudwrapper.views import UpdateWithInlinesView, InlineFormSet
from crudwrapper import CrispyModelForm
from .models import Lab, Share
from students.models import Selection


class SelectionForm(CrispyModelForm):
    readonly_fields = ('student_group')

    class Meta:
        model = Selection
        fields = ('student_group', 'is_selected')



class SelectionInline(InlineFormSet):
    model = Selection
    form_class = SelectionForm
    # fields = ('is_selected', 'student_group')
    can_delete = False
    extra = 0


class SelectGroupView(UpdateWithInlinesView):
    model = Lab
    fields = []
    inlines = [SelectionInline]

    def get_success_url(self):
        return reverse('select-group', kwargs=(dict(pk=self.object.pk)))

select_group = SelectGroupView.as_view()
