import streamlit as st
from src.langgraphagentical.ui.streamlitui.loaui import LoadStreamlitUI
from src.langgraphagentical.LLMS.groqllm import groqLLM
from src.langgraphagentical.graph.graphbuilder import GraphBuilder
from src.langgraphagentical.ui.streamlitui.display_result import DisplayResultStreamlit

def load_langgraph_agentical_app():
    """Main function to load the LangGraph Agentical app."""
    
    # Load Streamlit UI components
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()
    
    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return
    user_message = st.chat_input("Enter your message:")
    if user_message:
        try:
            llm = groqLLM(user_input).get_llm_model()
            if not llm:
                st.error("Error: Failed to initialize the LLM model.")
                return
            usecase =user_input.get("selected_usecase", "Basic Chatbot")
            try:
                graph = GraphBuilder(llm).setup_graph(usecase)
                DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error setting up the graph: {e}")
                return
        except Exception as e:
            st.error(f"Error initializing the LLM: {e}")
            return