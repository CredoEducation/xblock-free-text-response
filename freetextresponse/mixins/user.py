"""
Extend XBlock with additional user functionality
"""


# pylint: disable=too-few-public-methods
class MissingDataFetcherMixin(object):
    """
    The mixin used for getting the student_id of the current user.
    """
    def get_student_id(self):
        """
        Get the student id.
        """
        if hasattr(self, 'xmodule_runtime'):
            user_service = self.runtime.service(self, 'user')
            student_id = user_service.get_current_user().opt_attrs.get('edx-platform.anonymous_user_id')
        else:
            student_id = self.scope_ids.user_id or ''
        return student_id
