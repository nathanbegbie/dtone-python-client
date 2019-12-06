import os
from os.path import join, dirname, abspath
import shutil

from invoke import task

def get_docs_source_path():
    return join(dirname(abspath(__file__)), "docs")


def get_docs_build_path():
    return join(get_docs_source_path(), "_build")

@task
def makedocs(c):
    from sphinx.cmd.build import build_main

    build_main(["-b", "dirhtml", get_docs_source_path(), get_docs_build_path()])
