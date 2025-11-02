from pathlib import Path
from utils4plans.paths import StaticPaths
import pyprojroot


BASE_PATH = pyprojroot.find_root(pyprojroot.has_dir(".git"))
static_paths = StaticPaths("", BASE_PATH)


class DynamicPaths:
    init_data = static_paths.inputs / "Bayside_F1.json"
