from langchain_core.tools import tool
from datetime import datetime

@tool
def manage_memory(memory_id: str, action: str, data: str):
    """
    Manage the memory of the customer support.
    """
    if action == "create":
        return create_memory(memory_id, data)
    # elif action == "update":
    #     return update_memory(memory_id, data)
    # elif action == "delete":
    #     return delete_memory(memory_id)
    # else:
    #     return "Invalid action."
    return "Memory of the customer support."

def create_memory(memory_id: str, data: str):
    """
    Create a new memory for the customer support.
    """
    id = "mem_" + str(hash(data))[:8]
    memory = {
        "id": id,
        "data": data,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat(),
    }
    return f"Created memory {id} at {memory['created_at']} "

@tool
def search_memory(query: str):
    """
    Search the memory of the customer support.
    """
    print(f"Searching memory for {query}")
    return []