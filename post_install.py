import os
import sys
from subprocess import check_call

def _post_install():
    try:
        check_call([sys.executable, '-m', 'reqauto'])
    except Exception as e:
        print("Error running piply:", e)
        sys.exit(1)

if __name__ == '__main__':
    _post_install()
