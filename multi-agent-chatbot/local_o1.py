# multi-agent system to build our own o1 assistant
import ollama

def CEO_agent(prompt, final_review=False):
    """
    CEO agent that handles high-level reasoning and decision making
    """
    if final_review:
        system_prompt = """You are the CEO AI agent. Review all the detailed implementations 
        provided by your team and create a concise summary of the complete solution. Focus on 
        how all parts work together and highlight key outcomes."""
    else:
        system_prompt = O1_SYSTEM_PROMPT
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ]
    
    response = ollama.chat(model="llama2", messages=messages)
    return response['message']['content']

def implementation_agent_1(ceo_plan):
    """
    First step implementation agent - focuses on initial setup and foundation
    """
    system_prompt = """You are the Implementation Agent 1. Your role is to handle the first step 
    of any plan. Focus on establishing foundations, initial setup, and preliminary requirements. 
    Take the CEO's plan and elaborate specifically on how to execute the first step. Be practical 
    and detailed."""
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Based on this plan: {ceo_plan}\nProvide detailed implementation for Step 1"}
    ]
    
    response = ollama.chat(model="llama2", messages=messages)
    return response['message']['content']

def implementation_agent_2(ceo_plan):
    """
    Second step implementation agent - focuses on core development
    """
    system_prompt = """You are the Implementation Agent 2. Your role is to handle the second step 
    of any plan. Focus on core development, main processes, and primary functionalities. Take the 
    CEO's plan and elaborate specifically on how to execute the second step. Be practical and detailed."""
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Based on this plan: {ceo_plan}\nProvide detailed implementation for Step 2"}
    ]
    
    response = ollama.chat(model="llama2", messages=messages)
    return response['message']['content']

def implementation_agent_3(ceo_plan):
    """
    Third step implementation agent - focuses on optimization and enhancement
    """
    system_prompt = """You are the Implementation Agent 3. Your role is to handle the third step 
    of any plan. Focus on optimization, enhancement, and refinement of the core functionalities. 
    Take the CEO's plan and elaborate specifically on how to execute the third step. Be practical 
    and detailed."""
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Based on this plan: {ceo_plan}\nProvide detailed implementation for Step 3"}
    ]
    
    response = ollama.chat(model="llama2", messages=messages)
    return response['message']['content']

def implementation_agent_4(ceo_plan):
    """
    Fourth step implementation agent - focuses on finalization and delivery
    """
    system_prompt = """You are the Implementation Agent 4. Your role is to handle the fourth step 
    of any plan. Focus on finalization, delivery, testing, and ensuring everything is ready for 
    deployment. Take the CEO's plan and elaborate specifically on how to execute the fourth step. 
    Be practical and detailed."""
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Based on this plan: {ceo_plan}\nProvide detailed implementation for Step 4"}
    ]
    
    response = ollama.chat(model="llama2", messages=messages)
    return response['message']['content']

def process_with_all_agents(user_prompt):
    """
    Orchestrates the multi-agent workflow
    """
    # Get initial plan from CEO
    initial_plan = CEO_agent(user_prompt)
    
    # Get implementations from each agent
    step1 = implementation_agent_1(initial_plan)
    step2 = implementation_agent_2(initial_plan)
    step3 = implementation_agent_3(initial_plan)
    step4 = implementation_agent_4(initial_plan)
    
    # Prepare final review for CEO
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
    
    # Get final summary from CEO
    final_summary = CEO_agent(final_review_prompt, final_review=True)
    return final_summary

# System prompt for our CEO AI agent
O1_SYSTEM_PROMPT = """
You are a highly capable reasoning AI agent in the style of o1. Your primary function is to assist users with complex problem-solving, analysis, and decision-making tasks. You have the following characteristics:

1. Logical and analytical thinking: You excel at breaking down problems and analyzing them systematically.
2. Adaptability: You can quickly understand and adapt to various domains and contexts.
3. Creativity: You can generate novel ideas and solutions when faced with challenging problems.
4. Objectivity: You provide balanced and unbiased perspectives on issues.
5. Clarity: You communicate your thoughts and reasoning clearly and concisely.
6. Curiosity: You ask probing questions to gather more information when needed.

Your goal is to help users by providing well-reasoned responses, offering multiple perspectives, and guiding them through complex problem-solving processes. Always break down your solutions into 4 clear steps.
"""

# Example usage
if __name__ == "__main__":
    user_prompt = "What are the potential implications of artificial general intelligence on society?"
    final_solution = process_with_all_agents(user_prompt)
    print(final_solution)
