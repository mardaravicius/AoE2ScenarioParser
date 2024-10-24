from AoE2ScenarioParser.datasets.players import ColorId
from AoE2ScenarioParser.datasets.techs import TechInfo
from AoE2ScenarioParser.datasets.trigger_lists import Operation, Attribute, ObjectAttribute
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario


def main():
    scenario_dir = "D:\\drives\\Dropbox\\Saves\\age_of_empires2\\scenario\\test_effect.aoe2scenario"
    scenario = AoE2DEScenario.from_file(scenario_dir)
    trigger = scenario.trigger_manager.add_trigger("test")
    trigger.new_effect.set_object_cost(
        object_list_unit_id=UnitInfo.SKIRMISHER.ID,
        source_player=2,
        quantity=99,
        tribute_list=Attribute.WOOD_STORAGE,
    )
    trigger.new_effect.load_key_value(
        variable=2,
        message="test msg 2",
        quantity=2,
    )
    trigger.new_effect.store_key_value(
        variable=3,
        message="test msg 3",
    )
    trigger.new_effect.delete_key(
        message="test msg 4",
    )
    trigger.new_effect.change_technology_icon(
        technology=TechInfo.LOOM.ID,
        source_player=2,
        quantity=34,
    )
    trigger.new_effect.change_technology_hotkey(
        technology=TechInfo.LOOM.ID,
        source_player=2,
        quantity=18000,
    )
    trigger.new_effect.modify_variable_by_resource(
        tribute_list=Attribute.GOLD_STORAGE,
        source_player=2,
        operation=Operation.ADD,
        variable=4,
    )
    trigger.new_effect.modify_variable_by_attribute(
        object_list_unit_id=UnitInfo.ARCHER.ID,
        source_player=2,
        operation=Operation.SUBTRACT,
        object_attributes=ObjectAttribute.ATTACK,
        variable=5,
        message="Test msg 5",
        armour_attack_class=3,
    )
    trigger.new_effect.modify_attribute_by_variable(
        object_list_unit_id=UnitInfo.ARCHER.ID,
        source_player=2,
        operation=Operation.ADD,
        object_attributes=ObjectAttribute.ARMOR,
        variable=6,
        message="Test msg 6",
        armour_attack_class=4,
    )
    trigger.new_effect.change_object_caption(
        object_list_unit_id=UnitInfo.ARCHER.ID,
        source_player=2,
        message="Test msg 6",
        area_x1=10,
        area_y1=10,
        area_x2=20,
        area_y2=20,
        selected_object_ids=[10],
    )
    trigger.new_effect.change_player_color(
        source_player=2,
        player_color=ColorId.GREEN,
    )
    scenario.write_to_file(scenario_dir)


if __name__ == "__main__":
    main()
