from langchain_core.tools import tool
from datetime import datetime

@tool
def create_ticket(customer_name: str, type: str, data: str) -> str:
    """
    Create a new ticket for the customer support.
    """

    id = "ticket_" + str(hash(data))[:8]
    ticket = {
        "id": id,
        "customer_name": customer_name,
        "type": type,
        "data": data,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat(),
    }
    return f"Created ticket {id} at {ticket['created_at']} "

@tool
def send_reply(to_email: str, type: str, body: str) -> str:
    """
    Send a reply to the customer.
    """
    return f"Sent reply to {to_email} at {datetime.now().isoformat()} "

