import os
from .config_loader import load_config


config_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "configs",
    "config.toml",
)


CONFIG = load_config(config_path)
