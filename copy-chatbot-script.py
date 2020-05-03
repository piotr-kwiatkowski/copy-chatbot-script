#!/usr/bin/env python

import sys
import re


def usage():
    print("""
  Usage: """, sys.argv[0], """[REQUEST FILE] [API TOKEN] [PROJECT PUBLIC KEY]""")


def load_request_from_file(file):
    with open(file, encoding="utf8") as f:
        global request_to_process
        request_to_process = f.read()
    # f = open(file, encoding="utf8")
    # if f.mode == "r":
    #   global request_to_process
    #   request_to_process = f.read()
    #   f.close()
    # else:
    #   print("Could not read this file :(\nExiting...")
    #   sys.exit()


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
        print("Processing file:", sys.argv[1])
    except IndexError:
        usage()
        sys.exit(1)

    global request_to_process

    # start = request.find("dbNodeId\\\":") + len("dbNodeId\\\":")
    # end = request.find("dbNodeId\\\":")
    # substring = request[start:end]
    # print(substring)

    # for item in request:
    #   substring = re.search(pattern, request).group(1)
    #   print(substring)

    # print(request.split("dbNodeId", 5)[1])

    load_request_from_file(sys.argv[1])
    replace_dbNodeId_nr_with_null(request_to_process)


if __name__ == "__main__":
    main()
