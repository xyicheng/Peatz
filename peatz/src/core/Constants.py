import os

class Constants(Object):
    DS = os.sep
    CORE = os.path.dirname(__file__)
    PROJECT_DIR = os.path.dirname(CORE)

    TEMPLATES = CORE + DS + 'assets' + DS + 'templates' + DS