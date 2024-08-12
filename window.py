import os
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox, QLabel, QPushButton, QSpinBox, QTableWidget, QDialog, QFileDialog, QGraphicsDropShadowEffect, QWidget
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtGui import QColor
from PyQt5.uic import loadUiType
from projectile import ProjectileSimulator


def get_resource_path(relative_path:str): 
    if getattr(sys, "frozen", False):
        base_dir = sys._MEIPASS
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))

    base_path = os.path.join(base_dir, relative_path)
    return base_path

APP_NAME = "Python Projectilve Simulator"
ui, _ = loadUiType(get_resource_path('mainwindow.ui'))

class MainWindow(QMainWindow, ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(735, 611)
        self.pushButton_simulate.clicked.connect(self.getValues)

    def getValues(self):
        try:
            # Try to convert the input values to integers
            initialvelocity = int(self.lineEditVelocity.text())
            angle_of_projection = int(self.spinBoxtheta.text())
            
            # Continue with simulation logic
            simulator = ProjectileSimulator(initialvelocity, angle_of_projection)
            simulator.run_simulation()
        
        except ValueError:
            # Show an error message if the conversion fails
            self.showErrorMessage("Invalid input", "Please enter valid numeric values.")
        except Exception as e:
            # Catch any other exceptions and show the error message
            self.showErrorMessage("Error", f"An unexpected error occurred: {str(e)}")
            

    def showErrorMessage(self, title, message):
        # Create a message box to display the error
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.exec_()

def main():
    # Initialize the application
    app = QApplication(sys.argv)
    # Create and show the main window
    mainWindow = MainWindow()
    mainWindow.show()
    
    # Start the application event loop
    sys.exit(app.exec_())

# Entry point for standalone execution
if __name__ == "__main__":
    main()
