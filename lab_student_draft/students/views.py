from django.core.urlresolvers import reverse
from crudwrapper.views import UpdateWithInlinesView, InlineFormSet
from .models import StudentGroup, Student, GroupPreference


class PreferenceInline(InlineFormSet):
    model = GroupPreference
    fields = ('preference', 'lab')
    can_delete = False
    extra = 0


class RankPreferenceView(UpdateWithInlinesView):
    model = StudentGroup
    inlines = [PreferenceInline]
    fields = []

    def get_success_url(self):
        return reverse('rank-preference', kwargs=(dict(pk=self.object.pk)))


class StudentInline(InlineFormSet):
    model = Student
    can_delete = False
    extra = 0


class UpdateStudentGroupView(UpdateWithInlinesView):
    model = StudentGroup
    inlines = [StudentInline]
    fields = []

    def get_success_url(self):
        return reverse('update-group', kwargs=(dict(pk=self.object.pk)))

rank_preference = RankPreferenceView.as_view()
update_group = UpdateStudentGroupView.as_view()
