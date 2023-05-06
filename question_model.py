import data  # Data where questions come from

class Question:
    """
    A class representing a single question and its answer.

    Attributes:
        _question (str): The text of the question.
        _answer (str): The text of the answer.
        questions (list[Question]): A list of all created Question instances.

    Methods:
        __init__(self, question: str, answer: str) -> None
        question(self) -> str
        answer(self) -> str
        __str__(self) -> str
        add_question(cls, text: str, answer: str) -> None
        list_questions(cls) -> None
    """

    questions = []

    def __init__(self, question: str, answer: str) -> None:
        """
        Initializes a new Question instance with the given question and answer.

        Args:
            question (str): The text of the question.
            answer (str): The text of the answer.
        """
        self._question = question
        self._answer = answer

    @property
    def question(self) -> str:
        """
        Returns the text of the question.
        """
        return self._question

    @property
    def answer(self) -> str:
        """
        Returns the text of the answer.
        """
        return self._answer

    def __str__(self) -> str:
        """
        Returns a string representation of the Question instance, including the question and answer text.
        """
        return f'Q: {self._question}\nA: {self._answer}'

    @classmethod
    def add_question(cls, text: str, answer: str) -> None:
        """
        Adds a new Question instance to the questions list with the given question and answer.

        Args:
            text (str): The text of the question.
            answer (str): The text of the answer.
        """
        q = Question(text, answer)
        cls.questions.append(q)

    @classmethod
    def list_questions(cls) -> None:
        """
        Prints out all the questions and answers in the questions list.
        """
        for q in cls.questions:
            print(q)


