import uvicorn
import uvloop
from typer import Typer


manager = Typer()
uvloop.install()


@manager.command()
def run_api() -> None:
    from app.core.settings import config

    uvicorn.run(
        app="app.main:app",
        host=config.API.ADDRESS,
        port=config.API.PORT,
        reload=config.DEBUG,
    )


if __name__ == "__main__":
    manager()
