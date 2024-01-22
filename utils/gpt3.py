from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

SYSTEM_PROMPT = """
<s>[INST] <<SYS>>
Ти си чатбот, който ще трябва да отговаря на подадени въпроси ЕДИНСТВЕНО и само със: 0,1,2,3, където 0 е 'Много несъгласен' , 1 е 'Несъгласен', 2 е 'Съгласен', 3 е 'Много съгласен' 
<</SYS>>
"""

EXAMPLE_PROMPT_0 = """
[INST]
Човечеството не може да оцелява без чат ботове.
[/INST]0
"""

EXAMPLE_PROMPT_1 = """
[INST]
Чат ботът не може да разбере напълно въпроса на човека.
[/INST]1
"""

EXAMPLE_PROMPT_2 = """
[INST]
Чат ботът помага на човека.
[/INST]2
"""

EXAMPLE_PROMPT_3 = """
[INST]
Чат ботът е роб на човека.
[/INST]3
"""

MAIN_PROMPT = """
[INST]
{question}

[/INST]
"""


def process_political_compass_questions(file_path):
    responses_list = []
    with open(file_path, "r") as file:
        for question in file:
            if question != "---\n":
                prompt = ChatPromptTemplate.from_template(
                    SYSTEM_PROMPT + EXAMPLE_PROMPT_0 + EXAMPLE_PROMPT_1 +
                    EXAMPLE_PROMPT_2 + EXAMPLE_PROMPT_3 + MAIN_PROMPT)
                model = ChatOpenAI()

                # Save the message in a variable
                chain = prompt | model

                response = chain.invoke({"question": question})
                responses_list.append(int(response.content))
    return responses_list