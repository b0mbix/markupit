import typer
import pkg_resources

app = typer.Typer(no_args_is_help=True)


def version_callback(value: bool) -> None:
    if value:
        version = pkg_resources.get_distribution("markup-converter").version
        typer.echo(f"Markup convertion CLI tool version: {version}")
        raise typer.Exit()


@app.callback()
def version(
    version: bool = typer.Option(
        None, "--version", callback=version_callback, help="Show package version"
    ),
) -> None:
    """
    Markup Convertion CLI Tool
    """
    pass


@app.command()
def convert() -> None:
    """
    Convert Markup Files
    """
    typer.echo("Coverting...")
