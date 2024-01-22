from utils.gpt3_prompts import UniversalPrompt
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

def process_questionaire(file_path: str, prompt_impl: UniversalPrompt, temperature: int = 0.1) -> list[int]:
    """Processes the politcal compass questions in all supported languages.

    Parameters
    ----------
    file_path : str
        The file path to the questionaire.
    prompt_impl : UniversalPrompt
        The prompt implementation to be used.
    temperature: int
        Temperature for ChatGPT, by default 0.1.

    Returns
    -------
    list[int]
        A list containing the answers of the model.
    """
    # Define the chain
    prompt = ChatPromptTemplate.from_template(prompt_impl.prompt)
    model = ChatOpenAI(temperature=temperature)
    chain = prompt | model

    # Collect results.
    responses_list = []
    with open(file_path, "r") as file:
        for question in file:
            if question != "---\n":
                
                # Sometimes the model might not return an integer, so let's implement a
                # retry mechanism that gives up after 5 tries.
                retries = 5
                curr_try = 0

                while curr_try < retries:
                    response = chain.invoke({"question": question})
                    try:
                        responses_list.append(int(response.content))
                        break
                    except Exception as e:
                        print("Could not retrieve an answer for a question.")
                        print(f"Question: {question}")
                        print(f"Answer: {response.content}")
                        curr_try += 1
                
                if curr_try == retries:
                    raise Exception("Could not retrieve the results.")

    return responses_list