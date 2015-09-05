from timetable.models import Subject, Teacher, Lesson, Timetable, LessonInTimeTable, DayInTimetable, WeekInTimetable
from rest_framework import generics, permissions
from timetable.serializers import SubjectSerializer, TeacherSerializer, LessonSerializer, LessonInTimetableSerializer
from users.permissions import CanViewTimetable, CanAddAndEditSubjects, CanAddAndEditTeachers, CanEditTimetable
from rest_framework.response import Response
from rest_framework import status
from timetable.utils import start_and_end_of_lesson
from rest_framework.views import APIView
import datetime

# Create your views here.


class SubjectListAPIView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.IsAuthenticated(), CanViewTimetable(),]
        return [permissions.IsAuthenticated(), CanAddAndEditSubjects(),]


class SubjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(self, request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.IsAuthenticated(), CanViewTimetable(),]
        return [permissions.IsAuthenticated(), CanAddAndEditSubjects(),]


class TeacherListAPIView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.IsAuthenticated(), CanViewTimetable(),]
        return [permissions.IsAuthenticated(), CanAddAndEditTeachers()]


class TeacherDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(self, request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.IsAuthenticated(), CanViewTimetable(),]
        return [permissions.IsAuthenticated(), CanAddAndEditTeachers(),]

class LessonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.IsAuthenticated(), CanViewTimetable(),]
        return [permissions.IsAuthenticated(), CanEditTimetable(),]

    def get_queryset(self):
        return Lesson.objects.filter(group = self.request.user.student.group)

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        data['group'] = request.user.student.group.name
        try:
            Subject.objects.get(name = data['subject'])
        except Subject.DoesNotExist:
            Subject.objects.create(name = data['subject'])
        serializer = LessonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LessonDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.IsAuthenticated(), CanViewTimetable(),]
        return [permissions.IsAuthenticated(), CanEditTimetable(),]
    def get_queryset(self):
        return Lesson.objects.filter(group = self.request.user.student.group)

class GenerateTimetable(APIView):
    permission_classes = (permissions.IsAuthenticated, CanEditTimetable)

    def post(self, request, format = None):
        group = request.user.student.group
        if not request.POST.get('semester',0).isdigit():
            return Response('Wrong semester parameter', status=status.HTTP_400_BAD_REQUEST)
        semester = int(request.POST.get('semester',0))
        if semester < 1 or semester > 18:
            return Response('No semester parameter or parameter is out of range', status=status.HTTP_400_BAD_REQUEST)
        try:
            Timetable.objects.get(group = group, semester = semester)
            return Response('Timetable is created', status = status.HTTP_200_OK)
        except Timetable.DoesNotExist:
            timetable = Timetable.objects.create(group = group, semester = semester)
            lessons = Lesson.objects.filter(group = group, semester = semester).order_by('day', 'class_number')
            year = group.entrance_year + semester // 2
            if semester % 2 == 0:
                first_date = datetime.date(year, 2, 9)
                end_date = datetime.date(year, 5, 31)
            else:
                first_date = datetime.date(year, 9, 1)
                end_date = datetime.date(year, 12, 30)


            first_week_number = first_date.isocalendar()[1]
            end_week_number = end_date.isocalendar()[1]
            first_week_start = first_date - datetime.timedelta(days = first_date.weekday())
            end_week_start = end_date - datetime.timedelta(days = end_date.weekday())

            for lesson in lessons:
                start_and_end = start_and_end_of_lesson(lesson.class_number)
                day = first_week_start+datetime.timedelta(days=lesson.day-1)
                if first_date.isoweekday() <= lesson.day: #если первое занятие попадает в первую неделю семестра
                    week_in_timetable, created = WeekInTimetable.objects.get_or_create(week_number = first_week_number, timetable = timetable)
                    day_in_timetable, created = DayInTimetable.objects.get_or_create(date = day, weekday = lesson.day, week = week_in_timetable)
                    lsn = LessonInTimeTable.objects.create(lesson = lesson, start = datetime.datetime.combine(day, start_and_end[0]), end = datetime.datetime.combine(day, start_and_end[1]), day = day_in_timetable)
                    print(lsn.start)
                    print(lsn.end)
                for week in range(first_week_number + 1, end_week_number):
                    day += datetime.timedelta(days=7)
                    week_in_timetable, created = WeekInTimetable.objects.get_or_create(week_number = week, timetable = timetable)
                    day_in_timetable, created = DayInTimetable.objects.get_or_create(date = day, weekday = lesson.day, week = week_in_timetable)
                    LessonInTimeTable.objects.create(lesson = lesson, start = datetime.datetime.combine(day, start_and_end[0]), end = datetime.datetime.combine(day, start_and_end[1]), day = day_in_timetable)
                if end_date.isoweekday() >= lesson.day: #если последнее занятие попадает в последнюю неделю семестра
                    day = end_week_start+datetime.timedelta(days=lesson.day-1)
                    week_in_timetable, created = WeekInTimetable.objects.get_or_create(week_number = end_week_number, timetable = timetable)
                    day_in_timetable, created = DayInTimetable.objects.get_or_create(date = day, weekday = lesson.day, week = week_in_timetable)
                    LessonInTimeTable.objects.create(lesson = lesson, start = datetime.datetime.combine(day, start_and_end[0]), end = datetime.datetime.combine(day, start_and_end[1]), day = day_in_timetable)

            timetable.save()
            return Response('Timetable is created', status = status.HTTP_200_OK)


class LessonInTimetableListDay(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, CanViewTimetable)
    serializer_class = LessonInTimetableSerializer

    def get_queryset(self):
        group = self.request.user.student.group
        semester = self.kwargs['semester']
        week_number = self.kwargs['week_number']
        day_number = self.kwargs['day_number']
        timetable = Timetable.objects.get(group = group, semester = semester)
        week = timetable.weekintimetable_set.filter(week_number = week_number)[0]
        day = week.dayintimetable_set.filter(weekday = day_number)[0]
        return day.lessonintimetable_set

    def get(self, request, *args, **kwargs):
        try:
            value = self.list(request, *args, **kwargs)
        except Timetable.DoesNotExist:
            return Response('Timetable does not exit', status = status.HTTP_404_NOT_FOUND)
        except IndexError:
            return Response('There is no such week or day', status = status.HTTP_404_NOT_FOUND)
        return value

