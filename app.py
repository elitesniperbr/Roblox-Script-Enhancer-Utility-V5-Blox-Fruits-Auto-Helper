"""
Application module - main application class
"""

import tkinter as tk
from tkinter import ttk
import json
from pathlib import Path
from typing import Optional

class Application:
    def __init__(self):
        self.root: Optional[tk.Tk] = None
        self.window = None
        self.config = {}
        self.is_running = False
    
    def load_config(self, config_path: str = 'config/settings.json'):
        try:
            with open(config_path, 'r') as f:
                self.config = json.load(f)
            print(f"Loaded config from {config_path}")
        except FileNotFoundError:
            print(f"Config file {config_path} not found, using defaults")
            self.config = self._get_default_config()
    
    def _get_default_config(self):
        return {
            'window': {
                'title': 'GUI Menu Application',
                'width': 1024,
                'height': 768,
                'resizable': True
            },
            'theme': 'dark',
            'locale': 'en_US',
            'debug': False
        }
    
    def setup_ui(self):
        self.root = tk.Tk()
        self.root.title(self.config.get('window', {}).get('title', 'GUI App'))
        width = self.config['window'].get('width', 800)
        height = self.config['window'].get('height', 600)
        self.root.geometry(f'{width}x{height}')
        from src.ui.window import MainWindow
        self.window = MainWindow(self.root)
        self.window.pack(fill=tk.BOTH, expand=True)
    
    def run(self):
        if not self.root:
            print("Error: UI not setup")
            return 1
        self.is_running = True
        try:
            self.root.mainloop()
            return 0
        except Exception as e:
            print(f"Application error: {e}")
            return 1
        finally:
            self.is_running = False
    
    def shutdown(self):
        if self.root:
            self.root.quit()
