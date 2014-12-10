from django.core.urlresolvers import reverse
from braces.views import SetHeadlineMixin
from crudwrapper.views import UpdateWithInlinesView, InlineFormSet
from .models import StudentGroup, Student, GroupPreference


class PreferenceInline(InlineFormSet):
    model = GroupPreference
    fields = ('preference',)
    can_delete = False
    extra = 0


class RankPreferenceView(SetHeadlineMixin, UpdateWithInlinesView):
    model = StudentGroup
    inlines = [PreferenceInline]
    fields = []
    template_name = 'students/rank-preference.html'
    headline = "Specify you Lab Preferences"

    def get_success_url(self):
        return reverse('rank-preference', kwargs=(dict(pk=self.object.pk)))

    def get_form_valid_message(self):
        return "Thank you for specifying your Lab choices!"


class StudentInline(InlineFormSet):
    model = Student
    can_delete = False
    extra = 0


class UpdateStudentGroupView(SetHeadlineMixin, UpdateWithInlinesView):
    model = StudentGroup
    inlines = [StudentInline]
    fields = []
    formset_panel_layout = True
    headline = "Update Group Members"

    def get_success_url(self):
        return reverse('update-group', kwargs=(dict(pk=self.object.pk)))

    def get_form_valid_message(self):
        return "Group information updated!"

rank_preference = RankPreferenceView.as_view()
update_group = UpdateStudentGroupView.as_view()
