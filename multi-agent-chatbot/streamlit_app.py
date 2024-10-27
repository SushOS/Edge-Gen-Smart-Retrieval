import streamlit as st
from local_o1 import process_with_all_agents, CEO_agent, implementation_agent_1, implementation_agent_2, implementation_agent_3, implementation_agent_4

st.set_page_config(page_title="O1 Multi-Agent Assistant", page_icon="🤖", layout="wide")

st.title("O1 Multi-Agent Assistant")
st.markdown("*An AI system powered by multiple specialized agents*")

# User input
user_prompt = st.text_area("Enter your question or problem:", height=100)

# Add a process button
if st.button("Process with All Agents"):
    if user_prompt:
        with st.spinner("Processing with all agents..."):
            # Create tabs for detailed view
            tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
                "CEO Initial Plan", 
                "Implementation 1", 
                "Implementation 2", 
                "Implementation 3", 
                "Implementation 4",
                "Final Summary"
            ])
            
            # Get initial plan
            with tab1:
                st.markdown("### Initial Plan")
                initial_plan = CEO_agent(user_prompt)
                st.write(initial_plan)
            
            # Get implementations
            with tab2:
                st.markdown("### Step 1: Foundation & Setup")
                step1 = implementation_agent_1(initial_plan)
                st.write(step1)
                
            with tab3:
                st.markdown("### Step 2: Core Development")
                step2 = implementation_agent_2(initial_plan)
                st.write(step2)
                
            with tab4:
                st.markdown("### Step 3: Optimization")
                step3 = implementation_agent_3(initial_plan)
                st.write(step3)
                
            with tab5:
                st.markdown("### Step 4: Finalization")
                step4 = implementation_agent_4(initial_plan)
                st.write(step4)
            
            # Final summary
            with tab6:
                st.markdown("### Final Summary")
                final_review_prompt = f"""
                Original Plan:
                {initial_plan}
                
                Step 1 Implementation:
                {step1}
                
                Step 2 Implementation:
                {step2}
                
                Step 3 Implementation:
                {step3}
                
                Step 4 Implementation:
                {step4}
                
                Please provide a comprehensive summary of the complete solution.
                """
                final_summary = CEO_agent(final_review_prompt, final_review=True)
                st.write(final_summary)
    else:
        st.warning("Please enter a prompt first.")

# Add footer
st.markdown("---")
st.markdown("*Built with Streamlit and Ollama*")
