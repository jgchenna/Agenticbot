from src.langgraphagentical.state.state import State

class BasicChatbotNode:
    """Node for the basic chatbot functionality."""
    
    def __init__(self, model):
        self.llm = model

    def process(self,state:State)-> dict:
        """Builds the basic chatbot node."""
        # Here you would define the logic for the basic chatbot node
        return {"messages": self.llm.invoke(state['messages']) }