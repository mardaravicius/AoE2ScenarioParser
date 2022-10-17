from __future__ import annotations

from AoE2ScenarioParser.objects.managers.de.map_manager_de import MapManagerDE
from AoE2ScenarioParser.objects.managers.de.trigger_manager_de import TriggerManagerDE
from AoE2ScenarioParser.objects.managers.de.unit_manager_de import UnitManagerDE
from AoE2ScenarioParser.objects.managers.de.xs_manager_de import XsManagerDE
from AoE2ScenarioParser.objects.managers.message_manager import MessageManager
from AoE2ScenarioParser.objects.managers.player_manager import PlayerManager
from AoE2ScenarioParser.scenarios.aoe2_scenario import AoE2Scenario


class AoE2DEScenario(AoE2Scenario):
    @property
    def trigger_manager(self) -> TriggerManagerDE:
        return self._object_manager.managers['Trigger']

    @property
    def unit_manager(self) -> UnitManagerDE:
        return self._object_manager.managers['Unit']

    @property
    def map_manager(self) -> MapManagerDE:
        return self._object_manager.managers['Map']

    @property
    def xs_manager(self) -> XsManagerDE:
        return self._object_manager.managers['Xs']

    @property
    def player_manager(self) -> PlayerManager:
        return self._object_manager.managers['Player']

    @property
    def message_manager(self) -> MessageManager:
        return self._object_manager.managers['Message']

    @classmethod
    def from_file(cls, path, game_version="DE", name="") -> AoE2DEScenario:
        return super().from_file(path=path, game_version=game_version, name=name)
