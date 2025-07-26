from dataclasses import dataclass
from environs import Env


class DatabaseConfig():
    def __init__(self, database_url):
        self.database_url: str = database_url

@dataclass
class Config():
    db: DatabaseConfig
    secret_key: str
    debug: bool

def load_config(path: str) -> Config:
    env = Env()
    env.read_env(path)  # Загружаем переменные окружения из файла .env

    return Config(
        db=DatabaseConfig(database_url=env("DATABASE_URL")),
        secret_key=env("SECRET_KEY"),
        debug=env.bool("DEBUG", default=False)
    )
    
print(load_config('.env'))