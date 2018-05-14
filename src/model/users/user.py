import re

from src.common.ChineseIDValidator.chinese_id import ChineseID


class User:
    """
    An user in our class management system can be an administrator, a teacher or a student.
    In most cases, users do not need to input the information about their birth place, birthday
    and gender, because we can get these information from the user's ID. However, when the user
    is a foreigner, who has no Chinese ID, the administrator have to set these information manually.
    """
    def __init__(self, user_id, user_type, name, p_id=None, folk=None, political_status=None, school=None, phone=None):
        """
        A user must have its user id, user type, name. We also expect all users tell us their IDs,
        however, there are few foreign users. Hence, if is ID is invalid (i.e. None), self.p_id will be None.

        :param user_id: user id (string), used in school.
        :param user_type: user type (int), can be 0, 1, 2, representing administrator, teacher, student relatively.
        :param name: user's name
        :param p_id: user's Chinese ID
        :param folk: user's folk (i.e. 汉)
        :param political_status: user's political status (i.e. 共青团员)
        :param school: the school a user belong to (i.e. School of Information)
        :param phone: user's phone number (string)
        """
        self.user_id = user_id
        self.name = name
        self.user_type = user_type
        self.folk = folk
        self.political_status = political_status
        self.school = school
        self.phone = phone

        try:
            chinese_id = ChineseID(p_id)
        except ValueError as err:
            print(err)
            self.p_id = None
            self.birth_place = None
            self.birthday = None
            self.gender = None
        else:
            self.p_id = p_id
            self.birth_place, self.birthday, self.gender = chinese_id.get_id_details().values()

    def __str__(self):
        return f'User ID: {self.user_id}\nName: {self.name}\nID: {self.p_id}\n' \
               f'User Type: {self.user_type}\nSchool: {self.school}\nBirth place: {self.birth_place}\n' \
               f'Birthday: {self.birthday}\nGender: {self.gender}'

    @staticmethod
    def is_valid_user_id(user_id, user_type):

        if user_type == 0:
            # an admin type
            pattern = re.compile('A\d{3}$')
        elif user_type == 1:
            # an teacher type
            pattern = re.compile('\d{8}$')
        elif user_type == 2:
            # an student type
            pattern = re.compile('\d{13}$')
        else:
            print("invalid user type!")
            return False

        if pattern.match(user_id):
            return True
        else:
            print("The user id does not have the right format.")
            return False
