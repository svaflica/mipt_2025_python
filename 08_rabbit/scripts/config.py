from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='env', extra='ignore', case_sensitive=False
    )

    # PostgreSQL database settings
    db_host: str = 'localhost'
    db_port: int = 5432
    db_name: str = 'db'
    db_user: str = 'postgres'
    db_password: str | None = None  # Password can be optional

    # Other settings (optional)
    debug: bool = False

    @property
    def database_url(self) -> str:
        """Construct the async database URL."""
        if self.db_password:
            return (
                f'postgresql://{self.db_user}:{self.db_password}@{self.db_host}:'
                f'{self.db_port}/{self.db_name}'
            )
        else:
            return (
                f'postgresql://{self.db_user}@{self.db_host}:{self.db_port}/{self.db_name}'
            )

    @property
    def async_database_url(self) -> str:
        """Construct the async database URL for asyncpg."""
        return self.database_url.replace("postgresql://", "postgresql+asyncpg://")

    # Rabbit database settings
    RABBIT_HOST: str = 'rabbitmq'
    RABBIT_PORT: int = 5672
    RABBIT_PROTOCOL: str = 'amqp'
    RABBIT_USER: str = 'rmuser'
    RABBIT_PASSWORD: str | None = None  # Password can be optional

    @property
    def async_rm_url(self) -> str:
        """Construct the async database URL for asyncpg."""
        return f'{self.RABBIT_PROTOCOL}://{self.RABBIT_USER}:{self.RABBIT_PASSWORD}@{self.RABBIT_HOST}:{self.RABBIT_PORT}'


settings = Settings()


if __name__ == '__main__':
    print(settings.model_dump())
    print(settings.database_url)
    print(settings.async_database_url)
