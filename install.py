#!/usr/bin/env python3
# coding: UTF-8
import os
import sys
import shutil
import argparse
import platform
from typing import Union

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
nocopy_files = ["sensitivedata.cfg"]


def get_steamapps_common_paths() -> list:
    system = platform.system().lower()

    if system == "windows":
        return [
            os.path.join(os.environ["ProgramFiles(x86)"], "Steam", "steamapps"),
            os.path.join(os.environ["ProgramFiles"], "Steam", "steamapps"),
        ]

    # Linux
    return [
        os.path.expanduser("~/.local/share/Steam/steamapps"),
        os.path.expanduser("~/.steam/steamapps"),
    ]


def find_steamapps_dir() -> Union[str, None]:
    for trypath in get_steamapps_common_paths():
        if os.path.isdir(trypath):
            return trypath


def install(tf2_path: str, options: argparse.Namespace) -> None:
    cfg_src_dir = os.path.join(SCRIPT_DIR, "TeamFortress2", "cfg")
    cfg_dest_dir = os.path.join(tf2_path, "cfg")
    files = os.listdir(cfg_src_dir)
    ignored = nocopy_files

    if options.copy_ignored:
        ignored = []

    for configfile in files:
        path = os.path.join(cfg_src_dir, configfile)
        destpath = os.path.join(cfg_dest_dir, configfile)

        if configfile not in ignored:
            print('copying/replacing file: "{} -> {}"'.format(path, destpath))
            shutil.copyfile(path, destpath)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Sync files to Team Fortress directory"
    )
    parser.add_argument(
        "-d", "--steamapps-dir", help="Absolute path to 'steamapps' directory"
    )
    parser.add_argument(
        "-c", "--copy-ignored", help="copy ignored files", action="store_true"
    )
    args = parser.parse_args()

    if args.steamapps_dir:
        steamapps_dir = args.steamapps_dir
    else:
        print("--steamapps-dir not provided, trying common paths...")
        steamapps_dir = find_steamapps_dir()

    if not os.path.isdir(steamapps_dir):
        print("ERR: directory not found: {}".format(steamapps_dir))
        sys.exit(0)

    tfdir = os.path.join(steamapps_dir, "common", "Team Fortress 2", "tf")

    install(tfdir, args)
    print("ALL DONE!")
    sys.exit(os.EX_OK)
