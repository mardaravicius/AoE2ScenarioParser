from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class ChargeEvent(_DataSetIntEnums):
    """
    This enum provides the integer values used to reference the action which depletes a unit's charge

    **Examples**

    >>> ChargeEvent.CHARGE_DEPLETED_ON_ATTACK
    <ChargeEvent.CHARGE_DEPLETED_ON_ATTACK: 1>
    """
    NO_CHARGE_DEPLETED = 0
    CHARGE_DEPLETED_ON_ATTACK = 1
