from binary_file_parser.retrievers import RetrieverRef
from testing.sections.effects.Effect import Effect
from testing.sections.TriggerData import Effect as EffectStruct


class ResearchTechnology(Effect):
    """
    Research a technology for the source player
    """
    force = RetrieverRef(EffectStruct.force_research_technology)
    source_player = RetrieverRef(EffectStruct._source_player)
    technology = RetrieverRef(EffectStruct._technology)
