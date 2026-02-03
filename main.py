#!/usr/bin/env python3
"""
Main entry point for GUI Menu Application
"""

import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / 'src'))

from core.application import Application

def main():
    print("Starting GUI Menu Application...")
    app = Application()
    app.load_config()
    app.setup_ui()
    return app.run()

if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)
