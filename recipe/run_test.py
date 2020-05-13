import os
import sys
import pytest
import spacy
import multiprocessing

if __name__ == "__main__":
    multiprocessing.freeze_support()

    PACKAGE_DIR = os.path.abspath(os.path.dirname((spacy.__file__)))
    sys.exit(pytest.main([PACKAGE_DIR]))
