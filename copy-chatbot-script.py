#!/usr/bin/env python

"""
    TODO:
    1. replace api token
    2. replace ppk
"""

import sys
import re


def usage():
    print("""
  Usage: """, sys.argv[0], """[REQUEST FILE] [API TOKEN] [PROJECT PUBLIC KEY]""")


class Ctx:
    request_file = None
    loaded_request = None
    processed_request = None
    new_api_token = None
    new_ppk = None
    ppk_and_api_pattern = "[a-zA-Z0-9]{32}"

    def __init__(self, request_file, api_token, ppk):
        self.request_file = request_file
        self.new_api_token = api_token
        self.new_ppk = ppk

    def __str__(self):
        return 'File to open:', self.request_file, '\nProcessed request:', self.processed_request


def load_request_from_file(ctx):
    print("Loading request from file...")
    try:
        with open(ctx.request_file, encoding="utf8") as f:
            ctx.loaded_request = f.read()
    except FileNotFoundError:
        sys.exit("Error loading a file!\nExiting...")


def replace_dbNodeId_with_null(ctx):
    # TODO
    pattern = "(dbNodeId\\\"):(.*?),(\\\"id)"  # FIXME
    regex_pattern = "^[0-9a-f]{32}$"

    ctx.processed_request = re.sub('', '', ctx.loaded_request)

    # print(request.count(pattern))
    print("Number of instances:")
    print("-- dbNodeId:", ctx.processed_request.count("dbNodeId\\\":"))
    print("-- api_token:", ctx.processed_request.count("api_token\\\":\\\""))
    print("-- project_public_key:", ctx.processed_request.count("project_public_key"))


def replace_api_token(ctx):
    try:
        old_api_token = re.findall(ctx.ppk_and_api_pattern, ctx.processed_request)[0]
    except TypeError:
        sys.exit("Error processing request!\nExiting...")

    ctx.processed_request = ctx.processed_request.replace(old_api_token, ctx.new_api_token, 1)


def replace_public_key(ctx):
    # TODO
    # print('\nppk to replace:', ctx.request_to_process.count("^[a-zA-Z0-9]{32}$"))
    ppk_to_replace = re.findall(ctx.ppk_and_api_pattern, ctx.processed_request)[1]
    print('ppk to replace:', ppk_to_replace)
    # print('how many ppks:', len(re.findall(ctx.ppk_and_api_pattern, ctx.processed_request)))
    # ctx.request_to_process = re.sub('\"ml9izxoajvciiuhoagifniwpwocyyz4d\"', '', ctx.processed_request)


def print_request_to_file(ctx):
    print("Printing to file...")
    if ctx.processed_request is None:
        exit("Processed request is None\nExiting...")

    import time
    fpath = "logs/" + str(time.time()) + '_processed_request.txt'
    with open(fpath, 'x', encoding="utf-8") as f:
        f.write(ctx.processed_request)


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
    replace_dbNodeId_with_null(ctx)
    replace_api_token(ctx)
    # replace_public_key(ctx)
    # replace_url(ctx)
    print_request_to_file(ctx)

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
