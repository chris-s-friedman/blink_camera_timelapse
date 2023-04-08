"""
Copies contents of prd dataservice to local dataservice for a particular study
"""
from blink_timelapse.auth import blink_session
from blink_timelapse.take_timelapse_photos import take_photos
from blink_timelapse.utils import list_cameras

import click


@click.group()
@click.version_option(package_name="blink_timelapse")
@click.option(
    "-u",
    "--username",
    type=str,
    required=False,
    help="Username for blink",
)
@click.option(
    "-p",
    "--password",
    type=str,
    required=False,
    help="Password for blink",
)
@click.option(
    "-c",
    "--credential_file",
    type=click.Path(exists=True, dir_okay=False, file_okay=True),
    required=False,
    help="Location of blinkpy config file.",
)
@click.pass_context
def blink_timelapse(ctx, username, password, credential_file):
    """
    Tools related to building timelapse using blink cameras
    """
    ctx.ensure_object(dict)
    ctx.obj["blink"] = blink_session(username, password, credential_file)
    pass


@blink_timelapse.command("take_photo")
@click.option(
    "-d",
    "--photo_directory",
    type=click.Path(exists=True, dir_okay=True, file_okay=False),
    default="./",
    show_default=True,
    required=True,
    help="Location to save timelapse photos.",
)
@click.option(
    "-x",
    "--cameras",
    multiple=True,
)
@click.pass_context
def take_timelapse_photos(ctx, photo_directory, cameras):
    """
    Take photos with each specified camera
    """
    take_photos(
        ctx.obj["blink"],
        photo_directory,
        cameras,
    )


@blink_timelapse.command("list_cameras")
@click.pass_context
def list_blink_cameras(ctx):
    """
    List the cameras that can be accessed
    """
    list_cameras(ctx.obj["blink"])


if __name__ == "__main__":
    blink_timelapse(
        auto_envar_prefix="BLINK"
    )  # pylint: disable=no-value-for-parameter
