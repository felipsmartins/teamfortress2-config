#!/usr/bin/env python3
# coding: UTF-8
import os
import sys
import shutil
from glob import glob
import subprocess
import argparse

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def install(tf2_path: str) -> None:
    cfg_src_dir = os.path.join(SCRIPT_DIR, "TeamFortress2", "cfg")
    cfg_dest_dir = os.path.join(tf2_path, "cfg")

    files = os.listdir(cfg_src_dir)

    for basename in files:
        path = os.path.join(cfg_src_dir, basename)
        destpath = os.path.join(cfg_dest_dir, basename)

        if os.path.isdir(path):
            if os.path.exists(destpath):
                print("destination directory exists, replacing {}".format(destpath))
                shutil.rmtree(destpath)

            print("copying directory: {} -> {}".format(path, destpath))
            shutil.copytree(path, destpath)

        if os.path.isfile(path):
            if os.path.exists(destpath):
                print("destination file exists, replacing {}".format(destpath))
                os.remove(destpath)

            print('copying file: "{} -> {}"'.format(path, destpath))
            shutil.copyfile(path, destpath)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Sync files to Team Fortress directory")
    parser.add_argument(
        "steamapps_dir", help="Absolute path to 'steamapps' directory")
    args = parser.parse_args()

    if not os.path.isdir(args.steamapps_dir):
        print("ERR: directory not found: {}".format(
            args.steamapps_dir))
        sys.exit(0)

     # i.e:
     #  ~/.steam/steam/steamapps/common/Team Fortress 2/tf
     # ~/.steam/debian-installation/steamapps/common/Team Fortress 2/tf
    tfdir = os.path.join(args.steamapps_dir, "common", "Team Fortress 2", "tf")

    install(tfdir)
    print("ALL DONE!")
    sys.exit(os.EX_OK)
