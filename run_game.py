import sys
import os

project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'hero_of_embers'))
if project_path not in sys.path:
    sys.path.append(project_path)

from hero_of_embers.main import main

if __name__ == "__main__":
    game = main()
    game.main()
    
    