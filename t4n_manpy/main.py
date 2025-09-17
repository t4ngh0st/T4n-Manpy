#!/usr/bin/env python3
import argparse
from t4n_manpy.core.installer import install_package
from t4n_manpy.core.updater import update_package, update_all, sync_index, sync_repos
from t4n_manpy.core.remover import remove_package
from t4n_manpy.core.query import query_database, query_repos

from t4n_manpy.utils.xdeb_converter import convert_deb
from t4n_manpy.utils.xbps_src_manager import create_templatei

def main():
    parser = argparse.ArgumentParser(prog="t4n", description="T4n-Manpy Package Manager for Void Linux")
    parser.add_argument("-i", "--install", metavar="<software>", help="Install software")
    parser.add_argument("-u", "--update", metavar="<software>", help="Update software")
    parser.add_argument("-ua", "--update-all", action="store_true", help="Update all software")
    parser.add_argument("-q", "--query", action="store_true", help="Query database")
    parser.add_argument("-r", "--remove", metavar="<software>", help="Remove software")
    parser.add_argument("-s", "--sync", action="store_true", help="Sinkronisasi update terbaru")
    parser.add_argument("-sr", "--sync-repos", action="store_true", help="Sinkronisasi repo")
    parser.add_argument("-qr", "--query-repos", action="store_true", help="Cek repository")
    parser.add_argument("-xdeb", metavar="<file.deb>", help="Convert .deb to .xbps")
    parser.add_argument("-src", action="store_true", help="Create template using xbps-src")

    args = parser.parse_args()

    if args.install:
        install_package(args.install)
    elif args.update:
        update_package(args.update)
    elif args.update_all:
        update_all()
    elif args.query:
        query_database()
    elif args.remove:
        remove_package(args.remove)
    elif args.sync:
        sync_index()
    elif args.sync_repos:
        sync_repos()
    elif args.query_repos:
        query_repos()
    elif args.xdeb:
        convert_deb(args.xdeb)
    elif args.src:
        create_template()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
