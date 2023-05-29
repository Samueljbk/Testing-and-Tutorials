# Exercise 1: Create a simple window using PyQt
#
# Create a basic PyQt script that opens a window with the following requirements:
#
# Set the window title to "My First PyQt App"
# Set the window size to 300x200 pixels

from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

# Create the application object
app = QApplication(sys.argv)

# Create the main window
window = QMainWindow()
window.setWindowTitle("My First PyQt App")
window.setGeometry(300, 200, 400, 300)

# Show the window
window.show()

# Execute the event loop
sys.exit(app.exec_())
