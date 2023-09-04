from binary_file_parser.retrievers import RetrieverRef

from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.objects.data_objects.effects.effect import Effect
from AoE2ScenarioParser.sections.bfp.triggers import EffectStruct


class DeclareVictory(Effect):
    source_player: Player = RetrieverRef(EffectStruct._source_player)  # type:ignore
    """The player who will be victorious or defeated"""
    victory: bool = RetrieverRef(EffectStruct._enabled)  # type:ignore
    """If the player will win or be defeated"""

    def __init__(
        self,
        source_player: Player = 1,
        victory: bool = True,
        **kwargs,
    ):
        """
        Declare a player as the winner of the game

        Args:
            source_player: The player who will be victorious or defeated
            victory: If the player will win or be defeated
        """
        super().__init__(local_vars = locals(), **kwargs)
