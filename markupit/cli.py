import pkg_resources
import typer

from .supported_types import SupportedFrom, SupportedTo

app = typer.Typer(no_args_is_help=True)


def version_callback(value: bool) -> None:
    if value:
        version = pkg_resources.get_distribution("markupit").version
        typer.echo(f"Markup convertion CLI tool version: {version}")
        raise typer.Exit()


@app.callback()
def version(
    version: bool = typer.Option(None, "--version", callback=version_callback, help="Show package version"),
) -> None:
    """
    Markup Convertion CLI Tool
    """
    pass


@app.command(no_args_is_help=True)
def convert(
    # supressing B088, because it conflicts with syntax recommended by typer authors
    from_: SupportedFrom = typer.Option(..., "--from", help="Format of input file"),  # noqa: B008
    to: SupportedTo = typer.Option(help="Format of output file"),  # noqa: B008
    input: str = typer.Option(..., "--input", "-i", help="Input file"),  # noqa: B008
    output: str = typer.Option(None, "--output", "-o", help="Output file"),  # noqa: B008
) -> None:
    """
    Convert Markup Files
    """
    typer.echo("Converting...")
