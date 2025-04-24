# Hero of Embers - Version 0.3.1

## 📖 Table of Contents

- [Description](#description)
- [List to do](#to-do-list)
- [Installation](#installation)
- [Usage](#usage)
- [Plot](#plot)
- [Gameplay](#gameplay)
- [Plot Maker](#plot-maker)
- [Contributing](#contriburing)
- [License](#license)

<a name='description'></a>

## ✨ Description

**Hero of Embers** invites you into a **rich, evolving fantasy world**. You guide a young hero uncovering dangerous
secrets, forging alliances, and confronting a rising evil. Though the game is still under heavy development, key systems
like scene management, combat and narrative choices are already in place. Expect new content and mechanics in every
update!

<a name='to-do-list'></a>

## ✅ To do list

### The list of things I want to add, and the things that are already in game:

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
- [x] Add currency.
- [x] Add option to trade.
- [ ] Add more languages.
- [ ] Add level to enemies.
- [ ] Add more statistics to player.
- [ ] Remake plot.
- [ ] Expand the storyline with additional scenes and choices.
- [ ] Improve the user interface (e.g. color-coded text, better formatting).
- [ ] ~~Integrate sound and music~~.
- [ ] Include demo screenshots or GIFs in the README.md.

<a name='installation'></a>

## 🛠️ Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/McDjXdLol/Hero-of-Embers.git
    ```
2. Enter the project directory:
    ```bash
    cd Hero-of-Embers
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the game:
    ```bash
    python run_game.py
    ```

<a name='usage'></a>

## 🚀 Usage

Simply launch the game and follow on-screen prompts. Choices you make will influence the story’s outcome—be bold, but
choose wisely!

<a name='plot'></a>

## 📜 Plot (WIP)

You begin as a humble farmer drawn into a hidden destiny tied to the ancient **Protector** order. Alongside companions,
you unravel the conspiracy of the Hollow **Hand Cult** and seek the legendary sword Stormfang before darkness descends.

### 🗝️ Key Story Elements

- **The Protector**: An ancient order guarding the realm’s balance.

- **The Hollow Hand Cult**: A secretive group pursuing dark ambitions.

- **Stormfang**: A legendary blade essential to vanquishing evil.

<a name='gameplay'></a>

## 🎲 Gameplay

Experience a blend of **turn-based combat**, **branching narrative**, and **strategic choices.**

**Core Mechanics**:

- **Character Classes**:

    - **Protector**: Tanky, high defense & HP

    - **Fighter**: Balanced offense and defense

    - **Avenger**: High damage, lower survivability

- **Dynamic Combat**: HP, armor, damage stats

- **Inventory**: Acquire and manage gear

- **Currency**: Buy and sell stuff (WIP)

- **Choices** That Matter: Decisions alter the story path

- **Save & Load**: Resume your adventure at any time

<a name='plot-maker'></a>

## 📝 Plot Maker

The only GUI component of the project! Use `plot_maker_app.py` (requires PyQt6) to craft custom story scenes.

1. **Scene Name**: Enter a unique identifier for your scene.
2. **Description**: Provide the narrative text displayed to players.
3. **Add Scene**: Click to save, then re-enter the name to continue.
4. **Player Options**: Define choices (labels are case-insensitive).
5. **Option Description**: Briefly explain each choice.
6. **Effect**: Describe what happens after selection.
7. **Requirements**: Prevent options unless player has specific items.
8. **Items to Give**: Grant items for future use.
9. **Combat**: Toggle whether this option triggers a fight.
10. **Enemy Name**: Specify the enemy match from your library.
11. **Next Scene**: Link to the subsequent scene (existing or new).
12. **Add Option**: Save choice settings.
13. **New Scene**: Prepare to configure another scene.
14. **Save to File**: Export scenes.json for the game to load.

To run the plot maker:

```bash
python plot_maker_app.py
```

<a name='contriburing'></a>

### 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork the repo and submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

Please adhere to the existing code style and include tests where appropriate.

<a name="license"></a>

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

