from rest_framework import permissions


class IsUserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj == request.user


class IsUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user


class CanViewTimetable(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.has_perm('student_groups.view_timetable')
    def has_permission(self, request, view):
        return request.user.has_perm('student_groups.view_timetable')

class CanViewGrouplist(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.has_perm('student_groups.view_grouplist')
    def has_permission(self, request, view):
        return request.user.has_perm('student_groups.view_grouplist')

class CanViewNews(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.has_perm('student_groups.view_news')
    def has_permission(self, request, view):
        return request.user.has_perm('student_groups.view_news')

class CanViewHomeworks(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.has_perm('student_groups.view_homeworks')
    def has_permission(self, request, view):
        return request.user.has_perm('student_groups.view_homeworks')


class CanViewDocuments(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.has_perm('student_groups.view_documents')
    def has_permission(self, request, view):
        return request.user.has_perm('student_groups.view_documents')

class CanAddAndEditNews(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.has_perm('student_groups.add_and_edit_news')
    def has_permission(self, request, view):
        return request.user.has_perm('student_groups.add_and_edit_news')

class CanAddAndEditDocuments(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.has_perm('student_groups.add_and_edit_documents')
    def has_permission(self, request, view):
        return request.user.has_perm('student_groups.add_and_edit_documents')

class CanPostComments(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.has_perm('student_groups.post_comments')
    def has_permission(self, request, view):
        return request.user.has_perm('student_groups.post_comments')

class CanAddAndEditHomeworks(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.has_perm('student_groups.add_and_edit_homeworks')
    def has_permission(self, request, view):
        return request.user.has_perm('student_groups.add_and_edit_homeworks')

class CanAddAndEditTeachers(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.has_perm('student_groups.add_and_edit_teachers')
    def has_permission(self, request, view):
        return request.user.has_perm('student_groups.add_and_edit_teachers')

class CanAddAndEditSubjects(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.has_perm('student_groups.add_and_edit_subjects')
    def has_permission(self, request, view):
        return request.user.has_perm('student_groups.add_and_edit_subjects')

class CanEditTimetable(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.has_perm('student_groups.edit_timetable')
    def has_permission(self, request, view):
        return request.user.has_perm('student_groups.edit_timetable')

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.has_perm('student_groups.edit_others_news_homeworks_documents')

class CanChangePermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.has_perm('student_groups.change_permissions')
    def has_permission(self, request, view):
        return request.user.has_perm('student_groups.change_permissions')

class IsUserOrCanDeleteUsers(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.has_perm('student_groups.delete_users')
"""
permissions = (
            ("view_timetable", "Can see timetable of the group"), # groups: 'registered', 'students', 'group admin'
            ("view_grouplist", "Can see the list of students in the group"), # groups: 'registered', 'students', 'group admin'
            ("view_news", "Can see news of the group"), # groups: 'students', 'group admin'
            ("view_homeworks", "Can see homeworks"), # groups: 'students', 'group admin'
            ("view_documents", "Can see documents"), # groups: 'students', 'group admin'
            ("add_and_edit_news", "Can add and edit news of the group"), # groups: 'students', 'group admin'
            ("add_and_edit_documents", "Can add and edit documents"), # groups: 'students', 'group admin'
            ("post_comments", "Can post comments"), # groups: 'students', 'group admin'
            ("add_and_edit_homeworks", "Can add and edit homeworks"), # groups: 'students', 'group admin'
            ("add_and_edit_teachers", "Can add and edit teachers"), # groups: 'group admin'
            ("add_and_edit_subjects", "Can add and edit subjects"), # groups: 'group admin'
            ("edit timetable", "Can edit timetable"), # groups: 'group admin'
            ("edit_others_news_homeworks_documents", "Can edit news, homeworks and documents created by other users"), # groups: 'group admin'
            ("change_permissions", "Can change permissions"), # groups: 'group admin'
            ("delete_users", "Can delete users"), # groups: 'group admin'
        )
"""