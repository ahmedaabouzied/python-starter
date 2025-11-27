import os
import click
import importlib

class RootCLI(click.Group):
    def list_commands(self, ctx):
        """Scan the 'cmd' directory for .py files."""
        rv = []
        cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "cmd"))
        
        for filename in os.listdir(cmd_folder):
            if filename.endswith(".py") and not filename.startswith("__"):
                rv.append(filename[:-3]) # remove .py extension
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        """Import the module and return the cli object."""
        try:
            mod = importlib.import_module(f"cmd.{name}")
        except ImportError as e:
            # Optional: handle the case where the module or dependency is missing
            print(e)
            return None
        
        # It expects a click function named 'cli' inside the module
        return mod.cli

@click.command(cls=RootCLI)
def cli():
    """TODO: Implement the CLI application"""
    pass
