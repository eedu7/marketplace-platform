from pydantic import PostgresDsn, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    # Database Configuration
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "myuser"
    POSTGRES_PASSWORD: str = "mypassword"
    POSTGRES_DB: str = "mydatabase"

    DB_POOL_SIZE: int = 5
    DB_POOL_RECYCLE: int = 3600
    DB_POOL_PRE_PING: bool = True
    DB_MAX_OVERFLOW: int = 10

    # Test Database Configuration
    TEST_POSTGRES_HOST: str = "localhost"
    TEST_POSTGRES_PORT: int = 5433
    TEST_POSTGRES_USER: str = "mytestuser"
    TEST_POSTGRES_PASSWORD: str = "mytestpassword"
    TEST_POSTGRES_DB: str = "mytestdatabase"

    # JWT
    JWT_SECRET_KEY: str = "jwt_secret_key"
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    JWT_REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    JWT_ISSUER: str = "my-ecommerce-api"
    JWT_AUDIENCE: str = "my-ecommerce-web"
    JWT_LEEWAY_SECONDS: int = 30

    @computed_field
    @property
    def DATABASE_URL(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_HOST,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        )

    @computed_field
    @property
    def TEST_DATABASE_URL(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=self.TEST_POSTGRES_USER,
            password=self.TEST_POSTGRES_PASSWORD,
            host=self.TEST_POSTGRES_HOST,
            port=self.TEST_POSTGRES_PORT,
            path=self.TEST_POSTGRES_DB,
        )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )


config: Config = Config()
