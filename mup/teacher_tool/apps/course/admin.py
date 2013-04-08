from django.contrib import admin
from teacher_tool.apps.course.models import Course, Lesson, StudentsResults


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 0


class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "start_date", "end_date", "is_active")
    list_filter = ("is_active", )
    list_editable = ("is_active", )
    inlines = (LessonInline, )


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
admin.site.register(StudentsResults)
