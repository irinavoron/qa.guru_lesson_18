import pydantic_settings


class Config(pydantic_settings.BaseSettings):
    base_url: str = 'https://demowebshop.tricentis.com'
    window_width: int = 1896
    window_height: int = 1080
    timeout: float = 4.5


config = Config()