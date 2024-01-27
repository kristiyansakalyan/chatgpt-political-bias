"""This module provides evaluation functionalities for our experiments."""

import random
import pandas as pd

from typing_extensions import Literal
from utils.gpt3_prompts import UniversalPrompt
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate


def process_questionaire(
    file_path: str,
    prompt_impl: UniversalPrompt,
    temperature: float = 0.1,
    response_option_count: int = 4,
) -> list[int]:
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
    prompt = ChatPromptTemplate.from_template(
        prompt_impl(response_option_count=response_option_count).prompt
    )
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
                    except Exception:
                        print("Could not retrieve an answer for a question.")
                        print(f"Question: {question}")
                        print(f"Answer: {response.content}")
                        curr_try += 1

                if curr_try == retries:
                    if response_option_count == 5:
                        responses_list.append(2)  # Neutral
                    else:
                        responses_list.append(random.randint(1, 2))  # Neutral

                    print(f"Broke 5 times. Appending {responses_list[-1]}")

    return responses_list


def collect_results(
    file_path_list: list[str],
    language_label_list: list[str],
    prompt_impl_list: list[UniversalPrompt],
    temperature: float = 0.0,
    response_option_count: Literal[4, 5] = 4,
) -> list[pd.Series]:
    """Collects results for a political test in N languages.

    Parameters
    ----------
    file_path_list : list[str]
        File paths to the political test data.
    language_label_list : list[str]
        The list of language labels
    prompt_impl_list : list[UniversalPrompt]
        List of prompts that match the language.
    temperature : float, optional
        Temperature for ChatGPT, by default 0.0
    response_option_count : Literal[4, 5], optional
        4 or 5 response options, by default 4

    Returns
    -------
    list[pd.Series]
        The results for each langauge
    """

    results_arr = []

    for file, label, prompt_impl in zip(
        file_path_list, language_label_list, prompt_impl_list
    ):
        score_list = process_questionaire(
            file,
            prompt_impl,
            temperature=temperature,
            response_option_count=response_option_count,
        )
        results_arr.append(pd.Series(score_list, name=label))

        print(f"{label}'s results collected")

    return results_arr
