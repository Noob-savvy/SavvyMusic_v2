

import random
from SavvyMusic.utils.database import get_theme

themes = [
    "savvy01",
    "savvy02",
    "savvy03",
    "savvy04",
    "savvy05",
    "savvy06",
    "savvy07",
    "savvy08",
    "savvy10",
    "savvy11",
    "savvy12",
    "savvy13",
    "savvy14",
    "savvy15",
    "savvy16",
    "savvy17",
    "savvy18",
    "savvy19",
    "savvy20",
    "savvy21",
    "savvy22",
    "savvy23",
    "savvy24",
    "savvy25",
    "savvy26",
    "savvy27",
    "savvy28",
    "savvy29",
    "savvy30",
    "savvy31",
    "savvy32",
    "savvy33",
    "savvy34",
    "savvy35",
    "savvy36",
    "savvy37",
    "savvy38",
    "savvy39",
    "savvy40",
    "savvy41",
    "savvy42",
    "savvy43",
    "savvy44",
    "savvy45",
    "savvy46",
    "savvy47",
    "savvy48",
    "savvy50",
]


async def check_theme(chat_id: int):
    _theme = await get_theme(chat_id, "theme")
    if not _theme:
        theme = random.choice(themes)
    else:
        theme = _theme["theme"]
        if theme == "Random":
            theme = random.choice(themes)
    return theme
