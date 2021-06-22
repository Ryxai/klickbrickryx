import argparse
import sys


def main():
    args = parse_args(sys.argv[1:])
    res = dispatch_command(args)
    print(res)


def parse_args(args):
    main_parser = argparse.ArgumentParser()
    subparsers = main_parser.add_subparsers(dest="command")
    hello_parser = subparsers.add_parser('hello', help='hello help')
    hello_parser.add_argument('--name')
    args = main_parser.parse_args(args)
    return args


def dispatch_command(args):
    if args.command == 'hello':
        if args.name:
            return f'Hello {args.name}'
        else:
            return 'Hello World'
