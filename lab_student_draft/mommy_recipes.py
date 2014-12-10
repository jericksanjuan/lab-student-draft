from random import randint, choice

from django.contrib.auth.hashers import make_password
from model_mommy.recipe import Recipe, foreign_key, seq


from students.models import Batch, StudentGroup, Student, GroupPreference, Selection
from labs.models import Lab, Share
from users.models import User


_PERSON = (
    'Elsa', 'Ezra', 'Sasha', 'Atticus', 'Skyler', 'Nikita',
    'Arden', 'Mila', 'Olaf', 'Imogen', 'Ayla', 'Misha',
    'Hazel', 'Mira', 'Cosette', 'Kezia', 'Keegan', 'Quinn',
    'Hannibal', 'Theo', 'Enzo', 'Lexie', 'Jesse', 'Kalani',
    'Kalina', 'Nina', 'Sven', 'Maeve', 'Tristan', 'Kristoff',
    'Aslan', 'Ariel', 'Elysia', 'Avalon', 'Irene', 'Ezio',
    'Anisa', 'Kiera', 'Agnes', 'Kaelan', 'Jael', 'Tamara',
    'Ephraim', 'Reena', 'April', 'Lennox', 'Yasmin', 'Sloan',
    'Milan', 'Gael', 'Hans', 'Mimi', 'Deja', 'Stanley',
    'Sally', 'Jody', 'Ansel', 'Renata', 'Ishmael', 'Alfie',
    'Matthias', 'Kailani', 'August', 'Lula', 'Spencer',
)

name = lambda: choice(_PERSON)


user = Recipe(
    User,
    username=seq('user'),
    password=make_password('pass')
)


batch = Recipe(
    Batch
)

lab = Recipe(
    Lab,
    user=foreign_key(user),
    name=seq('lab')
)

share = Recipe(
    Share,
)

student_group = Recipe(
    StudentGroup,
    user=foreign_key(user),
    batch=foreign_key(batch),
)

student = Recipe(
    Student,
    first_name=name,
    last_name=name,
)

group_preference = Recipe(
    GroupPreference,
)

selection = Recipe(
    Selection
)


def create_test_data():
    batch_obj = batch.make()

    labs = []
    for i in xrange(10):
        lab_obj = lab.make()
        share.make(lab=lab_obj, batch=batch_obj, desired_groups=randint(1, 10))
        labs.append(lab_obj)

    for i in xrange(30):
        max_pref = len(labs) + 1

        student_group_obj = student_group.make(batch=batch_obj)
        for i in xrange(3):
            student.make(student_group=student_group_obj)

        for lab_obj in labs:
            group_preference.make(
                lab=lab_obj, student_group=student_group_obj, preference=randint(1, max_pref))
            selection.make(
                lab=lab_obj, student_group=student_group_obj)


def delete_test_data():
    User.objects.exclude(is_superuser=True).delete()
    Batch.objects.all().delete()
    Lab.objects.all().delete()
    Share.objects.all().delete()
    StudentGroup.objects.all().delete()
    Student.objects.all().delete()
    GroupPreference.objects.all().delete()
    Selection.objects.all().delete()
