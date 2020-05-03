#!/usr/bin/env python

import sys
import re


def usage():
    print("""
  Usage: """, sys.argv[0], """[REQUEST FILE] [API TOKEN] [PROJECT PUBLIC KEY]""")


class Ctx:
    file = None
    request_to_process = None

    def __init__(self, file, request):
        self.file = file
        self.request_to_process = request

    def __str__(self):
        return 'File to open:', self.file, '\nRequest to process:', self.request_to_process


def load_request_from_file(ctx):
    print("Loading request...")
    try:
        with open(ctx.file, encoding="utf8") as f:
            ctx.request_to_process = f.read()
    except FileNotFoundError:
        print("Error loading a file!\nExiting...")
        sys.exit(1)


def replace_dbNodeId_nr_with_null(request):
    pattern = "(dbNodeId\\\"):(.*?),(\\\"id)"  # FIXME
    regex_pattern = "^[0-9a-f]{32}$"

    # print(request.count(pattern))
    print("Number of instances:")
    print("-- dbNodeId:", request.count("dbNodeId\\\":"))
    print("-- api_token:", request.count("api_token\\\":\\\""))
    print("-- project_public_key:", request.count("project_public_key"))


def main():
    if sys.version_info < (3, 6):
        sys.exit("Python 3.6 required")

    try:
        print('Creating context...')
        ctx = Ctx(sys.argv[1], sys.argv[2])
    except IndexError:
        usage()
        sys.exit(1)

    load_request_from_file(ctx)
    # replace_dbNodeId_nr_with_null(ctx.request_to_process)

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
