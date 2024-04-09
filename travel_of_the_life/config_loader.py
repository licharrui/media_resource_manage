import os
import toml


class DataBaseConfig:
    def __init__(
        self, ip: str, port: int, user: str, password: str, db_name: str
    ) -> None:
        self.ip = ip
        self.port = port
        self.user = user
        self.password = password
        self.db_name = db_name


class MediaResourceConfig:
    def __init__(
        self,
        dir_name: str,
        image_dir: str,
        video_dir: str,
        audio_dir: str,
        document_dir: str,
    ) -> None:
        self.dir_name = dir_name
        self.image_dir = image_dir
        self.video_dir = video_dir
        self.audio_dir = audio_dir
        self.document_dir = document_dir


class TravelOfTheLifeConfig:
    def __init__(
        self, data_base: DataBaseConfig, media_resource: MediaResourceConfig
    ) -> None:
        self.data_base = data_base
        self.media_resource = media_resource


def load_config(config_file: str) -> TravelOfTheLifeConfig:
    if os.path.exists(config_file):
        config = toml.load(config_file)
    else:
        raise FileNotFoundError(f"{config_file} not found")

    _data_base_config = DataBaseConfig(**config["db"])
    _media_resource_config = MediaResourceConfig(**config["resource"])

    travel_of_the_life_config = TravelOfTheLifeConfig(
        data_base=_data_base_config,
        media_resource=_media_resource_config,
    )

    return travel_of_the_life_config
