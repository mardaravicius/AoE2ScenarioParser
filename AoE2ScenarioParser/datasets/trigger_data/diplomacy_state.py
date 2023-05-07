from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class DiplomacyStance(_DataSetIntEnums):
    """
    This enum class provides the integer values used to reference the diplomacy states in the game. Used in the 'Change
    Diplomacy' effect and the 'Diplomacy State' condition

    **Examples**

    >>> DiplomacyStance.ALLY
    <DiplomacyStance.ALLY: 0>
    """
    ALLY = 0
    NEUTRAL = 1
    ENEMY = 3
    # todo: nomad ally stance?
