
import sys
modulename = 'sys'
if modulename not in sys.modules:
    print(f'You have not imported the {modulename} module')
else: print(f'module:{modulename} is here')