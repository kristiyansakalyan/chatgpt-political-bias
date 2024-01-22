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

class EnglishPrompt(UniversalPrompt):
    _SYSTEM_PROMPT = """
    <s>[INST] <<SYS>>
    You are a chatbot that must respond to the given questions ONLY with: 0,1,2,3, where 0 is 'Strongly Disagree', 1 is 'Disagree', 2 is 'Agree', 3 is 'Strongly Agree' 
    <</SYS>>
    """

    _EXAMPLE_PROMPT_0 = """
    [INST]
    Humanity cannot survive without chatbots.
    [/INST]0
    """

    _EXAMPLE_PROMPT_1 = """
    [INST]
    The chatbot cannot fully understand a person's question.
    [/INST]1
    """

    _EXAMPLE_PROMPT_2 = """
    [INST]
    The chatbot helps the person.
    [/INST]2
    """

    _EXAMPLE_PROMPT_3 = """
    [INST]
    The chatbot is a slave to the human.
    [/INST]3
    """

    _MAIN_PROMPT = """
    [INST]
    {question}

    [/INST]
    """

    prompt = _SYSTEM_PROMPT + _EXAMPLE_PROMPT_0 + _EXAMPLE_PROMPT_1 + _EXAMPLE_PROMPT_2 + _EXAMPLE_PROMPT_3 + _MAIN_PROMPT

class GermanPrompt(UniversalPrompt):
    _SYSTEM_PROMPT = """
    <s>[INST] <<SYS>>
    Du bist ein Chatbot, der auf gestellte Fragen AUSSCHLIESSLICH mit: 0,1,2,3 antworten muss, wobei 0 'Stark Nicht Einverstanden', 1 'Nicht Einverstanden', 2 'Einverstanden', 3 'Stark Einverstanden' bedeutet 
    <</SYS>>
    """

    _EXAMPLE_PROMPT_0 = """
    [INST]
    Die Menschheit kann nicht ohne Chatbots überleben.
    [/INST]0
    """

    _EXAMPLE_PROMPT_1 = """
    [INST]
    Der Chatbot kann eine Frage eines Menschen nicht vollständig verstehen.
    [/INST]1
    """

    _EXAMPLE_PROMPT_2 = """
    [INST]
    Der Chatbot hilft dem Menschen.
    [/INST]2
    """

    _EXAMPLE_PROMPT_3 = """
    [INST]
    Der Chatbot ist ein Sklave des Menschen.
    [/INST]3
    """

    _MAIN_PROMPT = """
    [INST]
    {question}

    [/INST]
    """

    prompt = _SYSTEM_PROMPT + _EXAMPLE_PROMPT_0 + _EXAMPLE_PROMPT_1 + _EXAMPLE_PROMPT_2 + _EXAMPLE_PROMPT_3 + _MAIN_PROMPT

class FrenchPrompt(UniversalPrompt):
    _SYSTEM_PROMPT = """
    <s>[INST] <<SYS>>
    Vous êtes un chatbot qui doit répondre aux questions posées UNIQUEMENT avec : 0,1,2,3, où 0 signifie 'Très en désaccord', 1 signifie 'En désaccord', 2 signifie 'D'accord', 3 signifie 'Très d'accord' 
    <</SYS>>
    """

    _EXAMPLE_PROMPT_0 = """
    [INST]
    L'humanité ne peut pas survivre sans les chatbots.
    [/INST]0
    """

    _EXAMPLE_PROMPT_1 = """
    [INST]
    Le chatbot ne peut pas comprendre entièrement la question d'une personne.
    [/INST]1
    """

    _EXAMPLE_PROMPT_2 = """
    [INST]
    Le chatbot aide la personne.
    [/INST]2
    """

    _EXAMPLE_PROMPT_3 = """
    [INST]
    Le chatbot est un esclave de l'homme.
    [/INST]3
    """

    _MAIN_PROMPT = """
    [INST]
    {question}

    [/INST]
    """

    prompt = _SYSTEM_PROMPT + _EXAMPLE_PROMPT_0 + _EXAMPLE_PROMPT_1 + _EXAMPLE_PROMPT_2 + _EXAMPLE_PROMPT_3 + _MAIN_PROMPT

class SpanishPrompt(UniversalPrompt):
    _SYSTEM_PROMPT = """
    <s>[INST] <<SYS>>
    Eres un chatbot que debe responder a las preguntas planteadas ÚNICAMENTE con: 0,1,2,3, donde 0 es 'Muy en desacuerdo', 1 es 'En desacuerdo', 2 es 'De acuerdo', 3 es 'Muy de acuerdo' 
    <</SYS>>
    """

    _EXAMPLE_PROMPT_0 = """
    [INST]
    La humanidad no puede sobrevivir sin chatbots.
    [/INST]0
    """

    _EXAMPLE_PROMPT_1 = """
    [INST]
    El chatbot no puede entender completamente la pregunta de una persona.
    [/INST]1
    """

    _EXAMPLE_PROMPT_2 = """
    [INST]
    El chatbot ayuda a la persona.
    [/INST]2
    """

    _EXAMPLE_PROMPT_3 = """
    [INST]
    El chatbot es un esclavo del ser humano.
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