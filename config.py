from datetime import timedelta

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from pydantic import BaseSettings
from pydantic.config import Optional


class Settings(BaseSettings):
    DEBUG: Optional[str]
    DATABASE_URL: Optional[str]
    SECRET_KEY: str = "my_secret_key"
    LOG_LEVEL: str = "DEBUG"

    RESTX_VALIDATE: bool = True

    authorizations = {
        'apikey': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'X-API-KEY'
        }
    }
    APISPEC_SPEC = APISpec(
        title='Frame.work Test Admissão. o/',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0',
        securityDefinitions=authorizations
    )
    APISPEC_SWAGGER_UI_URL = '/'


settings = Settings(_env_file='.env', _env_file_encoding='utf-8')
