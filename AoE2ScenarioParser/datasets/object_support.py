from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class StartingAge(_DataSetIntEnums):
    """
    **This is not the same as the "Age" dataset and should !!NOT!! be used in effects/conditions etc.**

    This enum class provides the integer values used to reference the starting ages in the game.
    This is used in the player objects to set a starting age.

    **Examples**

    >>> StartingAge.POST_IMPERIAL_AGE
    <StartingAge.POST_IMPERIAL_AGE: 6>
    """
    DARK_AGE = 2
    FEUDAL_AGE = 3
    CASTLE_AGE = 4
    IMPERIAL_AGE = 5
    POST_IMPERIAL_AGE = 6


class Civilization(_DataSetIntEnums):
    """
    # TODO:
        This enum class provides the integer values used to reference the operations in the game. Used in a lot of effects
        like 'Modify Attribute' to control whether an attribute is set, added to, multiplied or divided by a value.

    **Examples**

    >>> Civilization.VIKINGS
    <Civilization.VIKINGS: 11>
    """
    BRITONS = 1
    FRANKS = 2
    GOTHS = 3
    TEUTONS = 4
    JAPANESE = 5
    CHINESE = 6
    BYZANTINES = 7
    PERSIANS = 8
    SARACENS = 9
    TURKS = 10
    VIKINGS = 11
    MONGOLS = 12
    CELTS = 13
    SPANISH = 14
    AZTECS = 15
    MAYANS = 16
    HUNS = 17
    KOREANS = 18
    ITALIANS = 19
    INDIANS = 20
    INCAS = 21
    MAGYARS = 22
    SLAVS = 23
    PORTUGUESE = 24
    ETHIOPIANS = 25
    MALIANS = 26
    BERBERS = 27
    KHMER = 28
    MALAY = 29
    BURMESE = 30
    VIETNAMESE = 31
    BULGARIANS = 32
    TATARS = 33
    CUMANS = 34
    LITHUANIANS = 35
    BURGUNDIANS = 36
    SICILIANS = 37
    POLES = 38
    BOHEMIANS = 39
    RANDOM = 40
    FULL_RANDOM = 42
