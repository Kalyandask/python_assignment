import sys
import os

# Add the root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from database.database import get_inventory, add_item, remove_item, update_quantity

class InventoryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.label = QLabel("Inventory:")
        self.layout.addWidget(self.label)

        self.inventory_label = QLabel("")
        self.layout.addWidget(self.inventory_label)

        self.update_inventory()

        self.buy_button = QPushButton("Buy Item")
        self.buy_button.clicked.connect(self.buy_item)
        self.layout.addWidget(self.buy_button)

        self.return_button = QPushButton("Return Item")
        self.return_button.clicked.connect(self.return_item)
        self.layout.addWidget(self.return_button)

        self.setLayout(self.layout)

    def update_inventory(self):
        inventory = get_inventory()
        text = "\n".join([f"{name}: {quantity}" for name, quantity in inventory])
        self.inventory_label.setText(text)

    def buy_item(self):
        add_item("Item1", 1)
        self.update_inventory()

    def return_item(self):
        remove_item("Item1")
        self.update_inventory()

if __name__ == '__main__':
    app = QApplication([])
    window = InventoryApp()
    window.show()
    app.exec_()