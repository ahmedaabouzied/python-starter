import click

@click.command()
@click.option("--port", default=3030, help="port to start the web server on.")
def cli(port):
    """Example serve command"""
    click.echo(f"TODO: Start web server on port {port}")
