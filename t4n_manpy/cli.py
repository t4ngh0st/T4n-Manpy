import argparse, sys
from t4n_manpy.core import installer, converter, src_generator, vur

def main():
    parser = argparse.ArgumentParser(prog='t4n', description='T4n-Manpy Package Manager')
    parser.add_argument('-i', '--install', help='Install software')
    parser.add_argument('-u', '--update', help='Update specific software/system')
    parser.add_argument('-ua', '--update-all', action='store_true', help='Update all software/system')
    parser.add_argument('-q', '--query', action='store_true', help='Query installed software/system')
    parser.add_argument('-r', '--remove', help='Remove software/system')
    parser.add_argument('-xdeb', action='store_true', help='Convert .deb to .xbps using xdeb')
    parser.add_argument('-src', action='store_true', help='Generate template using xbps-src')
    parser.add_argument('-vur', '--void-user-repo', help='Install package from VUR')
    parser.add_argument('--realtime', action='store_true', help='Enable realtime progress mode')
    parser.add_argument('-h', '--help', action='help', help='Show this help message and exit')

    args = parser.parse_args()

    if args.install:
        installer.install_package(args.install, realtime=args.realtime)
    elif args.update:
        installer.update_package(args.update)
    elif args.update_all:
        installer.update_all()
    elif args.query:
        installer.query_packages()
    elif args.remove:
        installer.remove_package(args.remove)
    elif args.xdeb:
        converter.run_xdeb()
    elif args.src:
        src_generator.run_xbps_src()
    elif args.void_user_repo:
        vur.install_from_vur(args.void_user_repo)
    else:
        parser.print_help()
