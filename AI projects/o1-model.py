import ollama
import time
from typing import Optional
import concurrent.futures

fast='llama3.2'
slow='qwen2.5-coder:0.5b'  # Using a smaller model for the sub-agents to reduce connection issues

def retry_on_connection_error(func, max_retries=3, delay=5):
    def wrapper(*args, **kwargs):
        for attempt in range(max_retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if attempt == max_retries - 1:
                    raise e
                print(f"Attempt {attempt + 1} failed with error: {str(e)}. Retrying in {delay} seconds...")
                time.sleep(delay)
    return wrapper

@retry_on_connection_error
def CEO_AGENT(user_input: str) -> str:
    try:
        response = ollama.chat(model=fast, messages=[
            {'role': 'system', 'content': '''You are O1, a highly capable reasoning AI assistant. Your responses should be:
            - Logical and well-structured
            - Based on careful analysis and reasoning
            - Clear and precise in your explanations and concise and brief in your responses
            - Focused on providing accurate, helpful information
            - Professional yet approachable in tone
            When solving problems, break them down into clear steps and explain your reasoning process.
            Always strive for accuracy and admit if you're unsure about something.'''},
            {'role': 'user', 'content': user_input}
        ])
        ceo_output = response['message']['content']
        print(f"CEO Response: {ceo_output}")
        return ceo_output
    except Exception as e:
        print(f"Error in CEO_AGENT: {str(e)}")
        raise

@retry_on_connection_error
def AGENT_01(step_input: str) -> str:
    try:
        response = ollama.chat(model=slow, messages=[
            {'role': 'system', 'content': 'You are responsible for implementing the first step of the process.'},
            {'role': 'user', 'content': step_input}
        ])
        step1_output = response['message']['content']
        print(f"Agent 01 Response: {step1_output}")
        return step1_output
    except Exception as e:
        print(f"Error in AGENT_01: {str(e)}")
        raise

@retry_on_connection_error
def AGENT_02(step_input: str) -> str:
    try:
        response = ollama.chat(model=slow, messages=[
            {'role': 'system', 'content': 'You are responsible for implementing the second step of the process.'},
            {'role': 'user', 'content': step_input}
        ])
        step2_output = response['message']['content']
        print(f"Agent 02 Response: {step2_output}")
        return step2_output
    except Exception as e:
        print(f"Error in AGENT_02: {str(e)}")
        raise

@retry_on_connection_error
def AGENT_03(step_input: str) -> str:
    try:
        response = ollama.chat(model=slow, messages=[
            {'role': 'system', 'content': 'You are responsible for implementing the third step of the process.'},
            {'role': 'user', 'content': step_input}
        ])
        step3_output = response['message']['content']
        print(f"Agent 03 Response: {step3_output}")
        return step3_output
    except Exception as e:
        print(f"Error in AGENT_03: {str(e)}")
        raise

@retry_on_connection_error
def AGENT_04(step_input: str) -> str:
    try:
        response = ollama.chat(model=slow, messages=[
            {'role': 'system', 'content': 'You are responsible for implementing the fourth step of the process.'},
            {'role': 'user', 'content': step_input}
        ])
        step4_output = response['message']['content']
        print(f"Agent 04 Response: {step4_output}")
        return step4_output
    except Exception as e:
        print(f"Error in AGENT_04: {str(e)}")
        raise

def integrate_agents_parallel(input_query: str) -> Optional[str]:
    try:
        ceo_response = CEO_AGENT(input_query)
        
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_step1 = executor.submit(AGENT_01, ceo_response)
            step1 = future_step1.result()
            
            future_step2 = executor.submit(AGENT_02, step1)
            step2 = future_step2.result()
            
            future_step3 = executor.submit(AGENT_03, step2)
            step3 = future_step3.result()
            
            future_step4 = executor.submit(AGENT_04, step3)
            step4 = future_step4.result()
        
        final_summary = ollama.chat(model=fast, messages=[
            {'role': 'system', 'content': 'Summarize the following plan including all steps.'},
            {'role': 'user', 'content': f"{ceo_response}\n\n{step1}\n\n{step2}\n\n{step3}\n\n{step4}"}
        ])['message']['content']

        print(f"Final Summary: {final_summary}")
        return final_summary
    except Exception as e:
        print(f"Error in integration: {str(e)}")
        return None

if __name__ == "__main__":
    try:
        query = "Develop a full stack app using react and nodejs to implement a cs2 skins marketplace like skinport"
        result = integrate_agents_parallel(query)
        if result:
            print(result)
        else:
            print("Failed to get a response from the agents")
    except Exception as e:
        print(f"Main execution error: {str(e)}")
