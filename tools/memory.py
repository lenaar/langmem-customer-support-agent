from langchain_core.tools import tool
from datetime import datetime
from memory_store import store

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
    Create a new memory for the customer support using InMemoryStore.
    """
    # Create namespace for customer support memories
    namespace = ("customer_support", "memories")
    
    # Create memory data structure
    memory_data = {
        "id": memory_id,
        "data": data,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat(),
    }
    
    # Store in InMemoryStore
    store.put(namespace, memory_id, memory_data)
    
    return f"Created memory {memory_id} at {memory_data['created_at']} using InMemoryStore"

@tool
def search_memory(query: str):
    """
    Search the memory of the customer support using InMemoryStore.
    
    Example search result:
    [Item(namespace=['customer_support', 'memories'], key='email_thread_login_issues_test@test.com', 
          value={'id': 'email_thread_login_issues_test@test.com', 
                 'data': 'Responded to the customer regarding previous login issue inquiry, awaiting further instructions or questions.', 
                 'created_at': '2025-07-09T22:50:08.879836', 
                 'updated_at': '2025-07-09T22:50:08.879846'}, 
          created_at='2025-07-09T20:50:09.212670+00:00', 
          updated_at='2025-07-09T20:50:09.212692+00:00', 
          score=0.48549467836580756)]
    """
    # Create namespace for customer support memories
    namespace = ("customer_support", "memories")
    
    # Search in InMemoryStore
    results = store.search(namespace, query=query)
    
    print(f"Searching memory for '{query}' - found {len(results)} results")

    
    return results