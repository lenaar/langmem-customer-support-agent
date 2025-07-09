from agents.state import State
from prompts.prompts import triage_user_prompt, triage_system_prompt
from agents.model_classifier import model_classifier
from profile_1 import get_profile
from prompts.triage_instructions import get_triage_instructions
from langgraph.types import Command
from typing import Literal

def triage_classifier(state: State) -> Command[Literal["response_agent", "__end__"]]:
    from_email = state["inquiry"]["from_email"]
    to_email = state["inquiry"]["to_email"]
    subject = state["inquiry"]["subject"]
    message_thread = state["inquiry"]["message_thread"]

    user_prompt = triage_user_prompt.format(from_email=from_email, to_email=to_email, subject=subject, message_thread=message_thread)

    profile = get_profile()
    instructions = get_triage_instructions(profile["full_name"])

    system_prompt = triage_system_prompt.format(
        full_name=profile["full_name"],
        profile_background=profile["profile_background"],
        triage_ignore=instructions["triage_rules"]["ignore"],
        triage_notify=instructions["triage_rules"]["notify"],
        triage_respond=instructions["triage_rules"]["respond"],
        examples=None
    )

    classifier = model_classifier.invoke(
        [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    classification = classifier.classification

    if classification == "respond":
        print("--------------------------------")
        print("Response needed")
        print("--------------------------------")

        return Command(
            goto="response_agent", 
            # update what state changes should be made when transitioning to the next agent
            update={
                "messages": [
                    {
                        "role": "user",
                        "content": f"Respond to the custormer inquiry, message thread: {message_thread}.Subject {subject}. From {from_email}."
                    }
                ]
            }
        )
    
    print(f"Triage classification: {classification}")
    print("No response needed")

    return Command(goto="__end__")