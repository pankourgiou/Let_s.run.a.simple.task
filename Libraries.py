"""
Libraries.py — easy mode!
Imports ~35 modules from Python's standard library (no pip install needed)
and then prints a simple message. 
"""

import os
import sys
import math
import random
import string
import time
import datetime
import re
import json
import csv
import collections
import itertools
import functools
import pathlib
import subprocess
import shutil
import glob
import hashlib
import base64
import uuid
import socket
import threading
import queue
import logging
import argparse
import textwrap
import pprint
import statistics
import decimal
import fractions
import calendar
import platform
import getpass
import tempfile
import zipfile
import copy
import operator

LIBRARIES = [
    os, sys, math, random, string, time, datetime, re, json, csv,
    collections, itertools, functools, pathlib, subprocess, shutil, glob,
    hashlib, base64, uuid, socket, threading, queue, logging, argparse,
    textwrap, pprint, statistics, decimal, fractions, calendar, platform,
    getpass, tempfile, zipfile, copy, operator,
]

def main():
    print("Hello, World! 👋")
    print(f"That message just rode in on {len(LIBRARIES)} imported standard library modules.")
    print(f"Running on {platform.system()} with Python {sys.version.split()[0]}")
    print(f"Current time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Imported modules:", ", ".join(m.__name__ for m in LIBRARIES))

if __name__ == "__main__":
    main()
