# Hero of Embers (WIP)

## Table of Contents
- [Description](#description)
- [List to do](#to-do-list)
- [Installation](#installation)
- [Plot](#plot)
- [Gameplay](#gameplay)
- [Plot Writer](#plot-writer)
- [Contributing](#contributing)
- [License](#license)

## Description
"Hero of Embers" is a console-based fantasy RPG. You play as Aldric, a young hero uncovering dangerous secrets and battling evil forces. The game is in progress, with evolving features and storyline.

## To do list
### The list of things I want to and the things that are already in game:
- [x] Implemented a scene system driven by a scenes.json file.
- [x] Built the main game loop.
- [x] Developed a plot generation tool in the plot_maker directory.
- [x] Added unit tests (run_tests.py).
- [x] Managed dependencies with requirements.txt.
- [x] Created a setup.py for package installation.
- [x] Implement a combat system with enemies and stats.
- [x] Add an inventory system and item management.
- [x] Introduce experience points and level-up mechanics.
- [x] Add game save/load functionality.
- [x] Write docstring's documentation in code.
- [ ] Add currency
- [ ] Add option to trade.
- [ ] Expand the storyline with additional scenes and choices.
- [ ] Improve the user interface (e.g. color-coded text, better formatting).
- [ ] Integrate sound and music (if ever expanded beyond the console).
- [ ] Include demo screenshots or GIFs in the README.md.

## Installation
1. Clone the repository:

    ```bash
    git clone https://github.com/McDjXdLol/Hero-of-Embers.git 
    ```

2. Navigate to the project folder:

    ```bash
    cd Hero-of-Embers
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt 
    ```

4. Start the game:

    ```bash
    python run_game.py
    ```

## Plot (WIP)
Follow Aldric's journey from a young farmer to a hero who uncovers dark conspiracies tied to the Hollow Hand Cult and the legendary sword Stormfang. 

## Gameplay
A turn-based RPG with choices that impact the story, dynamic combat, and an evolving narrative. Your choices shape your adventure, with features like:

- **Character Classes:** Protector, Fighter, and Avenger.
- **Dynamic Combat:** Strategic turn-based battles.
- **Inventory System:** Collect items for progression.
- **Save/Load Progress:** Save your game and continue anytime.

## Plot Writer

If you'd like to create your own plot for the game, you can use the `plot_maker_app.py` script. This is the only part of the project where a GUI is used, so you'll need to install `pyqt6` beforehand.

![plot_maker_app](https://github.com/user-attachments/assets/3de29f7b-2386-4b59-a951-2fc930a22077)


### Here’s how to use it:
1. **Scene Name**: Enter the name of the scene. Remember this name, as you'll use it later to navigate between scenes.
2. **Description**: Add a description to tell the player what’s happening in the scene.
3. **Add Scene**: After adding the scene, you'll need to re-enter the scene name to continue.
4. **Options for the Player**: For each scene, you can add multiple options for the player. You can use simple letters or numbers for options; capitalization doesn't affect the game’s mechanics.
5. **Option Description**: Add a short description for each player option, e.g., "run away", "fight", etc.
6. **Effect**: Describe the effect of the option, explaining what happens after the player selects it.
7. **Requirements**: This checks if the player has the necessary items in their inventory. For example, if the player needs berries to make a choice, the option will be unavailable if they don’t have them.
8. **Items to Give**: If the player needs specific items, you can give them here to be used later in the game.
9. **Combat**: Set whether a fight will occur after selecting this option.
10. **Enemy Name**: If there’s a fight, you can set the enemy the player will face. Be sure the enemy name matches one from the library file.
11. **Next Scene**: After selecting an option, you can set the scene that will follow. You can reference scenes that haven’t been created yet.
12. **Add Option**: After configuring the option, click "Add Option" to save it. You can add as many options as needed.
13. **Start New Scene**: Once you've added options, click "New Scene" to create additional scenes and repeat the process.
14. **Save Plot**: When you’re finished, click "Save to file" to save your plot. Now you're ready to load it into the game and start playing.

To run the plot maker, simply execute the following command:
```bash
python run_plot_maker.py
```

## Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
