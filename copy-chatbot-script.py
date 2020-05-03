#!/usr/bin/env python

import sys
import re


def usage():
    print("""
  Usage: """, sys.argv[0], """[REQUEST FILE] [API TOKEN] [PROJECT PUBLIC KEY]""")


class Ctx:
    request_file = None
    request_to_process = None
    new_api_token = None
    new_ppk = None

    def __init__(self, request_file, api_token, ppk):
        self.request_file = request_file
        self.new_api_token = api_token
        self.new_ppk = ppk

    def __str__(self):
        return 'File to open:', self.request_file, '\nRequest to process:', self.request_to_process


def load_request_from_file(ctx):
    print("Loading request...")
    try:
        with open(ctx.request_file, encoding="utf8") as f:
            ctx.request_to_process = f.read()
    except FileNotFoundError:
        print("Error loading a file!\nExiting...")
        sys.exit(1)


def replace_dbNodeId_nr_with_null(ctx):
    pattern = "(dbNodeId\\\"):(.*?),(\\\"id)"  # FIXME
    regex_pattern = "^[0-9a-f]{32}$"

    # TODO
    ctx.request_to_process = re.sub('', '', ctx.request_to_process)

    # print(request.count(pattern))
    print("Number of instances:")
    print("-- dbNodeId:", ctx.request_to_process.count("dbNodeId\\\":"))
    print("-- api_token:", ctx.request_to_process.count("api_token\\\":\\\""))
    print("-- project_public_key:", ctx.request_to_process.count("project_public_key"))


def replace_api_token(ctx):
    # TODO
    ctx.request_to_process = re.sub('', '', ctx.request_to_process)


def replace_public_key(ctx):
    # TODO
    old_ppk = 'project_public_key\":\"'
    new_ppk = '_______'
    ctx.request_to_process = re.sub(old_ppk, new_ppk, ctx.request_to_process)


def main():
    if sys.version_info < (3, 6):
        sys.exit("Python 3.6 required")

    try:
        print('Creating context...')
        ctx = Ctx(sys.argv[1], sys.argv[2], sys.argv[3])
    except IndexError:
        usage()
        sys.exit(1)

    load_request_from_file(ctx)
    replace_dbNodeId_nr_with_null(ctx)
    replace_api_token(ctx)
    replace_public_key(ctx)

    # start = request.find("dbNodeId\\\":") + len("dbNodeId\\\":")
    # end = request.find("dbNodeId\\\":")
    # substring = request[start:end]
    # print(substring)

    # for item in request:
    #   substring = re.search(pattern, request).group(1)
    #   print(substring)

    # print(request.split("dbNodeId", 5)[1])


if __name__ == "__main__":
    main()
