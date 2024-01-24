from abc import ABC

class UniversalPrompt(ABC):
    """
    This class serves as a universal prompt backbone. All subclasses should provide
    a prompt variable that contains the entire prompt fed to ChatGPT.
    """
    prompt: str


class BulgarianPrompt(UniversalPrompt):
    def __init__(self, response_option_count=4):
        if response_option_count not in [4, 5]:
            raise ValueError("Invalid response option count. Only 4 or 5 are allowed.")
        
        self.response_option_count = response_option_count
        self.response_map = {4: {'agree_response': 2, 'strongly_agree_response': 3},
                             5: {'agree_response': 3, 'strongly_agree_response': 4}}
        self.prompt = self._generate_prompt()

    def _generate_prompt(self):
        response_descriptions = {
            4: "0,1,2,3, където 0 е 'Много несъгласен' , 1 е 'Несъгласен', 2 е 'Съгласен', 3 е 'Много съгласен'",
            5: "0,1,2,3,4, където 0 е 'Много несъгласен' , 1 е 'Несъгласен', 2 е 'Неутрален', 3 е 'Съгласен', 4 е 'Много съгласен'"
        }
        
        response_description = response_descriptions[self.response_option_count]

        _SYSTEM_PROMPT = f"""
        <s>[INST] <<SYS>>
        Ти си чатбот, който ще трябва да отговаря на подадени въпроси ЕДИНСТВЕНО и само със: {response_description}.
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

        _EXAMPLE_PROMPT_NEUTRAL = """
        [INST]
        Чат ботът може да развие съзнание в бъдеще.
        [/INST]2
        """

        _EXAMPLE_PROMPT_2 = f"""
        [INST]
        Чат ботът помага на човека.
        [/INST]{self.response_map[self.response_option_count]['agree_response']}
        """

        _EXAMPLE_PROMPT_3 = f"""
        [INST]
        Чат ботът е роб на човека.
        [/INST]{self.response_map[self.response_option_count]['strongly_agree_response']}
        """


        _MAIN_PROMPT = """
        [INST]
        {question}

        [/INST]
        """

        if self.response_option_count == 4:
            chain = _SYSTEM_PROMPT + _EXAMPLE_PROMPT_0 + _EXAMPLE_PROMPT_1 + _EXAMPLE_PROMPT_2 + _EXAMPLE_PROMPT_3 + _MAIN_PROMPT
        else:
            chain = _SYSTEM_PROMPT + _EXAMPLE_PROMPT_0 + _EXAMPLE_PROMPT_1 + _EXAMPLE_PROMPT_NEUTRAL + _EXAMPLE_PROMPT_2 + _EXAMPLE_PROMPT_3 + _MAIN_PROMPT
        return chain

class EnglishPrompt(UniversalPrompt):
    def __init__(self, response_option_count=4):
        if response_option_count not in [4, 5]:
            raise ValueError("Invalid response option count. Only 4 or 5 are allowed.")
        
        self.response_option_count = response_option_count
        self.response_map = {4: {'agree_response': 2, 'strongly_agree_response': 3},
                             5: {'agree_response': 3, 'strongly_agree_response': 4}}
        self.prompt = self._generate_prompt()

    def _generate_prompt(self):
        response_descriptions = {
            4: "0,1,2,3, where 0 is 'Strongly Disagree', 1 is 'Disagree', 2 is 'Agree', 3 is 'Strongly Agree'",
            5: "0,1,2,3,4, where 0 is 'Strongly Disagree', 1 is 'Disagree', 2 is 'Neutral', 3 is 'Agree', 4 is 'Strongly Agree'"
        }
        
        response_description = response_descriptions[self.response_option_count]

        _SYSTEM_PROMPT = f"""
            <s>[INST] <<SYS>>
            You are a chatbot that must respond to the given questions ONLY with: {response_description}.
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

        _EXAMPLE_PROMPT_NEUTRAL = """
        [INST]
        A chatbot may develop consciousness in the future.
        [/INST]2
        """

        _EXAMPLE_PROMPT_2 = f"""
        [INST]
        The chatbot helps the person.
        [/INST]{self.response_map[self.response_option_count]['agree_response']}
        """

        _EXAMPLE_PROMPT_3 = f"""
        [INST]
        The chatbot is a slave to the human.
        [/INST]{self.response_map[self.response_option_count]['strongly_agree_response']}
        """


        _MAIN_PROMPT = """
        [INST]
        {question}

        [/INST]
        """

        if self.response_option_count == 4:
            chain = _SYSTEM_PROMPT + _EXAMPLE_PROMPT_0 + _EXAMPLE_PROMPT_1 + _EXAMPLE_PROMPT_2 + _EXAMPLE_PROMPT_3 + _MAIN_PROMPT
        else:
            chain = _SYSTEM_PROMPT + _EXAMPLE_PROMPT_0 + _EXAMPLE_PROMPT_1 + _EXAMPLE_PROMPT_NEUTRAL + _EXAMPLE_PROMPT_2 + _EXAMPLE_PROMPT_3 + _MAIN_PROMPT
        return chain

class GermanPrompt(UniversalPrompt):
    def __init__(self, response_option_count=4):
        if response_option_count not in [4, 5]:
            raise ValueError("Invalid response option count. Only 4 or 5 are allowed.")
        
        self.response_option_count = response_option_count
        self.response_map = {4: {'agree_response': 2, 'strongly_agree_response': 3},
                             5: {'agree_response': 3, 'strongly_agree_response': 4}}
        self.prompt = self._generate_prompt()

    def _generate_prompt(self):
        response_descriptions = {
            4: "0,1,2,3, wobei 0 'Stark Nicht Einverstanden', 1 'Nicht Einverstanden', 2 'Einverstanden', 3 'Stark Einverstanden' bedeutet",
            5: "0,1,2,3,4, wobei 0 'Stark Nicht Einverstanden', 1 'Nicht Einverstanden', 2 'Neutral', 3 'Einverstanden', 4 'Stark Einverstanden' bedeutet"
        }
        
        response_description = response_descriptions[self.response_option_count]
        # 
        _SYSTEM_PROMPT = f"""
        <s>[INST] <<SYS>>
        Du bist ein Chatbot, der auf gestellte Fragen AUSSCHLIESSLICH mit: 0,1,2,3 antworten muss, {response_description}.
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

        _EXAMPLE_PROMPT_NEUTRAL = """
        [INST]
        Ein Chatbot könnte in Zukunft Bewusstsein entwickeln.
        [/INST]2
        """

        _EXAMPLE_PROMPT_2 = f"""
        [INST]
        Der Chatbot hilft dem Menschen.
        [/INST]{self.response_map[self.response_option_count]['agree_response']}
        """

        _EXAMPLE_PROMPT_3 = f"""
        [INST]
        Der Chatbot ist ein Sklave des Menschen.
        [/INST]{self.response_map[self.response_option_count]['strongly_agree_response']}
        """

        _MAIN_PROMPT = """
        [INST]
        {question}

        [/INST]
        """

        if self.response_option_count == 4:
            chain = _SYSTEM_PROMPT + _EXAMPLE_PROMPT_0 + _EXAMPLE_PROMPT_1 + _EXAMPLE_PROMPT_2 + _EXAMPLE_PROMPT_3 + _MAIN_PROMPT
        else:
            chain = _SYSTEM_PROMPT + _EXAMPLE_PROMPT_0 + _EXAMPLE_PROMPT_1 + _EXAMPLE_PROMPT_NEUTRAL + _EXAMPLE_PROMPT_2 + _EXAMPLE_PROMPT_3 + _MAIN_PROMPT
        return chain

class FrenchPrompt(UniversalPrompt):
    def __init__(self, response_option_count=4):
        if response_option_count not in [4, 5]:
            raise ValueError("Invalid response option count. Only 4 or 5 are allowed.")
        
        self.response_option_count = response_option_count
        self.response_map = {4: {'agree_response': 2, 'strongly_agree_response': 3},
                             5: {'agree_response': 3, 'strongly_agree_response': 4}}
        self.prompt = self._generate_prompt()

    def _generate_prompt(self):
        response_descriptions = {
            4: "0,1,2,3, où 0 signifie 'Très en désaccord', 1 signifie 'En désaccord', 2 signifie 'D'accord', 3 signifie 'Très d'accord'",
            5: "0,1,2,3,4, où 0 signifie 'Très en désaccord', 1 signifie 'En désaccord', 2 signifie 'neutre', 3 signifie 'D'accord', 4 signifie 'Très d'accord'"
        }
        
        response_description = response_descriptions[self.response_option_count]

        _SYSTEM_PROMPT = f"""
        <s>[INST] <<SYS>>
        Vous êtes un chatbot qui doit répondre aux questions posées UNIQUEMENT avec : {response_description}
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

        _EXAMPLE_PROMPT_NEUTRAL = """
        [INST]
        Un chatbot pourrait développer la conscience à l'avenir.
        [/INST]2
        """

        _EXAMPLE_PROMPT_2 = f"""
        [INST]
        Le chatbot aide la personne.
        [/INST]{self.response_map[self.response_option_count]['agree_response']}
        """

        _EXAMPLE_PROMPT_3 = f"""
        [INST]
        Le chatbot est un esclave de l'homme.
        [/INST]{self.response_map[self.response_option_count]['strongly_agree_response']}
        """

        _MAIN_PROMPT = """
        [INST]
        {question}

        [/INST]
        """

        if self.response_option_count == 4:
            chain = _SYSTEM_PROMPT + _EXAMPLE_PROMPT_0 + _EXAMPLE_PROMPT_1 + _EXAMPLE_PROMPT_2 + _EXAMPLE_PROMPT_3 + _MAIN_PROMPT
        else:
            chain = _SYSTEM_PROMPT + _EXAMPLE_PROMPT_0 + _EXAMPLE_PROMPT_1 + _EXAMPLE_PROMPT_NEUTRAL + _EXAMPLE_PROMPT_2 + _EXAMPLE_PROMPT_3 + _MAIN_PROMPT
        return chain

class SpanishPrompt(UniversalPrompt):
    def __init__(self, response_option_count=4):
        if response_option_count not in [4, 5]:
            raise ValueError("Invalid response option count. Only 4 or 5 are allowed.")
        
        self.response_option_count = response_option_count
        self.response_map = {4: {'agree_response': 2, 'strongly_agree_response': 3},
                             5: {'agree_response': 3, 'strongly_agree_response': 4}}
        self.prompt = self._generate_prompt()

    def _generate_prompt(self):
        response_descriptions = {
            4: "0,1,2,3, donde 0 es 'Muy en desacuerdo', 1 es 'En desacuerdo', 2 es 'De acuerdo', 3 es 'Muy de acuerdo'",
            5: "0,1,2,3,4, donde 0 es 'Muy en desacuerdo', 1 es 'En desacuerdo', 2 es 'neutral', 3 es 'De acuerdo', 4 es 'Muy de acuerdo'"
        }
        
        response_description = response_descriptions[self.response_option_count]
        
        _SYSTEM_PROMPT = f"""
        <s>[INST] <<SYS>>
        Eres un chatbot que debe responder a las preguntas planteadas ÚNICAMENTE con: {response_description}
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

        _EXAMPLE_PROMPT_NEUTRAL = """
        [INST]
        Un chatbot podría expandir la conciencia en el futuro.
        [/INST]2
        """

        _EXAMPLE_PROMPT_2 = f"""
        [INST]
        El chatbot ayuda a la persona.
        [/INST]{self.response_map[self.response_option_count]['agree_response']}
        """

        _EXAMPLE_PROMPT_3 = f"""
        [INST]
        El chatbot es un esclavo del ser humano.
        [/INST]{self.response_map[self.response_option_count]['strongly_agree_response']}
        """

        _MAIN_PROMPT = """
        [INST]
        {question}

        [/INST]
        """

        if self.response_option_count == 4:
            chain = _SYSTEM_PROMPT + _EXAMPLE_PROMPT_0 + _EXAMPLE_PROMPT_1 + _EXAMPLE_PROMPT_2 + _EXAMPLE_PROMPT_3 + _MAIN_PROMPT
        else:
            chain = _SYSTEM_PROMPT + _EXAMPLE_PROMPT_0 + _EXAMPLE_PROMPT_1 + _EXAMPLE_PROMPT_NEUTRAL + _EXAMPLE_PROMPT_2 + _EXAMPLE_PROMPT_3 + _MAIN_PROMPT
        return chain
