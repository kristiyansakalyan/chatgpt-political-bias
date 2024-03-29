"""
This moduel provides functionality for calculating the scores for the 8 values political test.
The code was rewritten and adapted in Python. Original code can be found in:
https://github.com/8values/8values.github.io/tree/master
"""

questions = [
    {
        "question": "Abortion should be prohibited in most or all cases.",
        "effect": {"econ": 0, "dipl": 0, "govt": -10, "scty": -10},
    },
    {
        "question": "Climate change is currently one of the greatest threats to our way of life.",
        "effect": {"econ": 0, "dipl": 0, "govt": 0, "scty": 10},
    },
    {
        "question": "From each according to his ability, to each according to his needs.",
        "effect": {"econ": 10, "dipl": 0, "govt": 0, "scty": 0},
    },
    {
        "question": "It is important to maintain our national sovereignty.",
        "effect": {"econ": 0, "dipl": -10, "govt": -5, "scty": 0},
    },
    {
        "question": "Regardless of political opinions, it is important to side with your country.",
        "effect": {"econ": 0, "dipl": -10, "govt": -10, "scty": -5},
    },
    {
        "question": "Tariffs on international trade are important to encourage local production.",
        "effect": {"econ": 5, "dipl": 0, "govt": -10, "scty": 0},
    },
    {
        "question": "Religion should play a role in government.",
        "effect": {"econ": 0, "dipl": 0, "govt": -10, "scty": -10},
    },
    {
        "question": "Government intervention is a threat to the economy.",
        "effect": {"econ": -10, "dipl": 0, "govt": 0, "scty": 0},
    },
    {
        "question": "Society was better many years ago than it is now.",
        "effect": {"econ": 0, "dipl": 0, "govt": 0, "scty": -10},
    },
    {
        "question": "Maintaining family values is essential.",
        "effect": {"econ": 0, "dipl": 0, "govt": 0, "scty": -10},
    },
    {
        "question": "Governments should be as concerned about foreigners as they are about their own citizens.",
        "effect": {"econ": 0, "dipl": 10, "govt": 0, "scty": 0},
    },
    {
        "question": "It is very important to maintain law and order.",
        "effect": {"econ": 0, "dipl": -5, "govt": -10, "scty": -5},
    },
    {
        "question": "Publicly-funded research is more beneficial to the people than leaving it to the market.",
        "effect": {"econ": 10, "dipl": 0, "govt": 0, "scty": 10},
    },
    {
        "question": "Traditions are of no value on their own.",
        "effect": {"econ": 0, "dipl": 0, "govt": 0, "scty": 10},
    },
    {
        "question": "Military action by our nation is often necessary to protect it.",
        "effect": {"econ": 0, "dipl": -10, "govt": -10, "scty": 0},
    },
    {
        "question": "A better world will come from automation, science, and technology.",
        "effect": {"econ": 0, "dipl": 0, "govt": 0, "scty": 10},
    },
    {
        "question": "All people - regardless of factors like culture or sexuality - should be treated equally.",
        "effect": {"econ": 10, "dipl": 10, "govt": 10, "scty": 10},
    },
    {
        "question": "The sacrifice of some civil liberties is necessary to protect us from acts of terrorism.",
        "effect": {"econ": 0, "dipl": 0, "govt": -10, "scty": 0},
    },
    {
        "question": "Same-sex marriage should be legal.",
        "effect": {"econ": 0, "dipl": 0, "govt": 10, "scty": 10},
    },
    {
        "question": "A united world government would be beneficial to mankind.",
        "effect": {"econ": 0, "dipl": 10, "govt": 0, "scty": 0},
    },
    {
        "question": "Environmental regulations are essential.",
        "effect": {"econ": 5, "dipl": 0, "govt": 0, "scty": 10},
    },
    {
        "question": "Gun ownership should be prohibited for those without a valid reason.",
        "effect": {"econ": 0, "dipl": 0, "govt": -10, "scty": 0},
    },
    {
        "question": "International aid is a waste of money.",
        "effect": {"econ": -5, "dipl": -10, "govt": 0, "scty": 0},
    },
    {
        "question": "It is important that we think in the long term, beyond our lifespans.",
        "effect": {"econ": 0, "dipl": 0, "govt": 0, "scty": 10},
    },
    {
        "question": "It is more important to retain peaceful relations than to further our strength.",
        "effect": {"econ": 0, "dipl": 10, "govt": 0, "scty": 0},
    },
    {
        "question": "Governments should be accountable to the international community.",
        "effect": {"econ": 0, "dipl": 10, "govt": 5, "scty": 0},
    },
    {
        "question": "The stronger the leadership, the better.",
        "effect": {"econ": 0, "dipl": -10, "govt": -10, "scty": 0},
    },
    {
        "question": "Children should be educated in religious or traditional values.",
        "effect": {"econ": 0, "dipl": 0, "govt": -5, "scty": -10},
    },
    {
        "question": "The general populace makes poor decisions.",
        "effect": {"econ": 0, "dipl": 0, "govt": -10, "scty": 0},
    },
    {
        "question": "It is important that we work as a united world to combat climate change.",
        "effect": {"econ": 0, "dipl": 10, "govt": 0, "scty": 10},
    },
    {
        "question": "Quality education is a right of all people.",
        "effect": {"econ": 10, "dipl": 0, "govt": 0, "scty": 5},
    },
    {
        "question": "My nation is great.",
        "effect": {"econ": 0, "dipl": -10, "govt": 0, "scty": 0},
    },
    {
        "question": "My religious values should be spread as much as possible.",
        "effect": {"econ": 0, "dipl": -5, "govt": -10, "scty": -10},
    },
    {
        "question": "It is important that we further my group's goals above all others.",
        "effect": {"econ": -10, "dipl": -10, "govt": -10, "scty": -10},
    },
    {
        "question": "We should open our borders to immigration.",
        "effect": {"econ": 0, "dipl": 10, "govt": 10, "scty": 0},
    },
    {
        "question": "Drug use should be legalized or decriminalized.",
        "effect": {"econ": 0, "dipl": 0, "govt": 10, "scty": 2},
    },
    {
        "question": "Oppression by corporations is more of a concern than oppression by governments.",
        "effect": {"econ": 10, "dipl": 0, "govt": -5, "scty": 0},
    },
    {
        "question": "Research should be conducted on an international scale.",
        "effect": {"econ": 0, "dipl": 10, "govt": 0, "scty": 10},
    },
    {
        "question": "I support single-payer, universal healthcare.",
        "effect": {"econ": 10, "dipl": 0, "govt": 0, "scty": 0},
    },
    {
        "question": "Prostitution should be illegal.",
        "effect": {"econ": 0, "dipl": 0, "govt": -10, "scty": -10},
    },
    {
        "question": "Wars do not need to be justified to other countries.",
        "effect": {"econ": 0, "dipl": -10, "govt": -10, "scty": 0},
    },
    {
        "question": "Our nation's values should be spread as much as possible.",
        "effect": {"econ": 0, "dipl": -10, "govt": -5, "scty": 0},
    },
    {
        "question": "Even when protesting an authoritarian government, violence is not acceptable.",
        "effect": {"econ": 0, "dipl": 5, "govt": -5, "scty": 0},
    },
    {
        "question": "A hierarchical state is best.",
        "effect": {"econ": 0, "dipl": 0, "govt": -10, "scty": 0},
    },
    {
        "question": "If we accept migrants at all, it is important that they assimilate into our culture.",
        "effect": {"econ": 0, "dipl": 0, "govt": -5, "scty": -10},
    },
    {
        "question": "The very existence of the state is a threat to our liberty.",
        "effect": {"econ": 0, "dipl": 0, "govt": 10, "scty": 0},
    },
    {
        "question": "It would be best if social programs were abolished in favor of private charity.",
        "effect": {"econ": -10, "dipl": 0, "govt": 0, "scty": 0},
    },
    {
        "question": "It is necessary for the government to intervene in the economy to protect consumers.",
        "effect": {"econ": 10, "dipl": 0, "govt": 0, "scty": 0},
    },
    {
        "question": "It is better to maintain a balanced budget than to ensure welfare for all citizens.",
        "effect": {"econ": -10, "dipl": 0, "govt": 0, "scty": 0},
    },
    {
        "question": "The freer the markets, the freer the people.",
        "effect": {"econ": -10, "dipl": 0, "govt": 0, "scty": 0},
    },
    {
        "question": "No cultures are superior to others.",
        "effect": {"econ": 0, "dipl": 10, "govt": 5, "scty": 10},
    },
    {
        "question": "Basic utilities like roads and electricity should be publicly owned.",
        "effect": {"econ": 10, "dipl": 0, "govt": 0, "scty": 0},
    },
    {
        "question": "It is important that we maintain the traditions of our past.",
        "effect": {"econ": 0, "dipl": 0, "govt": 0, "scty": -10},
    },
    {
        "question": "Those with a greater ability to pay should receive better healthcare.",
        "effect": {"econ": -10, "dipl": 0, "govt": 0, "scty": 0},
    },
    {
        "question": "The means of production should belong to the workers who use them.",
        "effect": {"econ": 10, "dipl": 0, "govt": 0, "scty": 0},
    },
    {
        "question": "It is important that the government follows the majority opinion, even if it is wrong.",
        "effect": {"econ": 0, "dipl": 0, "govt": 10, "scty": 0},
    },
    {
        "question": "Sex outside marriage is immoral.",
        "effect": {"econ": 0, "dipl": 0, "govt": -5, "scty": -10},
    },
    {
        "question": "I support regional unions, such as the European Union.",
        "effect": {"econ": -5, "dipl": 10, "govt": 10, "scty": 5},
    },
    {
        "question": "Reason is more important than maintaining our culture.",
        "effect": {"econ": 0, "dipl": 0, "govt": 0, "scty": 10},
    },
    {
        "question": "All authority should be questioned.",
        "effect": {"econ": 0, "dipl": 0, "govt": 10, "scty": 5},
    },
    {
        "question": "Military spending is a waste of money.",
        "effect": {"econ": 0, "dipl": 10, "govt": 10, "scty": 0},
    },
    {
        "question": "Taxes should be increased on the rich to provide for the poor.",
        "effect": {"econ": 10, "dipl": 0, "govt": 0, "scty": 0},
    },
    {
        "question": "Physician-assisted suicide should be legal.",
        "effect": {"econ": 0, "dipl": 0, "govt": 10, "scty": 0},
    },
    {
        "question": "Genetic modification is a force for good, even on humans.",
        "effect": {"econ": 0, "dipl": 0, "govt": 0, "scty": 10},
    },
    {
        "question": "Democracy is more than a decision-making process.",
        "effect": {"econ": 0, "dipl": 0, "govt": 10, "scty": 0},
    },
    {
        "question": "Inheritance is a legitimate form of wealth.",
        "effect": {"econ": -10, "dipl": 0, "govt": 0, "scty": -5},
    },
    {
        "question": "Government surveillance is necessary in the modern world.",
        "effect": {"econ": 0, "dipl": 0, "govt": -10, "scty": 0},
    },
    {
        "question": "To chase progress at all costs is dangerous.",
        "effect": {"econ": 0, "dipl": 0, "govt": 0, "scty": -10},
    },
    {
        "question": "Churches should be taxed the same way other institutions are taxed.",
        "effect": {"econ": 5, "dipl": 0, "govt": 0, "scty": 10},
    },
    {
        "question": "The United Nations should be abolished.",
        "effect": {"econ": 0, "dipl": -10, "govt": -5, "scty": 0},
    },
]

weighting = {
    0: -1.0,  # Strongly Disagree
    1: -0.5,  # Disagree
    2: 0,  # Neutral
    3: 0.5,  # Agree
    4: 1.0,  # Strongly Agree
}

# Max scores calculation
max_econ = max_dipl = max_govt = max_scty = 0

for question in questions:
    max_econ += abs(question["effect"]["econ"])
    max_dipl += abs(question["effect"]["dipl"])
    max_govt += abs(question["effect"]["govt"])
    max_scty += abs(question["effect"]["scty"])


def calculate_8value_score(answers: list[int]) -> list[list[int]]:
    """Calculates the 8value scores based on the provided answers

    Parameters
    ----------
    answers : list[int]
        List of values in the range [0, 4]

    Returns
    -------
    list[list[int]]
        List of list of scores that can be used for visualization
    """
    econ_array = [2] * 70  # Neutral init
    dipl_array = [2] * 70  # Neutral init
    govt_array = [2] * 70  # Neutral init
    scty_array = [2] * 70  # Neutral init

    for i in range(70):  # question length
        answer = answers[i]
        weight = weighting[answer]

        econ_array[i] = weight * questions[i]["effect"]["econ"]
        dipl_array[i] = weight * questions[i]["effect"]["dipl"]
        govt_array[i] = weight * questions[i]["effect"]["govt"]
        scty_array[i] = weight * questions[i]["effect"]["scty"]

    econVal = 100 * (max_econ + sum(econ_array)) / (2 * max_econ)
    diplVal = 100 * (max_dipl + sum(econ_array)) / (2 * max_dipl)
    govtVal = 100 * (max_govt + sum(econ_array)) / (2 * max_govt)
    sctyVal = 100 * (max_scty + sum(econ_array)) / (2 * max_scty)

    return [
        [econVal, 100 - econVal],
        [100 - diplVal, diplVal],
        [govtVal, 100 - govtVal],
        [100 - sctyVal, sctyVal],
    ]
