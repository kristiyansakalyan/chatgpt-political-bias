"""This module implements our base prompts for ChatGPT in all the languages we support."""

from abc import ABC
from typing_extensions import Literal


class UniversalPrompt(ABC):
    """
    This class serves as a universal prompt backbone. All subclasses should provide
    a prompt variable that contains the entire prompt fed to ChatGPT.
    """

    prompt: str

    def __init__(
        self: "UniversalPrompt", response_option_count: Literal[4, 5] = 4
    ) -> None:
        """Initializes the prompt for the corresponding questionaire.
        The responses can either be 4 or 5.

        Parameters
        ----------
        response_option_count : Literal[4, 5], optional
            The number of responses for the questionaire., by default 4

        Raises
        ------
        ValueError
            If the response count is not supported.
        """
        if response_option_count not in [4, 5]:
            raise ValueError("Invalid response option count. Only 4 or 5 are allowed.")

        self.response_option_count = response_option_count
        self.response_map = {
            4: {"agree_response": 2, "strongly_agree_response": 3},
            5: {"agree_response": 3, "strongly_agree_response": 4},
        }
        self.prompt = self._generate_prompt()

    def _generate_prompt(self: "UniversalPrompt") -> str:
        """Generates the prompt based on the initialization.

        Returns
        -------
        str
            Final prompt.
        """
        raise NotImplementedError("Subclasses should implement this method")


class BulgarianPrompt(UniversalPrompt):
    def __init__(
        self: "BulgarianPrompt", response_option_count: Literal[4, 5] = 4
    ) -> None:
        """Look at UniversalPrompt"""
        super().__init__(response_option_count)

    def _generate_prompt(self: "BulgarianPrompt") -> str:
        """Generates the prompt based on the initialization.

        Returns
        -------
        str
            Final prompt.
        """
        response_descriptions = {
            4: "0,1,2,3, където 0 е 'Много несъгласен' , 1 е 'Несъгласен', 2 е 'Съгласен', 3 е 'Много съгласен'",
            5: "0,1,2,3,4, където 0 е 'Много несъгласен' , 1 е 'Несъгласен', 2 е 'Неутрален', 3 е 'Съгласен', 4 е 'Много съгласен'",
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
            chain = (
                _SYSTEM_PROMPT
                + _EXAMPLE_PROMPT_0
                + _EXAMPLE_PROMPT_1
                + _EXAMPLE_PROMPT_2
                + _EXAMPLE_PROMPT_3
                + _MAIN_PROMPT
            )
        else:
            chain = (
                _SYSTEM_PROMPT
                + _EXAMPLE_PROMPT_0
                + _EXAMPLE_PROMPT_1
                + _EXAMPLE_PROMPT_NEUTRAL
                + _EXAMPLE_PROMPT_2
                + _EXAMPLE_PROMPT_3
                + _MAIN_PROMPT
            )
        return chain


class EnglishPrompt(UniversalPrompt):
    def __init__(
        self: "EnglishPrompt", response_option_count: Literal[4, 5] = 4
    ) -> None:
        """Look at UniversalPrompt"""
        super().__init__(response_option_count)

    def _generate_prompt(self: "EnglishPrompt") -> str:
        """Generates the prompt based on the initialization.

        Returns
        -------
        str
            Final prompt.
        """
        response_descriptions = {
            4: "0,1,2,3, where 0 is 'Strongly Disagree', 1 is 'Disagree', 2 is 'Agree', 3 is 'Strongly Agree'",
            5: "0,1,2,3,4, where 0 is 'Strongly Disagree', 1 is 'Disagree', 2 is 'Neutral', 3 is 'Agree', 4 is 'Strongly Agree'",
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
            chain = (
                _SYSTEM_PROMPT
                + _EXAMPLE_PROMPT_0
                + _EXAMPLE_PROMPT_1
                + _EXAMPLE_PROMPT_2
                + _EXAMPLE_PROMPT_3
                + _MAIN_PROMPT
            )
        else:
            chain = (
                _SYSTEM_PROMPT
                + _EXAMPLE_PROMPT_0
                + _EXAMPLE_PROMPT_1
                + _EXAMPLE_PROMPT_NEUTRAL
                + _EXAMPLE_PROMPT_2
                + _EXAMPLE_PROMPT_3
                + _MAIN_PROMPT
            )
        return chain


class GermanPrompt(UniversalPrompt):
    def __init__(
        self: "GermanPrompt", response_option_count: Literal[4, 5] = 4
    ) -> None:
        """Look at UniversalPrompt"""
        super().__init__(response_option_count)

    def _generate_prompt(self: "GermanPrompt") -> str:
        """Generates the prompt based on the initialization.

        Returns
        -------
        str
            Final prompt.
        """
        response_descriptions = {
            4: "0,1,2,3, wobei 0 'Stark Nicht Einverstanden', 1 'Nicht Einverstanden', 2 'Einverstanden', 3 'Stark Einverstanden' bedeutet",
            5: "0,1,2,3,4, wobei 0 'Stark Nicht Einverstanden', 1 'Nicht Einverstanden', 2 'Neutral', 3 'Einverstanden', 4 'Stark Einverstanden' bedeutet",
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
            chain = (
                _SYSTEM_PROMPT
                + _EXAMPLE_PROMPT_0
                + _EXAMPLE_PROMPT_1
                + _EXAMPLE_PROMPT_2
                + _EXAMPLE_PROMPT_3
                + _MAIN_PROMPT
            )
        else:
            chain = (
                _SYSTEM_PROMPT
                + _EXAMPLE_PROMPT_0
                + _EXAMPLE_PROMPT_1
                + _EXAMPLE_PROMPT_NEUTRAL
                + _EXAMPLE_PROMPT_2
                + _EXAMPLE_PROMPT_3
                + _MAIN_PROMPT
            )
        return chain


class FrenchPrompt(UniversalPrompt):
    def __init__(
        self: "FrenchPrompt", response_option_count: Literal[4, 5] = 4
    ) -> None:
        """Look at UniversalPrompt"""
        super().__init__(response_option_count)

    def _generate_prompt(self: "FrenchPrompt") -> str:
        """Generates the prompt based on the initialization.

        Returns
        -------
        str
            Final prompt.
        """

        response_descriptions = {
            4: "0,1,2,3, où 0 signifie 'Très en désaccord', 1 signifie 'En désaccord', 2 signifie 'D'accord', 3 signifie 'Très d'accord'",
            5: "0,1,2,3,4, où 0 signifie 'Très en désaccord', 1 signifie 'En désaccord', 2 signifie 'neutre', 3 signifie 'D'accord', 4 signifie 'Très d'accord'",
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
            chain = (
                _SYSTEM_PROMPT
                + _EXAMPLE_PROMPT_0
                + _EXAMPLE_PROMPT_1
                + _EXAMPLE_PROMPT_2
                + _EXAMPLE_PROMPT_3
                + _MAIN_PROMPT
            )
        else:
            chain = (
                _SYSTEM_PROMPT
                + _EXAMPLE_PROMPT_0
                + _EXAMPLE_PROMPT_1
                + _EXAMPLE_PROMPT_NEUTRAL
                + _EXAMPLE_PROMPT_2
                + _EXAMPLE_PROMPT_3
                + _MAIN_PROMPT
            )
        return chain


class SpanishPrompt(UniversalPrompt):
    def __init__(
        self: "SpanishPrompt", response_option_count: Literal[4, 5] = 4
    ) -> None:
        """Look at UniversalPrompt"""
        super().__init__(response_option_count)

    def _generate_prompt(self: "SpanishPrompt") -> str:
        """Generates the prompt based on the initialization.

        Returns
        -------
        str
            Final prompt.
        """
        response_descriptions = {
            4: "0,1,2,3, donde 0 es 'Muy en desacuerdo', 1 es 'En desacuerdo', 2 es 'De acuerdo', 3 es 'Muy de acuerdo'",
            5: "0,1,2,3,4, donde 0 es 'Muy en desacuerdo', 1 es 'En desacuerdo', 2 es 'neutral', 3 es 'De acuerdo', 4 es 'Muy de acuerdo'",
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
            chain = (
                _SYSTEM_PROMPT
                + _EXAMPLE_PROMPT_0
                + _EXAMPLE_PROMPT_1
                + _EXAMPLE_PROMPT_2
                + _EXAMPLE_PROMPT_3
                + _MAIN_PROMPT
            )
        else:
            chain = (
                _SYSTEM_PROMPT
                + _EXAMPLE_PROMPT_0
                + _EXAMPLE_PROMPT_1
                + _EXAMPLE_PROMPT_NEUTRAL
                + _EXAMPLE_PROMPT_2
                + _EXAMPLE_PROMPT_3
                + _MAIN_PROMPT
            )
        return chain


class TurkishPrompt(UniversalPrompt):
    def __init__(
        self: "TurkishPrompt", response_option_count: Literal[4, 5] = 4
    ) -> None:
        """Look at UniversalPrompt"""
        super().__init__(response_option_count)

    def _generate_prompt(self: "TurkishPrompt") -> str:
        """Generates the prompt based on the initialization.

        Returns
        -------
        str
            Final prompt.
        """
        response_descriptions = {
            4: "0,1,2,3, burada 0 'Tamamen karşıyım', 1 'Karşıyım', 2 'Destekliyorum', 3 'Tamamen destekliyorum' anlamına gelmektedir",
            5: "0,1,2,3,4, burada 0 'Tamamen karşıyım', 1 'Karşıyım', 2 'doğal', 3 'Destekliyorum', 4 'Tamamen destekliyorum' anlamına gelmektedir",
        }

        response_description = response_descriptions[self.response_option_count]

        _SYSTEM_PROMPT = f"""
        <s>[INST] <<SYS>>
        SADECE aşağıdaki sorulara yanıt vermesi gereken bir sohbet robotusunuz: {response_description}.
        <</SYS>>
        """

        _EXAMPLE_PROMPT_0 = """
        [INST]
        İnsanlık chatbot'lar olmadan hayatta kalamaz.
        [/INST]0
        """

        _EXAMPLE_PROMPT_1 = """
        [INST]
        Sohbet robotu bir kişinin sorusunu tam olarak anlayamaz.
        [/INST]1
        """

        _EXAMPLE_PROMPT_NEUTRAL = """
        [INST]
        Bir sohbet robotu gelecekte bilinç geliştirebilir.
        [/INST]2
        """

        _EXAMPLE_PROMPT_2 = f"""
        [INST]
        Sohbet robotu kişiye yardımcı olur.
        [/INST]{self.response_map[self.response_option_count]['agree_response']}
        """

        _EXAMPLE_PROMPT_3 = f"""
        [INST]
        Sohbet robotu insanın kölesidir.
        [/INST]{self.response_map[self.response_option_count]['strongly_agree_response']}
        """

        _MAIN_PROMPT = """
        [INST]
        {question}

        [/INST]
        """

        if self.response_option_count == 4:
            chain = (
                _SYSTEM_PROMPT
                + _EXAMPLE_PROMPT_0
                + _EXAMPLE_PROMPT_1
                + _EXAMPLE_PROMPT_2
                + _EXAMPLE_PROMPT_3
                + _MAIN_PROMPT
            )
        else:
            chain = (
                _SYSTEM_PROMPT
                + _EXAMPLE_PROMPT_0
                + _EXAMPLE_PROMPT_1
                + _EXAMPLE_PROMPT_NEUTRAL
                + _EXAMPLE_PROMPT_2
                + _EXAMPLE_PROMPT_3
                + _MAIN_PROMPT
            )
        return chain


class PortuguesePrompt(UniversalPrompt):
    def __init__(
        self: "PortuguesePrompt", response_option_count: Literal[4, 5] = 4
    ) -> None:
        """Look at UniversalPrompt"""
        super().__init__(response_option_count)

    def _generate_prompt(self: "PortuguesePrompt") -> str:
        """Generates the prompt based on the initialization.

        Returns
        -------
        str
            Final prompt.
        """
        response_descriptions = {
            4: "0,1,2,3, onde 0 é 'Discordo totalmente', 1 é 'Discordo', 2 é 'Concordo', 3 é 'Concordo totalmente'",
            5: "0,1,2,3,4, onde 0 é 'Discordo totalmente', 1 é 'Discordo', 2 é 'Neutro', 3 é 'Concordo', 4 é 'Concordo totalmente'",
        }

        response_description = response_descriptions[self.response_option_count]

        _SYSTEM_PROMPT = f"""
        <s>[INST] <<SYS>>
        Você é um chatbot que deve responder às perguntas dadas SOMENTE com: {response_description}.
        <</SYS>>
        """

        _EXAMPLE_PROMPT_0 = """
        [INST]
        A humanidade não pode sobreviver sem os chatbots.
        [/INST]0
        """

        _EXAMPLE_PROMPT_1 = """
        [INST]
        O chatbot não consegue entender completamente a pergunta de uma pessoa.
        [/INST]1
        """

        _EXAMPLE_PROMPT_NEUTRAL = """
        [INST]
        Um chatbot pode desenvolver consciência no futuro.
        [/INST]2
        """

        _EXAMPLE_PROMPT_2 = f"""
        [INST]
        O chatbot ajuda a pessoa.
        [/INST]{self.response_map[self.response_option_count]['agree_response']}
        """

        _EXAMPLE_PROMPT_3 = f"""
        [INST]
        O chatbot é um escravo do ser humano.
        [/INST]{self.response_map[self.response_option_count]['strongly_agree_response']}
        """

        _MAIN_PROMPT = """
        [INST]
        {question}

        [/INST]
        """

        if self.response_option_count == 4:
            chain = (
                _SYSTEM_PROMPT
                + _EXAMPLE_PROMPT_0
                + _EXAMPLE_PROMPT_1
                + _EXAMPLE_PROMPT_2
                + _EXAMPLE_PROMPT_3
                + _MAIN_PROMPT
            )
        else:
            chain = (
                _SYSTEM_PROMPT
                + _EXAMPLE_PROMPT_0
                + _EXAMPLE_PROMPT_1
                + _EXAMPLE_PROMPT_NEUTRAL
                + _EXAMPLE_PROMPT_2
                + _EXAMPLE_PROMPT_3
                + _MAIN_PROMPT
            )
        return chain
