import dotenv
import pydantic_settings


def load_env():
    dotenv.load_dotenv()


class Config(pydantic_settings.BaseSettings):
    BASE_URL: str = 'https://demowebshop.tricentis.com'
    WINDOW_WIDTH: int = 1896
    WINDOW_HEIGHT: int = 1080
    TIMEOUT: float = 4.5


load_env()
config = Config()
