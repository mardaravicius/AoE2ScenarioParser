from binary_file_parser.retrievers import RetrieverRef

from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.datasets.trigger_data import DiplomacyStance
from AoE2ScenarioParser.datasets.triggers import EffectType
from AoE2ScenarioParser.sections.bfp.triggers.effect_struct import EffectStruct

from AoE2ScenarioParser.objects.data_objects.effects.effect import Effect


class ChangeDiplomacy(Effect):
    _type_ = EffectType.CHANGE_DIPLOMACY

    source_player: Player = RetrieverRef(EffectStruct._source_player)  # type: ignore
    """The player to change the diplomacy stance for"""
    target_player: Player = RetrieverRef(EffectStruct._target_player)  # type: ignore
    """The player to change the diplomacy stance towards"""
    diplomacy_stance: DiplomacyStance = RetrieverRef(EffectStruct._diplomacy)  # type: ignore
    """The new diplomacy stance"""

    # @overload
    # def __init__(self, source_player: Player, target_player: Player, diplomacy_stance: DiplomacyStance): ...

    def __init__(
        self,
        source_player: Player,
        target_player: Player,
        diplomacy_stance: DiplomacyStance,
        **kwargs,
    ):
        """
        Change the source_player's diplomacy_stance towards the target_player

        Args:
            source_player: The player to change the diplomacy stance for
            target_player: The player to change the diplomacy stance towards
            diplomacy_stance: The new diplomacy stance
        """
        super().__init__(local_vars = locals(), **kwargs)