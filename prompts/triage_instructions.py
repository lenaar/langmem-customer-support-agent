

def get_triage_instructions(name: str = "John"):
    return {
        "triage_rules": {
            "ignore": "Spam, rude, offensive, or other inappropriate messages. Marketing, sales, or other promotional messages. Non-customer messages.",
            "notify": "Feedback, product feedback, or other non-urgent customer messages.",
            "respond": "Help with the product, technical support, urgent issues, account problems, or other customer messages.",
        },
        "agent_instructions": f" Use these tools to help {name} to provide the best possible support service and answer customer questions efficiently."
    }

classification_description = """
The classification of the message is based on the following rules: 
"ignore" for spam, rude, offensive, or other inappropriate messages. 
"notify" for important messages that does not require an immediate response such as feedback, product feedback. 
"respond" that requires a response to help with the product, technical support, urgent issues, account problems, or other customer messages.
"""

classification = {
    "description": classification_description
}

