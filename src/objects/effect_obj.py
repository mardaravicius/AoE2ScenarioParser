from src.objects.aoe2_object import AoE2Object


class EffectObject(AoE2Object):
    def __init__(self,
                 effect_type,
                 ai_script_goal,
                 aa_quantity,
                 aa_armor_or_attack_type,
                 quantity,
                 tribute_list,
                 diplomacy,
                 number_of_units_selected,
                 object_list_unit_id,
                 player_source,
                 player_target,
                 technology,
                 string_id,
                 display_time,
                 trigger_id,
                 location_x,
                 location_y,
                 area_1_x,
                 area_1_y,
                 area_2_x,
                 area_2_y,
                 object_group,
                 object_type,
                 instruction_panel_position,
                 attack_stance,
                 time_unit,
                 enabled_or_victory,
                 food,
                 wood,
                 stone,
                 gold,
                 item_id,
                 flash_object,
                 force_research_technology,
                 visibility_state,
                 scroll,
                 operation,
                 object_list_unit_id_2,
                 button_location,
                 ai_signal_value,
                 object_attributes,
                 from_variable,
                 variable_or_timer,
                 facet,
                 play_sound,
                 message,
                 sound_name,
                 selected_object_id,
                 ):
        super().__init__(locals())
