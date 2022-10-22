
from typing import NamedTuple,TYPE_CHECKING

if TYPE_CHECKING:
    from AoE2ScenarioParser.sections.aoe2_file_section import AoE2FileSection


class ConstructProgress(NamedTuple):
    """a docstring"""
    section: 'AoE2FileSection'
    done: int

    __annotations__ = {'section': 'AoE2FileSection', 'done': int}
