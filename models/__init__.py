#!/usr/bin/env python3
"""
Models package initialization for the AirBnB clone project.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

# Additional initialization code if necessary...
