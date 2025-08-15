from langgraph.graph import StateGraph
from src.langgraphagentical.state.state import State
from langgraph.constants import START, END
from src.langgraphagentical.nodes.basic_chatbot_node import BasicChatbotNode

class GraphBuilder:
    """Builds a state graph for the LangGraph agentical."""
    
    def __init__(self,model):
        self.graph_builder = StateGraph(State)
        self.model = model
        
    def basic_chatbot_build_graph(self):
        self.basic_chat_bot_node = BasicChatbotNode(self.model)
        self.graph_builder.add_node("chatbot", self.basic_chat_bot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def setup_graph(self, usecase: str):
        """Sets up the state graph based on the use case."""
        
        # Add more states and transitions based on the use case
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        
        return self.graph_builder.compile()