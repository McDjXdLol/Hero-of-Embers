# Plot Maker (WIP)
## About
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


### To run the plot maker:

```python 
python run_plot_maker.py
```

## Plans
So the **plot maker is not done yet**. There is still few variables to add to app, so the game could read it.
But making plot maker is kinda hard. Because if I add something to plot file i have to add it to Plot Maker app.
And after few last updates I added a bunch of variables, and I forgot about adding all of them to Plot Maker.
So for now it's pretty much not working "enough".
