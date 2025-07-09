# LangMem Customer Support Agent

A customer support agent with memory that automatically classifies inquiries, creates tickets, and maintains conversation history using LangGraph and OpenAI.

## Quick Start

### Install

```bash
git clone <repository-url>
cd langmem-customer-support-agent
pip install -r requirements.txt
cp env.example .env
# Add your OpenAI API key to .env
```

### Run

```bash
python main.py
```

## Usage

Choose from the menu:

1. **Custom ticket** - Enter your own support request
2. **Example ticket** - Test with predefined scenarios
3. **Search memory** - Find previous customer interactions
4. **Exit**

### Example

```
Step 1. Choose option: 2 (Example ticket)
Step 2. Choose example: 1 (Login issues)

✅ Agent automatically:
- Searches for customer history
- Creates support ticket
- Sends personalized reply
- Stores interaction in memory

Choose option: 3 (Search memory)
Enter query: login issues

✅ Found previous interaction:
- Customer: test@test.com
- Issue: Login problems
- Status: Awaiting response
```

## How It Works

1. **Triage Agent** classifies incoming messages (ignore/notify/respond)
2. **Response Agent** processes requests using tools (create tickets, send replies)
3. **Memory System** automatically stores all interactions for future reference
4. **Search** finds relevant customer history using semantic similarity

### Agent Components

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  Triage Agent   │───▶│ Response Agent  │───▶│  Memory Store   │
│                 │    │                 │    │                 │
│ • Classifies    │    │ • Uses Tools    │    │ • InMemoryStore │
│ • Routes        │    │ • Sends Replies │    │ • Vector Search │
│ • Updates State │    │ • Creates Memory│    │ • Persistence   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## Project Structure

```
├── agents/          # Agent workflow and classification
├── tools/           # Memory, ticket, and reply tools
├── prompts/         # System prompts and instructions
├── tests/           # Test scenarios
└── main.py          # Interactive interface
```

## Requirements

- Python 3.11+
- OpenAI API key
- LangGraph 0.4.0+

---

**Built with LangGraph, LangChain, and OpenAI**
