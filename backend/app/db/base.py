from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# Import models so SQLAlchemy registers metadata.
from app.models.attempt import Attempt  # noqa: E402,F401
from app.models.conversation import Conversation, Message  # noqa: E402,F401
from app.models.document import Document  # noqa: E402,F401
from app.models.quiz import Question, Quiz  # noqa: E402,F401
from app.models.user import User  # noqa: E402,F401
