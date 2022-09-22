from pathlib import Path

root_directory = Path(__file__).parent
source_directory = root_directory / 'AoE2ScenarioParser'

for file in [file for file in source_directory.rglob('*.*') if file.suffix in {'.c', '.pyd'}]:
    print(file)
    file.unlink()
