"""Command-line interface."""

import click


@click.command()
@click.version_option()
def main() -> None:
    """SSB Pypitest Vst."""


if __name__ == "__main__":
    main(prog_name="ssb-pypitest-vst")  # pragma: no cover
