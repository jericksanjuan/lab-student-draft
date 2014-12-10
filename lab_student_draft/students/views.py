from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from braces.views import SetHeadlineMixin, LoginRequiredMixin
from crudwrapper.views import UpdateWithInlinesView, InlineFormSet
from tables2_extras import ModelSingleTableView

from .models import StudentGroup, Student, GroupPreference


class StudentGroupRequiredMixin(LoginRequiredMixin):

    def get_student_group(self):
        try:
            student_group = self.request.user.studentgroup
        except:
            raise PermissionDenied
        return student_group

    def get_object(self):
        return self.get_student_group()


class PreferenceInline(InlineFormSet):
    model = GroupPreference
    fields = ('preference',)
    can_delete = False
    extra = 0


class RankPreferenceView(StudentGroupRequiredMixin, SetHeadlineMixin, UpdateWithInlinesView):
    model = StudentGroup
    inlines = [PreferenceInline]
    fields = []
    template_name = 'students/rank-preference.html'
    headline = "Specify you Lab Preferences"

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
    table_fields = ('user', 'students', 'lab')
    headline = 'Results'
    paginate_by = 20
    orderable = False


rank_preference = RankPreferenceView.as_view()
update_group = UpdateStudentGroupView.as_view()
results_list = ResultsListView.as_view()
