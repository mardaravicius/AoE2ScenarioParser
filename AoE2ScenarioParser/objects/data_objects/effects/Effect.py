from __future__ import annotations

from typing import Type

from binary_file_parser import BaseStruct, Retriever

from AoE2ScenarioParser.datasets.effects import EffectType
from AoE2ScenarioParser.sections.bfp.triggers.effect import Effect as EffectStruct


class Effect(EffectStruct):
    def __init__(
        self,
        struct_version: tuple[int, ...] = (3, 5, 1, 47),
        parent: BaseStruct = None,
        local_vars = None,
        **retriever_inits,
    ):
        if len(retriever_inits) > 0:
            super().__init__(struct_version, parent, **retriever_inits)
            return

        for ref in self._refs:
            name = (
                ref.retriever.p_name
                if isinstance(ref.retriever, Retriever)
                else ref.retriever.get_p_name(struct_version)
            )
            retriever_inits[name] = local_vars[ref.name]
        super().__init__(struct_version, parent, **retriever_inits)

    @staticmethod
    def _make_effect(struct: EffectStruct, type_: EffectType = EffectType.InvalidEffect) -> Effect:
        effect_cls: Type[Effect] = {
            EffectType.InvalidEffect: InvalidEffect,
        }[type_]

        return effect_cls(
            **{ref.name: None for ref in effect_cls._refs},
            struct_version = struct.struct_version,
            parent = struct.parent,
            **struct.retriever_name_value_map,
        )
