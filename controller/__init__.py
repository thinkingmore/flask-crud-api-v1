import os
import importlib

current_dir = os.path.dirname(__file__)

for filename in os.listdir(current_dir):
    if filename.endswith('.py') and filename != '__init__.py':
        module_name = f'controller.{filename[:-3]}'
        importlib.import_module(module_name)