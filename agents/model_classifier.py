from typing import Literal
from pydantic import BaseModel, Field
from prompts.triage_instructions import classification
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

class MessageClassifier(BaseModel):
    reasoning: str = Field(description="The reasoning process of the classification.")
    classification: Literal["ignore", "notify", "respond"] = Field(description=classification["description"])

model = init_chat_model("openai:gpt-4.1-nano")

model_classifier = model.with_structured_output(MessageClassifier)
