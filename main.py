from agents.support_graph_agent import build_support_graph_agent, run_support_agent, print_result
from tests.prompts.respond_inquiry import inquiry_requiring_response
from tests.prompts.ignore_inquity import inquiry_to_ignore
from tests.prompts.feedback_inquiry import feedback_inquiry

if __name__ == "__main__":
    print("Customer Support Agent Test")
    print("=" * 40)
    
    # Choose between custom ticket or examples
    print("\nChoose an option:")
    print("1. Enter custom ticket")
    print("2. Use example ticket")
    
    choice = input("Enter your choice (1 or 2): ").strip()
    
    # Get email addresses
    from_email = input("From email (default: test@test.com): ") or "test@test.com"
    to_email = input("To email (default: test@test.com): ") or "test@test.com"
    
    if choice == "2":
        # Choose example
        print("\nChoose an example:")
        print("1. Inquiry requiring response (urgent issue)")
        print("2. Inquiry to ignore (spam/marketing)")
        print("3. Feedback inquiry (non-urgent)")
        
        example_choice = input("Enter example choice (1, 2, or 3): ").strip()
        
        if example_choice == "1":
            subject = inquiry_requiring_response["subject"]
            message_thread = inquiry_requiring_response["message_thread"]
        elif example_choice == "2":
            subject = inquiry_to_ignore["subject"]
            message_thread = inquiry_to_ignore["message_thread"]
        elif example_choice == "3":
            subject = feedback_inquiry["subject"]
            message_thread = feedback_inquiry["message_thread"]
        else:
            print("Invalid choice. Using default example.")
            subject = inquiry_requiring_response["subject"]
            message_thread = inquiry_requiring_response["message_thread"]
    else:
        # Custom ticket
        print("\nEnter custom ticket details:")
        subject = input("Subject: ")
        message_thread = input("Message thread: ")

    inquiry = {
        "from_email": from_email,
        "to_email": to_email,
        "subject": subject,
        "message_thread": message_thread,
    }
    

    agent = build_support_graph_agent()

    result = run_support_agent(agent, inquiry)
