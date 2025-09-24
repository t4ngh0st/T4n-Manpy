# cli.py
import argparse
import logging
import sys
from t4n_manpy import __version__
from t4n_manpy.config import APP_NAME
from t4n_manpy.core import installer, converter, src_generator, vur

APP_NAME = "tan"

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
log = logging.getLogger(APP_NAME)


USAGE = f"""{APP_NAME} — T4n-Manpy (dual-mode progress)

Usage:
  tan -i <pkg> [pkg...]        Install package(s)
  tan -u <pkg> [pkg...]        Update package(s)
  tan -ua                      Update all packages
  tan -r <pkg> [pkg...]        Remove package(s)
  tan -q <keyword>             Query package db
  tan -xdeb <file.deb>         Convert .deb -> .xbps (via bundled wrapper)
  tan -src <template-name>     Create xbps-src template (via bundled wrapper)
  tan -vq <keyword>            Query package in VUR
  tan -vur <pkg>               Install package from VUR

Options:
  --realtime                   Use realtime progress bar (default: print-step)
  -h, --help                   Show help
  --version                    Show version
"""

def main():
    parser = argparse.ArgumentParser(prog="t4n", add_help=False)
    parser.add_argument("-i", "--install", help="Install software")
    parser.add_argument("-u", "--update", help="Update software")
    parser.add_argument("-ua", "--update-all", action="store_true", help="Update all software")
    parser.add_argument("-q", "--query", action="store_true", help="Query database")
    parser.add_argument("-r", "--remove", help="Remove software")
    parser.add_argument("-xdeb", action="store_true", help="Convert .deb to .xbps")
    parser.add_argument("-src", action="store_true", help="Create template using xbps-src")
    parser.add_argument("-vq", "--vur-query", help="Query package in VUR (Void User Repository)")
    parser.add_argument("-vur", help="Install software from VUR (Void User Repository)")
    parser.add_argument("-h", "-help", action="store_true", help="Show usage")

    args = parser.parse_args()

    if args.install:
        installer.install(args.install)
    elif args.update:
        installer.update(args.update)
    elif args.update_all:
        installer.update_all()
    elif args.query:
        installer.query()
    elif args.remove:
        installer.remove(args.remove)
    elif args.xdeb:
        converter.convert_deb()
    elif args.src:
        src_generator.create_template()
    elif args.vur_query:
        vur.query(args.vur_query)
    elif args.vur:
        vur.install_from_vur(args.vur)
    else:
        parser.print_help()
