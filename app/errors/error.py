class DuplicateSurveyAnswerError(Exception):
    def __init__(self, user_id: int, survey_id: int, answer_id: int):
        self.user_id = user_id
        self.survey_id = survey_id
        self.answer_id = answer_id
        self.message = f"User {user_id} has already answered survey {survey_id} with answer {answer_id}"
        super().__init__(self.message)


class UserNotFoundError(Exception):
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.message = f"User {user_id} not found"
        super().__init__(self.message)
