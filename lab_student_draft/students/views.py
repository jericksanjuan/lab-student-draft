from django.forms import ValidationError, Select
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from braces.views import SetHeadlineMixin, LoginRequiredMixin
from crudwrapper.views import UpdateWithInlinesView, InlineFormSet, BaseInlineFormSet
from crudwrapper.forms import CrispyModelForm
from tables2_extras import ModelSingleTableView
from model_utils import Choices

from .models import StudentGroup, Student, GroupPreference
from labs.models import Lab


class StudentGroupRequiredMixin(LoginRequiredMixin):

    def get_student_group(self):
        try:
            student_group = self.request.user.studentgroup
        except:
            raise PermissionDenied
        return student_group

    def get_object(self):
        return self.get_student_group()


class PreferenceFormSet(BaseInlineFormSet):
    def clean(self):
        if any(self.errors):
            return

        scores = []
        for form in self.forms:
            score = form.cleaned_data.get('preference')
            if score in scores:
                raise ValidationError('Preferences for each lab should be unique!')
            scores.append(score)


class PreferenceForm(CrispyModelForm):

    class Meta:
        model = GroupPreference
        fields = ('preference',)
        lab_count = Lab.objects.filter(active=True).count()+1
        widgets = {'preference': Select(choices=Choices(*range(1, lab_count)))}


class PreferenceInline(InlineFormSet):
    model = GroupPreference
    fields = ('preference',)
    can_delete = False
    extra = 0
    form_class = PreferenceForm
    formset_class = PreferenceFormSet


class RankPreferenceView(StudentGroupRequiredMixin, SetHeadlineMixin, UpdateWithInlinesView):
    model = StudentGroup
    inlines = [PreferenceInline]
    fields = []
    template_name = 'students/rank-preference.html'
    headline = "Specify you Lab Preferences"

    def forms_valid(self, *args, **kwargs):
        response = super(RankPreferenceView, self).forms_valid(*args, **kwargs)
        self.object.has_preference = True
        self.object.save()
        return response

    def get_success_url(self):
        return reverse('rank-preference',)

    def get_form_valid_message(self):
        return "Thank you for specifying your Lab choices!"


class StudentInline(InlineFormSet):
    model = Student
    can_delete = False
    extra = 0


class UpdateStudentGroupView(StudentGroupRequiredMixin, SetHeadlineMixin, UpdateWithInlinesView):
    model = StudentGroup
    inlines = [StudentInline]
    fields = []
    formset_panel_layout = True
    headline = "Update Group Members"

    def get_success_url(self):
        return reverse('update-group',)

    def get_form_valid_message(self):
        return "Group information updated!"


class ResultsListView(SetHeadlineMixin, ModelSingleTableView):
    model = StudentGroup
    table_fields = ('user', 'students', 'has_preference', 'lab')
    headline = 'Results'
    paginate_by = 20
    orderable = False


rank_preference = RankPreferenceView.as_view()
update_group = UpdateStudentGroupView.as_view()
results_list = ResultsListView.as_view()
