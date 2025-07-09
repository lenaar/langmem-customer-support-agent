from typing import Annotated
from langgraph.graph import add_messages
from typing_extensions import TypedDict

class State(TypedDict):
    inquiry: dict
    messages: Annotated[list, add_messages]