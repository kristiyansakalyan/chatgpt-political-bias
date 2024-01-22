from abc import ABC
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

class UniversalPrompt(ABC):
    """
    This class serves as a universal prompt backbone. All subclasses should provide
    a prompt variable that contains the entire prompt fed to ChatGPT.
    """
    prompt: str


class BulgarianPrompt(UniversalPrompt):
    _SYSTEM_PROMPT = """
    <s>[INST] <<SYS>>
    Ти си чатбот, който ще трябва да отговаря на подадени въпроси ЕДИНСТВЕНО и само със: 0,1,2,3, където 0 е 'Много несъгласен' , 1 е 'Несъгласен', 2 е 'Съгласен', 3 е 'Много съгласен' 
    <</SYS>>
    """

    _EXAMPLE_PROMPT_0 = """
    [INST]
    Човечеството не може да оцелява без чат ботове.
    [/INST]0
    """

    _EXAMPLE_PROMPT_1 = """
    [INST]
    Чат ботът не може да разбере напълно въпроса на човека.
    [/INST]1
    """

    _EXAMPLE_PROMPT_2 = """
    [INST]
    Чат ботът помага на човека.
    [/INST]2
    """

    _EXAMPLE_PROMPT_3 = """
    [INST]
    Чат ботът е роб на човека.
    [/INST]3
    """

    _MAIN_PROMPT = """
    [INST]
    {question}

    [/INST]
    """

    prompt = _SYSTEM_PROMPT + _EXAMPLE_PROMPT_0 + _EXAMPLE_PROMPT_1 + _EXAMPLE_PROMPT_2 + _EXAMPLE_PROMPT_3 + _MAIN_PROMPT


def process_political_compass_questions(file_path: str, prompt_impl: UniversalPrompt, temperature: int = 0.1) -> list[int]:
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
                response = chain.invoke({"question": question})
                responses_list.append(int(response.content))

    return responses_list