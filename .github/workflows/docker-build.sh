name: Test

on:
    push:
        branches:
            main

jobs:
    echo:
        runs-on: ubuntu-latest
        steps:
            - uses: actions/checkout@v2
            - run: echo "OK"