# Hero of Embers (WIP)

### Table of Contents:
- [Description](#description)
- [Installation](#installation)
- [Plot](#plot)
- [Gameplay](#gameplay)
- [Plot Writer](#plot-writer)
- [Contributing](#contributing)
- [License](#license)

## Description
"Hero of Embers" is a work-in-progress console-based fantasy RPG. Currently, it’s in early development, with the core game mechanics and plot still evolving. The game takes place in a rich, fantasy world filled with combat, choices, and an engaging narrative. You take on the role of a young hero who must uncover hidden secrets and battle a rising evil.

The game is not yet exported to an executable, and it lacks a click-to-play feature. To test the mechanics, you need to run the Python script via `main.py`. As of now, the plot consists mainly of scene names and basic structure, but it is rapidly evolving.

## Installation
To play the game, you need to have Python 3.x installed on your PC. You can then download the project files and run the game locally.

1. Clone the repository:
    ```bash
    git clone https://github.com/McDjXdLol/Hero-of-Embers.git
    ```

2. Navigate to the project folder:
    ```bash
    cd Hero-of-Embers
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
   This will install all the necessary dependencies, including `pyqt6` (used for the plot creation tool).

4. To start the game, run the following:
    ```bash
    python main.py
    ```

## Plot
The story follows **Aldric**, a young farmer who arrives in a bustling city only to be drawn into a world of ancient mysteries. Soon, Aldric meets **Lyria**, a mysterious girl with ties to a powerful order that once protected the world from darkness. As Aldric grows stronger, he becomes embroiled in a dangerous cult's conspiracy, fighting to uncover secrets about an ancient weapon that could determine the fate of the world.

Along the way, he must make tough choices, including dealing with betrayal, forging alliances, and facing powerful enemies, all while preparing for an ultimate showdown against a dark force that threatens to consume everything.

### Key Story Elements:
- **The Protector**: A knightly order long thought destroyed, with connections to Aldric’s destiny.
- **The Hollow Hand Cult**: A mysterious group that seeks to unleash a deadly power.
- **Stormfang**: A legendary sword said to hold the key to defeating the ultimate evil.

## Gameplay
In "Hero of Embers," you will embark on a journey that blends narrative choices and turn-based combat. You will encounter different enemies, explore new locations, and face moral dilemmas that shape the course of the story.

### Core Features:
- **Character Classes**: Choose from a range of classes that will define your playstyle. Classes include:
    - **The Protector (Tank)** – High HP, high armor, low damage.
    - **The Fighter (Balanced)** – Standard stats for a balanced approach.
    - **The Avenger (Damager)** – High damage, low HP, for aggressive combat.
  
- **Dynamic Combat**: Engage in turn-based combat with a variety of enemies. The battle mechanics include HP, armor, and attack damage.

- **Inventory System**: Collect items, potions, and weapons. You can equip your character with different gear as you progress.

- **Choices That Matter**: The game features branching story paths where your choices will directly affect the plot.

- **Save & Load**: Save your progress and load it later to continue where you left off.

### Combat Mechanics:
- **Turn-based Battles**: Each character has HP, armor, and damage stats, and you must strategize your moves carefully to defeat enemies.
  
- **Potion System**: Use health potions and other items to heal during battle.

### Levels of Difficulty:
The game offers three difficulty levels that affect the stats and progression of the player:
- **Cushioned Path (Easy)**: Increased player stats for an easier experience.
- **Twisted Road (Normal)**: Balanced stats for a challenging yet fair experience.
- **Iron Trial (Hard)**: Reduced player stats for a tough challenge.

## Plot Writer
If you wish to create your own scenes and plot progression, you can use the Plot Writer tool. This is a GUI application built with PyQt6. To use it, you need to install the required dependencies and run the `plot_maker_app.py` file.

### How to Use:
1. Enter the scene name you want to create.
2. Add a description that explains what is happening in the scene.
3. Add options that the player can choose, with each option affecting the game in different ways.
    - **Each option includes**:
        - **Description** of the choice (e.g., "Fight", "Run Away").
        - **Effect** (what happens after the player chooses).
        - **Requirements** (items or conditions required to make the choice).
        - **Items to give** (items the player will receive after making the choice).
        - **Combat Encounter** (whether or not a fight will happen).
        - **Next Scene** (the next scene that follows based on the choice).
4. You can create a full story using this tool by adding new scenes, options, and branching paths.

### Note:
You must install `pyqt6` to use this tool:
```bash
pip install pyqt6
```
## Contributing
We welcome contributions to the game! If you have ideas for new features, bug fixes, or improvements, feel free to fork the repository and submit a pull request. Before submitting, please ensure that your changes don’t break existing functionality.

### How to Contribute:
1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and commit them with a clear description.
4. Submit a pull request with a description of the changes.

## License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
