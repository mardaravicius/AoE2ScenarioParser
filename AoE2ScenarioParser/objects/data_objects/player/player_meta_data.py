from AoE2ScenarioParser.datasets.object_support import Civilization
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink


class PlayerMetaData(AoE2Object):
    """Object for handling a tile in the map."""

    _link_list = [
        RetrieverObjectLink("active", "DataHeader", "player_data_1[__index__].active"),
        RetrieverObjectLink("human", "DataHeader", "player_data_1[__index__].human"),
        RetrieverObjectLink("civilization", "DataHeader", "player_data_1[__index__].civilization"),
        RetrieverObjectLink("architecture_set", "DataHeader", "player_data_1[__index__].architecture_set"),
    ]

    def __init__(self, active: int, human: int, civilization: int, architecture_set: int, **kwargs):
        super().__init__(**kwargs)

        self.active: bool = bool(active)
        self.human: bool = bool(human)
        self.civilization: Civilization = Civilization(civilization)
        self.architecture_set: Civilization = Civilization(architecture_set)