# Hero of Embers (WIP)
### List of content:
- [Description](#Description)
- [Plot](#Plot)
- [Plot Writer](#plot-writer)
## Description
This is a simple work-in-progress (WIP) console-based fantasy RPG game. Currently, it's not exported to an executable and lacks a click-to-play feature. To test the mechanics, you need to run the Python file via `main.py`. At this stage, the plot consists only of scene names.

## Plot
The story follows a young farmer who arrives in a city and soon becomes involved in a mysterious ancient threat. After meeting a strange girl, they uncover secrets about an ancient order and a legendary weapon. As they grow stronger, they get caught in a dangerous cult's web, facing tough choices and powerful enemies. The hero must uncover hidden conspiracies and prepare for a final battle that will determine the fate of the world.

<a name="plot-writer"></a>
## Plot Writer
You can create your own plot by running the plot_maker_app.py file. Please note that you will need to install pyqt6 for this feature, as it's the only instance where a GUI is used.

![plot_maker_app](https://github.com/user-attachments/assets/3de29f7b-2386-4b59-a951-2fc930a22077)
1. Enter the scene name, which you will need later to jump to this scene.

2. Add a description to tell the player what is happening.

3. Click "Add Scene." Then, write the name of the scene again. You can add options for the player to make at this point.

4. The option value represents a choice the player can make later. Use simple letters or numbers. Capitalization doesn't affect gameplay mechanics, but the player will see it as typed.

5. Write a description of the option (e.g., "run away," "stay," "fight," etc.).

6. The effect shows what happens after the player chooses this option.

7. Requirements specify which items the player must have to select this option (e.g., the option to eat berries if the player has them).

8. Use the "Items to Give" field to give the player items they will need later.

9. Specify whether a combat encounter occurs after selecting the option.

10. Set the enemy name for combat. (Ensure the name matches exactly what's in the library.py file.)

11. Define the next scene that opens after selecting this option (you can type a scene name even if it doesn't exist yet).

12. Click "Add Option" to add as many options as needed.

13. After adding all options, click "New Scene" to start again.

14. When you're done, click "Finish" to complete the plot.

