from agents.state import State
from langgraph.graph import StateGraph, START, END
from agents.triage_agent import triage_classifier
from agents.response_agent import response_agent


def build_support_graph_agent():
    support_graph_agent = StateGraph(State)
    support_graph_agent.add_node("triage_agent", triage_classifier)
    support_graph_agent.add_node("response_agent", response_agent)

    support_graph_agent.add_edge(START, "triage_agent")
    support_graph_agent.add_edge("triage_agent", "response_agent")
    support_graph_agent.add_edge("triage_agent", END)
    support_graph_agent.add_edge("response_agent", END)

    support_agent = support_graph_agent.compile()

    return support_agent

def print_result(result):
    messages = result.get("messages", [])
    print("--------------------------------")
    for message in messages:
        if hasattr(message, "pretty_print"):
            message.pretty_print()
        else:
            content = message.get("content")
            print(f"{message['role']}: {message[:250]}")
    print("--------------------------------")

def run_support_agent(agent, inquiry: dict):
    config = {"configurable": {"langgraph_user_id": "123"}}

    try:
        result = agent.invoke({"inquiry": inquiry, "messages": []}, config=config)
        print_result(result)
        return result
    except Exception as e:
        print(f"Error running support agent: {e}")
        return None
    

