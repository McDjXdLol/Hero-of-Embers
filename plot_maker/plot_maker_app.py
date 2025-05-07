import sys
import json
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit,
    QPushButton, QTextEdit, QHBoxLayout, QFormLayout
)
from PyQt6.QtGui import QFont, QPalette, QColor, QIcon
import html

class SceneBuilderApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Plot Maker")
        self.setGeometry(100, 100, 1200, 800)
        self.setWindowIcon(QIcon("icon.ico"))
        self.loop = True
        self.options = {}
        self.scenes = {}

        self.main_layout = QHBoxLayout()

        self.form_layout = QVBoxLayout()

        self.scene_name_input = QLineEdit(self)
        self.scene_name_input.setPlaceholderText("Enter scene name")
        self.description_input = QLineEdit(self)
        self.description_input.setPlaceholderText("Enter scene description")
        self.add_scene_button = QPushButton("Add Scene", self)

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

        self.scenes_display = QTextEdit(self)
        self.scenes_display.setReadOnly(True)

        self.json_output_display = QTextEdit(self)
        self.json_output_display.setReadOnly(True)
        self.json_output_display.setFont(QFont("Courier New", 10))

        palette = self.json_output_display.palette()
        palette.setColor(QPalette.ColorRole.Base, QColor(255, 255, 255, 0))
        self.json_output_display.setPalette(palette)


        self.setup_ui()
        self.update_json_output()

    def setup_ui(self):
        form_layout = QFormLayout()
        form_layout.addRow("Scene Name:", self.scene_name_input)
        form_layout.addRow("Description:", self.description_input)
        form_layout.addWidget(self.add_scene_button)

        form_layout.addRow("Option:", self.option_name_input)
        form_layout.addRow("Description:", self.option_desc_input)
        form_layout.addRow("Effect:", self.option_effect_input)
        form_layout.addRow("Requirements:", self.option_req_input)
        form_layout.addRow("Item to Give:", self.option_item_input)
        form_layout.addRow("Is Combat:", self.option_combat_input)
        form_layout.addRow("Enemy Name:", self.option_enemy_input)
        form_layout.addRow("Next Scene:", self.option_next_scene_input)
        form_layout.addWidget(self.add_option_button)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.new_scene_button)
        button_layout.addWidget(self.save_button)

        button_widget = QWidget()
        button_widget.setLayout(button_layout)
        form_layout.addRow("", button_widget)

        form_layout.addRow("Scenes Display:", self.scenes_display)

        self.main_layout.addLayout(form_layout)
        self.main_layout.addWidget(self.json_output_display)

        central_widget = QWidget(self)
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

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
            self.scenes_display.append(f"Scene '{html.escape(scene_name)}' added.")
            self.clear_scene_inputs()
            self.update_json_output()
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
            self.scenes_display.append(f"Option '{html.escape(option_name)}' added to scene '{html.escape(scene_name)}'.") 
            self.clear_option_inputs()
            self.update_json_output()
        else:
            self.scenes_display.append(f"Scene '{scene_name}' not found or option name is empty.")

    def new_scene(self):
        self.scene_name_input.clear()
        self.description_input.clear()

    def save_to_file(self):
        file_name = f"../hero_of_embers/languages/scenes_en.json"
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
        self.option_enemy_input.clear()
        self.option_next_scene_input.clear()

    def update_json_output(self):
        self.json_output_display.clear()
        formatted_text = "<div style='font-family: Arial, sans-serif; color: #FFFFFF; background-color: transparent; border: 2px solid white'>"
        for scene_name, scene_data in self.options.items():
            formatted_text += f"<div style='margin-bottom: 15px; padding: 10px;'>"
            formatted_text += f"<h3 style='color: #2196F3; margin-bottom: 5px; text-align: center;'><span style='font-weight: bold;'>{html.escape(scene_data.get('scene_name', ''))}</span></h3>"
            formatted_text += f"<p style='margin-bottom: 10px;'><b></b> {html.escape(scene_data.get('description', ''))}</p>"
            formatted_text += f"<hr>"
            formatted_text += "<h4 style='color: #FFC107; margin-bottom: 5px;'>Options:</h4>"
            for option_name, option_data in scene_data.items():
                if option_name not in ['scene_name', 'description']:
                    formatted_text += f"<div style='margin-left: 20px; margin-bottom: 10px;'>"
                    formatted_text += f"<h5 style='color: #9C27B0; margin-bottom: 5px;'>Option: <span style='font-weight: normal;'>{html.escape(option_name)}</span></h5>" 
                    formatted_text += f"<p style='margin-bottom: 5px;'><b>Description:</b> {html.escape(option_data.get('description', ''))}</p>"  
                    formatted_text += f"<p style='margin-bottom: 5px;'><b>Effect:</b> {html.escape(option_data.get('effect', ''))}</p>" 
                    formatted_text += f"<p style='margin-bottom: 5px;'><b>Requirements:</b> {html.escape(option_data.get('requirements', ''))}</p>"  
                    formatted_text += f"<p style='margin-bottom: 5px;'><b>Item to Give:</b> {html.escape(option_data.get('giving_item', ''))}</p>" 
                    formatted_text += f"<p style='margin-bottom: 5px;'><b>Is Combat:</b> {'<span style=\"color: red;\">ON</span>' if option_data.get('is_combat', False) else '<span style=\"color: green;\">OFF</span>'}</p>"
                    formatted_text += f"<p style='margin-bottom: 5px;'><b>Enemy Name:</b> {html.escape(option_data.get('enemy_name', ''))}</p>" 
                    formatted_text += f"<p style='margin-bottom: 5px;'><b>Next Scene:</b> {html.escape(option_data.get('next_scene', ''))}</p>"  
                    formatted_text += "</div>"
            formatted_text += "</div>"
        formatted_text += "</div>"
        self.json_output_display.setHtml(formatted_text)
        self.json_output_display.repaint()
        self.json_output_display.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SceneBuilderApp()
    window.show()
    sys.exit(app.exec())
