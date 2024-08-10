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
        # QMainWindow.__init__(self)
        self.setupUi(self)
        self.setFixedSize(1085, 611)
        self.pushButton_simulate.clicked.connect(self.getValues)

    def getValues(self):
        initialvelocity = int(self.lineEditVelocity.text())
        angle_of_projection = int(self.spinBoxtheta.text())
        g = int(self.spinBox_g.text())
        scale = float(self.spinBox_scale.text())
        scale = scale if scale != 0 else 1.5
        time = float(self.spinBox_time.text())
        time = time if time != 0 else 0.1


        simulator = ProjectileSimulator(initialvelocity, angle_of_projection, g, scale, time)
        simulator.run_simulation()




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