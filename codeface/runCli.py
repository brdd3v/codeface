#!/usr/bin/env python3
"""
Simple script to run codeface directly from source
"""
import sys
from codeface.cli import main; 
if __name__ == '__main__':
    ret = main()
    sys.exit(ret)
