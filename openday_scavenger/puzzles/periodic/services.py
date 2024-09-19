# from enum import Enum

# class PeriodicCategory(Enum):
#     AlkaliMetal = "AlkaliMetal"
#     AlkalineEarthMetal = "AlkalineEarthMetal"
#     TransitionMetal = "TransitionMetal"
#     PostTransitionMetal = "PostTransitionMetal"
#     Metalloid = "Metalloid"
#     ReactiveNonmetal = "ReactiveNonmetal"
#     NobleGas = "NobleGas"
#     Lanthanide = "Lanthanide"
#     Actinide = "Actinide"


def get_category_style(category: str):
    styles = {
        "AlkaliMetal": {
            "color": "#0C3BA0",
            "backgroundColor": "#DEF7FE",
        },
        "AlkalineEarthMetal": {
            "color": "#C4292E",
            "backgroundColor": "#FBE8E7",
        },
        "TransitionMetal": {
            "color": "#5A3EE3",
            "backgroundColor": "#F1E8FB",
        },
        "PostTransitionMetal": {
            "color": "#0E2B06",
            "backgroundColor": "#DDF8E9",
        },
        "Metalloid": {
            "color": "#8C591D",
            "backgroundColor": "#FDF7E2",
        },
        "ReactiveNonmetal": {
            "color": "#2163E7",
            "backgroundColor": "#E4EEFD",
        },
        "NobleGas": {
            "color": "#BC335F",
            "backgroundColor": "#FBE8EB",
        },
        "Lanthanide": {
            "color": "#113352",
            "backgroundColor": "#E3F2FE",
        },
        "Actinide": {
            "color": "#C24C00",
            "backgroundColor": "#FFEDE1",
        },
    }

    return styles.get(
        category,
        {
            "color": "#3E374D",
            "backgroundColor": "#E7E7EA",
        },
    )