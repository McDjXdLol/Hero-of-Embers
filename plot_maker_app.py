import sys
import json
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit,
    QPushButton, QTextEdit, QHBoxLayout, QFormLayout
)


class SceneBuilderApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Plot Maker")
        self.setGeometry(100, 100, 600, 600)

        self.loop = True
        self.options = {}
        self.scenes = {}

        # Main layout
        self.main_layout = QVBoxLayout()

        # Scene Name and Description
        self.scene_name_input = QLineEdit(self)
        self.scene_name_input.setPlaceholderText("Enter scene name")
        self.description_input = QLineEdit(self)
        self.description_input.setPlaceholderText("Enter scene description")
        self.add_scene_button = QPushButton("Add Scene", self)

        # Options
        self.option_name_input = QLineEdit(self)
        self.option_name_input.setPlaceholderText("Enter option ('a', 'b', etc.)")
        self.option_desc_input = QLineEdit(self)
        self.option_desc_input.setPlaceholderText("Option description")
        self.option_effect_input = QLineEdit(self)
        self.option_effect_input.setPlaceholderText("Option effect")
        self.option_req_input = QLineEdit(self)
        self.option_req_input.setPlaceholderText("Option requirements (items)")
        self.option_item_input = QLineEdit(self)
        self.option_item_input.setPlaceholderText("Item to give after option")

        self.option_combat_input = QPushButton("Is Combat: OFF", self)
        self.option_combat_input.setCheckable(True)
        self.option_combat_input.setChecked(False)
        self.option_combat_input.clicked.connect(self.toggle_combat)

        self.option_enemy_input = QLineEdit(self)
        self.option_enemy_input.setPlaceholderText("Enemy name (if any)")

        self.option_next_scene_input = QLineEdit(self)
        self.option_next_scene_input.setPlaceholderText("Next scene")

        self.add_option_button = QPushButton("Add Option", self)
        self.new_scene_button = QPushButton("New Scene", self)
        self.save_button = QPushButton("Save to File", self)

        # Display area for current scenes/options
        self.scenes_display = QTextEdit(self)
        self.scenes_display.setReadOnly(True)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Scene name and description layout
        scene_layout = QFormLayout()
        scene_layout.addRow("Scene Name:", self.scene_name_input)
        scene_layout.addRow("Description:", self.description_input)
        scene_layout.addWidget(self.add_scene_button)

        # Options layout
        option_layout = QFormLayout()
        option_layout.addRow("Option:", self.option_name_input)
        option_layout.addRow("Description:", self.option_desc_input)
        option_layout.addRow("Effect:", self.option_effect_input)
        option_layout.addRow("Requirements:", self.option_req_input)
        option_layout.addRow("Item to Give:", self.option_item_input)
        option_layout.addRow("Is Combat:", self.option_combat_input)
        option_layout.addRow("Enemy Name:", self.option_enemy_input)
        option_layout.addRow("Next Scene:", self.option_next_scene_input)
        option_layout.addWidget(self.add_option_button)

        # New scene and save button
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.new_scene_button)
        button_layout.addWidget(self.save_button)

        # Add widgets to the main layout
        layout.addLayout(scene_layout)
        layout.addLayout(option_layout)
        layout.addWidget(self.scenes_display)
        layout.addLayout(button_layout)

        # Set the main widget and layout
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Connect buttons to actions
        self.add_scene_button.clicked.connect(self.add_scene)
        self.add_option_button.clicked.connect(self.add_option)
        self.new_scene_button.clicked.connect(self.new_scene)
        self.save_button.clicked.connect(self.save_to_file)

    def toggle_combat(self):
        if self.option_combat_input.isChecked():
            self.option_combat_input.setText("Is Combat: ON")
        else:
            self.option_combat_input.setText("Is Combat: OFF")

    def add_scene(self):
        scene_name = self.scene_name_input.text().strip()
        description = self.description_input.text().strip()

        if scene_name and description:
            self.options[scene_name] = {"scene_name": scene_name, "description": description}
            self.scenes_display.append(f"Scene '{scene_name}' added.")
            self.clear_scene_inputs()
        else:
            self.scenes_display.append("Scene name and description cannot be empty.")

    def add_option(self):
        scene_name = self.scene_name_input.text().strip()
        option_name = self.option_name_input.text().strip()
        description = self.option_desc_input.text().strip()
        effect = self.option_effect_input.text().strip()
        requirements = self.option_req_input.text().strip()
        giving_item = self.option_item_input.text().strip()
        is_combat = self.option_combat_input.isChecked()
        enemy_name = self.option_enemy_input.text().strip()
        next_scene = self.option_next_scene_input.text().strip()

        if scene_name in self.options and option_name:
            self.options[scene_name][option_name] = {
                "description": description,
                "effect": effect,
                "requirements": requirements,
                "giving_item": giving_item,
                "is_combat": is_combat,
                "enemy_name": enemy_name,
                "next_scene": next_scene
            }
            self.scenes_display.append(f"Option '{option_name}' added to scene '{scene_name}'.")
            self.clear_option_inputs()
        else:
            self.scenes_display.append(f"Scene '{scene_name}' not found or option name is empty.")

    def new_scene(self):
        self.scene_name_input.clear()
        self.description_input.clear()

    def save_to_file(self):
        file_name = "scenes.json"
        with open(file_name, 'w') as f:
            json.dump(self.options, f, indent=4)
        self.scenes_display.append(f"Data saved to {file_name}.")

    def clear_scene_inputs(self):
        self.scene_name_input.clear()
        self.description_input.clear()

    def clear_option_inputs(self):
        self.option_name_input.clear()
        self.option_desc_input.clear()
        self.option_effect_input.clear()
        self.option_req_input.clear()
        self.option_item_input.clear()
        self.option_combat_input.setChecked(False)
        self.option_combat_input.setText("Is Combat: OFF")
        self.option_enemy_input.clear()
        self.option_next_scene_input.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SceneBuilderApp()
    window.show()
    sys.exit(app.exec())
