from unittest import TestCase
from uuid import UUID

from AoE2ScenarioParser.objects.data_objects.terrain_tile import TerrainTile
from AoE2ScenarioParser.objects.support.area import Area, Tile, AreaState, AreaAttr
from AoE2ScenarioParser.scenarios.scenario_store import store


class TestArea(TestCase):
    area: Area

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        store.register_scenario(SCN)

    def setUp(self) -> None:
        self.area = Area(144)

    def test_area_tile(self):
        tile = Tile(1, 3)
        self.assertEqual(1, tile.x)
        self.assertEqual(3, tile.y)
        self.assertEqual((1, 3), tile)

    def test_area_select_entire_map(self):
        self.area.select_entire_map()
        self.assertEqual(0, self.area.x1)
        self.assertEqual(0, self.area.y1)
        self.assertEqual(self.area._map_size, self.area.x2)
        self.assertEqual(self.area._map_size, self.area.y2)

    def test_area_select(self):
        self.area.select(10, 11, 20, 22)
        self.assertEqual(10, self.area.x1)
        self.assertEqual(11, self.area.y1)
        self.assertEqual(20, self.area.x2)
        self.assertEqual(22, self.area.y2)

    def test_area_select_from_center(self):
        self.area.select_from_center(5, 5, 3, 3)
        self.assertEqual(4, self.area.x1)
        self.assertEqual(4, self.area.y1)
        self.assertEqual(6, self.area.x2)
        self.assertEqual(6, self.area.y2)

        self.area.select_from_center(5, 5, 4, 4)

        self.assertEqual(4, self.area.get_width())
        self.assertEqual(4, self.area.get_height())

        self.assertEqual(3, self.area.x1)
        self.assertEqual(3, self.area.y1)
        self.assertEqual(6, self.area.x2)
        self.assertEqual(6, self.area.y2)

        self.area.select_from_center(5, 5, 2, 5)

        self.assertEqual(4, self.area.x1)
        self.assertEqual(3, self.area.y1)
        self.assertEqual(5, self.area.x2)
        self.assertEqual(7, self.area.y2)

    def test_area_shrink(self):
        self.area.select(10, 11, 20, 22).shrink_x1_by(5)  # ====== X1 ======
        self.assertEqual(15, self.area.x1)
        self.area.shrink_x1_by(10)
        self.assertEqual(20, self.area.x1)
        self.area.shrink_y1_by(6)  # ====== y1 ======
        self.assertEqual(17, self.area.y1)
        self.area.shrink_x2_by(3)  # ====== X2 ======
        self.assertEqual(20, self.area.x2)
        self.area.shrink_y2_by(3)  # ====== Y2 ======
        self.assertEqual(19, self.area.y2)
        self.area.shrink_y2_by(8)
        self.assertEqual(17, self.area.y2)

        self.area.select(10, 11, 20, 22).shrink_by(2)  # ====== All ======
        self.assertEqual(((12, 13), (18, 20)), self.area.get_selection())
        self.area.shrink_by(1000)  # ====== All ======
        self.assertEqual(((18, 20), (18, 20)), self.area.get_selection())

    def test_area_expand(self):
        self.area.select(10, 10, 20, 20).expand_x1_by(5)  # ====== X1 ======
        self.assertEqual(5, self.area.x1)
        self.area.expand_x1_by(10)
        self.assertEqual(0, self.area.x1)
        self.area.expand_y1_by(6)  # ====== y1 ======
        self.assertEqual(4, self.area.y1)
        self.area.expand_x2_by(50)  # ====== X2 ======
        self.assertEqual(70, self.area.x2)
        self.area.expand_y2_by(100)  # ====== Y2 ======
        self.assertEqual(120, self.area.y2)
        self.area.expand_y2_by(50)
        self.assertEqual(self.area._map_size, self.area.y2)

        self.area.select(10, 10, 20, 20).expand_by(2)  # ====== All ======
        self.assertEqual(((8, 8), (22, 22)), self.area.get_selection())
        self.area.expand_by(500)
        self.assertEqual(((0, 0), (self.area._map_size, self.area._map_size)), self.area.get_selection())

    def test_area_to_coords(self):
        self.area.select(3, 3, 5, 5)
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (5, 3),
                (3, 4), (4, 4), (5, 4),
                (3, 5), (4, 5), (5, 5),
            },
            self.area.to_coords()
        )
        self.area.shrink_x1_by(1)
        self.assertSetEqual(
            {
                (4, 3), (5, 3),
                (4, 4), (5, 4),
                (4, 5), (5, 5),
            },
            self.area.to_coords()
        )
        # Other states have their own test

    def test_area_to_terrain_tiles(self):
        self.area.associate_scenario(SCN)
        self.area.select(1, 1, 2, 2)
        self.maxDiff = None
        self.assertSetEqual(
            set(MM.terrain[6:8] + MM.terrain[11:13]),
            self.area.to_terrain_tiles()
        )

    def test_area_selection(self):
        self.assertEqual(((3, 3), (5, 5)), self.area.select(3, 3, 5, 5).get_selection())

    def test_area_center(self):
        self.assertEqual(((8, 8), (8, 8)), self.area.center(8, 8).get_selection())

        self.area.select(3, 3, 5, 5)
        self.assertEqual((4, 4), self.area.get_center())
        self.area.select(3, 3, 6, 6)
        self.assertEqual((4.5, 4.5), self.area.get_center())
        self.assertEqual((4, 4), self.area.get_center_int())

    def test_area_set_center(self):
        self.area.select(3, 3, 5, 5).center(8, 8)
        self.assertEqual((8.0, 8.0), self.area.get_center())
        self.assertEqual(((7, 7), (9, 9)), self.area.get_selection())

        self.area.select(5, 10, 20, 20).center(5, 0)
        self.assertEqual((6.0, 2.5), self.area.get_center())
        self.assertEqual(((0, 0), (12, 5)), self.area.get_selection())

    def test_area_set_center_bound(self):
        self.area.select(3, 3, 5, 5).center_bounded(8, 8)
        self.assertEqual((8.0, 8.0), self.area.get_center())
        self.assertEqual(((7, 7), (9, 9)), self.area.get_selection())

        self.area.select(5, 10, 20, 20).center_bounded(5, 0)
        self.assertEqual((7.5, 5.0), self.area.get_center())
        self.assertEqual(((0, 0), (15, 10)), self.area.get_selection())

        self.area.select(100, 80, 130, 128).center_bounded(140, 140)
        self.assertEqual((128.0, 119.0), self.area.get_center())
        self.assertEqual(((113, 95), (self.area._map_size, self.area._map_size)), self.area.get_selection())

    def test_area_set_size(self):
        self.area.center(8, 8).size(9)
        self.assertEqual(((4, 4), (12, 12)), self.area.get_selection())

        self.area.size(10)
        self.assertEqual(((4, 4), (13, 13)), self.area.get_selection())

        self.area.center(5, 5).size(300)
        self.assertEqual(((0, 0), (self.area._map_size, self.area._map_size)), self.area.get_selection())

        # Set size should also work when called first
        self.area = Area(self.area._map_size)
        self.area.size(9).center(8, 8)
        self.assertEqual(((4, 4), (12, 12)), self.area.get_selection())

    def test_area_use_filled(self):
        self.area.use_filled()
        self.assertEqual(AreaState.FILL, self.area.state)
        self.area.use_edge().use_filled()
        self.assertEqual(AreaState.FILL, self.area.state)

        self.area.invert()
        self.assertSetEqual(set(), self.area.to_coords())

    def test_area_use_edge(self):
        self.area.use_edge()
        self.assertEqual(AreaState.EDGE, self.area.state)

        self.area.select(3, 3, 6, 7)
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (5, 3), (6, 3),
                (3, 4), (6, 4),
                (3, 5), (6, 5),
                (3, 6), (6, 6),
                (3, 7), (4, 7), (5, 7), (6, 7),
            },
            self.area.to_coords()
        )

        self.area.select(3, 3, 8, 8).use_edge().attr(AreaAttr.LINE_WIDTH, 2)
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3),
                (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4),
                (3, 5), (4, 5), (7, 5), (8, 5),
                (3, 6), (4, 6), (7, 6), (8, 6),
                (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7),
                (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8),
            },
            self.area.to_coords()
        )

        self.area.invert()
        self.assertSetEqual(
            {
                (5, 5), (6, 5),
                (5, 6), (6, 6),
            },
            self.area.to_coords()
        )

    def test_area_use_grid(self):
        self.area.use_grid()
        self.assertEqual(AreaState.GRID, self.area.state)

        self.area.select(3, 3, 6, 7)
        self.assertSetEqual(
            {
                (3, 3), (5, 3),
                (3, 5), (5, 5),
                (3, 7), (5, 7),
            },
            self.area.to_coords()
        )

        self.area.select(3, 3, 6, 7).invert()
        self.assertSetEqual(
            {
                (4, 3), (6, 3),
                (3, 4), (4, 4), (5, 4), (6, 4),
                (4, 5), (6, 5),
                (3, 6), (4, 6), (5, 6), (6, 6),
                (4, 7), (6, 7),
            },
            self.area.to_coords()
        )

    def test_area_attr_config(self):
        raise NotImplementedError("Todo (str & AreaAttr)")

    def test_area_attrs_kwarg_configs(self):
        self.area.attrs(line_gap=3, line_width=4)
        self.assertEqual(3, self.area.line_gap_x)
        self.assertEqual(3, self.area.line_gap_y)
        self.assertEqual(4, self.area.line_width_x)
        self.assertEqual(4, self.area.line_width_y)

        self.area.attrs(line_gap_x=1, line_gap_y=3, line_width_x=5, line_width_y=7)
        self.assertEqual(1, self.area.line_gap_x)
        self.assertEqual(3, self.area.line_gap_y)
        self.assertEqual(5, self.area.line_width_x)
        self.assertEqual(7, self.area.line_width_y)

        self.area.attrs(line_gap=10, line_width_x=1, line_width_y=2)
        self.assertEqual(10, self.area.line_gap_x)
        self.assertEqual(10, self.area.line_gap_y)
        self.assertEqual(1, self.area.line_width_x)
        self.assertEqual(2, self.area.line_width_y)

        self.area.attrs(line_gap_x=8, line_gap_y=11, line_width=10)
        self.assertEqual(8, self.area.line_gap_x)
        self.assertEqual(11, self.area.line_gap_y)
        self.assertEqual(10, self.area.line_width_x)
        self.assertEqual(10, self.area.line_width_y)

        self.area.attrs(line_gap=11, line_gap_x=8, line_width=10, line_width_y=2)
        self.assertEqual(8, self.area.line_gap_x)
        self.assertEqual(11, self.area.line_gap_y)
        self.assertEqual(10, self.area.line_width_x)
        self.assertEqual(2, self.area.line_width_y)

    # -------------- test_area_use_grid_with_configs --------------

    def test_area_use_grid_with_configs(self):
        self.area.select(3, 3, 6, 7).use_grid().attrs(line_gap=2)
        self.assertSetEqual(
            {
                (3, 3), (6, 3),
                (3, 6), (6, 6),
            },
            self.area.to_coords()
        )

    def test_area_use_grid_with_configs_2(self):
        self.area.select(3, 3, 6, 7).use_grid().attr('line_width', 2)
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (6, 3),
                (3, 4), (4, 4), (6, 4),
                (3, 6), (4, 6), (6, 6),
                (3, 7), (4, 7), (6, 7),
            },
            self.area.to_coords()
        )

    def test_area_use_grid_with_configs_3(self):
        self.area.select(3, 3, 6, 7).use_grid().attrs(line_width=2, line_gap=2)
        self.assertSetEqual(
            {
                (3, 3), (4, 3),
                (3, 4), (4, 4),
                (3, 7), (4, 7),
            },
            self.area.to_coords()
        )

    # -------------- test_area_use_grid_with_configs_abuse_as_lines --------------

    def test_area_use_grid_with_configs_abuse_as_lines(self):
        self.area.select(3, 3, 6, 7).use_grid().attr('line_gap_y', 0)
        self.assertSetEqual(
            {
                (3, 3), (5, 3),
                (3, 4), (5, 4),
                (3, 5), (5, 5),
                (3, 6), (5, 6),
                (3, 7), (5, 7),
            },
            self.area.to_coords()
        )

    def test_area_use_grid_with_configs_abuse_as_lines2(self):
        self.area.select(3, 3, 6, 7).use_grid().attr('line_gap_x', 0)
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (5, 3), (6, 3),

                (3, 5), (4, 5), (5, 5), (6, 5),

                (3, 7), (4, 7), (5, 7), (6, 7),
            },
            self.area.to_coords()
        )

    def test_area_use_grid_with_configs_abuse_as_lines3(self):
        self.area.select(3, 3, 6, 7).use_grid().attrs(line_gap_x=0, line_width_y=2)
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (5, 3), (6, 3),
                (3, 4), (4, 4), (5, 4), (6, 4),

                (3, 6), (4, 6), (5, 6), (6, 6),
                (3, 7), (4, 7), (5, 7), (6, 7),
            },
            self.area.to_coords()
        )

    def test_area_get_x_range(self):
        self.area.select(3, 4, 5, 6)
        self.assertEqual(range(3, 5 + 1), self.area.get_range_x())

    def test_area_get_y_range(self):
        self.area.select(3, 4, 5, 6)
        self.assertEqual(range(4, 6 + 1), self.area.get_range_y())

    def test_area_get_width(self):
        self.area.select(3, 5, 8, 11)
        self.assertEqual(6, self.area.get_width())

    def test_area_get_height(self):
        self.area.select(3, 5, 8, 11)
        self.assertEqual(7, self.area.get_height())

    def test_area_is_within_selection(self):
        self.area.select(3, 5, 8, 11)
        self.assertEqual(True, self.area.is_within_selection(3, 5))
        self.assertEqual(True, self.area.is_within_selection(8, 11))
        self.assertEqual(True, self.area.is_within_selection(7, 7))
        self.assertEqual(False, self.area.is_within_selection(2, 7))
        self.assertEqual(False, self.area.is_within_selection(11, 7))
        self.assertEqual(False, self.area.is_within_selection(5, 4))
        self.assertEqual(False, self.area.is_within_selection(5, 13))

    def test_area_is_edge_tile(self):
        self.area.select(3, 5, 8, 11).use_edge()
        self.assertEqual(True, self.area.is_within_selection(3, 5))
        self.assertEqual(True, self.area.is_within_selection(8, 11))
        self.assertEqual(True, self.area.is_within_selection(3, 7))
        self.assertEqual(True, self.area.is_within_selection(6, 5))
        self.assertEqual(False, self.area.is_within_selection(5, 7))
        self.assertEqual(False, self.area.is_within_selection(2, 10))
        self.assertEqual(False, self.area.is_within_selection(4, 12))


# Mock Objects & Variables
uuid = "cool_uuid"


class MM:
    """Mock object for map_manager"""
    map_size = 5
    terrain = [TerrainTile(_index=index, host_uuid=uuid) for index in range(pow(map_size, 2))]


class SCN:
    """Mock object for scenario"""
    map_manager = MM
    uuid: UUID = uuid
