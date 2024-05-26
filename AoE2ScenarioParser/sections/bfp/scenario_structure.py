import zlib

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import ByteStream

from AoE2ScenarioParser.sections.bfp.background_image.background_image import BackgroundImage
from AoE2ScenarioParser.sections.bfp.cynematics import Cinematics
from AoE2ScenarioParser.sections.bfp.diplomacy import Diplomacy
from AoE2ScenarioParser.sections.bfp.file_header import FileHeader
from AoE2ScenarioParser.sections.bfp.files.file_data import FileData
from AoE2ScenarioParser.sections.bfp.global_victory import GlobalVictory
from AoE2ScenarioParser.sections.bfp.map.map_data import MapData
from AoE2ScenarioParser.sections.bfp.messages import Messages
from AoE2ScenarioParser.sections.bfp.meta_data.meta_data import MetaData
from AoE2ScenarioParser.sections.bfp.options import Options
from AoE2ScenarioParser.sections.bfp.player_data_block_2.player_data_block_2 import PlayerDataBlock2
from AoE2ScenarioParser.sections.bfp.triggers.trigger_data import TriggerData
from AoE2ScenarioParser.sections.bfp.units.unit_data import UnitData


class ScenarioStructure(BaseStruct):
    # @formatter:off
    file_header: FileHeader           = Retriever(FileHeader,                         default_factory = lambda sv, p: FileHeader(sv, p))
    data_header: MetaData             = Retriever(MetaData,                           default_factory = lambda sv, p: MetaData(sv, p), remaining_compressed = True)
    text_data: Messages               = Retriever(Messages,                           default_factory = lambda sv, p: Messages(sv, p))
    cinematics: Cinematics            = Retriever(Cinematics,                         default_factory = lambda sv, p: Cinematics(sv, p))
    background_image: BackgroundImage = Retriever(BackgroundImage,                    default_factory = lambda sv, p: BackgroundImage(sv, p))
    player_data2: PlayerDataBlock2    = Retriever(PlayerDataBlock2,                   default_factory = lambda sv, p: PlayerDataBlock2(sv, p))
    global_victory: GlobalVictory     = Retriever(GlobalVictory,                      default_factory = lambda sv, p: GlobalVictory(sv, p))
    diplomacy: Diplomacy              = Retriever(Diplomacy,                          default_factory = lambda sv, p: Diplomacy(sv, p))
    options: Options                  = Retriever(Options,                            default_factory = lambda sv, p: Options(sv, p))
    map_data: MapData                 = Retriever(MapData,                            default_factory = lambda sv, p: MapData(sv, p))
    unit_data: UnitData               = Retriever(UnitData,                           default_factory = lambda sv, p: UnitData(sv, p))
    trigger_data: TriggerData         = Retriever(TriggerData,                        default_factory = lambda sv, p: TriggerData(sv, p))
    file_data: FileData               = Retriever(FileData, min_ver=Version((1, 40)), default_factory = lambda sv, p: FileData(sv, p))
    # @formatter:on

    @classmethod
    def decompress(cls, bytes_: bytes) -> bytes:
        return zlib.decompress(bytes_, -zlib.MAX_WBITS)

    @classmethod
    def compress(cls, bytes_: bytes) -> bytes:
        deflate_obj = zlib.compressobj(9, zlib.DEFLATED, -zlib.MAX_WBITS)
        compressed = deflate_obj.compress(bytes_) + deflate_obj.flush()
        return compressed

    @classmethod
    def get_version(
        cls,
        stream: ByteStream,
        struct_ver: Version = Version((0,)),
        parent: BaseStruct = None,
    ) -> Version:
        ver_str = stream.peek(4).decode("ASCII")
        return Version(tuple(map(int, ver_str.split("."))))

    def __init__(
        self, struct_ver: Version = Version((1, 47)), parent: BaseStruct = None, initialise_defaults = True,
        **retriever_inits
    ):
        super().__init__(struct_ver, parent, initialise_defaults = initialise_defaults, **retriever_inits)