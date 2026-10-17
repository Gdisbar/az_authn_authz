import os

from fastapi import FastAPI, Security
from backends import service
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from auth import azure_scheme
from auth import AZURE_FRONTEND_APP_CLIENT_ID,AZURE_BACKEND_APP_CLIENT_ID,SCOPE_NAME


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the OpenID configuration on startup
    await azure_scheme.openid_config.load_config()
    yield

app = FastAPI(
    title="Secure Azure API",
    lifespan=lifespan,
    swagger_ui_oauth2_redirect_url='/oauth2-redirect',
    swagger_ui_init_oauth={
        'usePkceWithAuthorizationCodeGrant': True,
        'clientId': AZURE_FRONTEND_APP_CLIENT_ID,
        'scopes': f"api://{AZURE_BACKEND_APP_CLIENT_ID}/{SCOPE_NAME}"
    },
)

# CORS configuration is essential for localhost testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    service.router,
    dependencies=[
        Security(
            azure_scheme,
            scopes=[SCOPE_NAME],
        )
    ],
)