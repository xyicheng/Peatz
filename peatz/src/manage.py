# THE FIRST PY TO BE LAUNCHED

import sys
from core.core import Core

try:
	core = Core();
	core.launch(sys.argv)
except Exception as e:
	print(e)