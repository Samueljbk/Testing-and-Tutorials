# Exercise 1: Create a simple window using PyQt
#
# Create a basic PyQt script that opens a window with the following requirements:
#
# Set the window title to "My First PyQt App"
# Set the window size to 300x200 pixels

# Exercise 2: Add a button and an action
#
# Modify the script from Exercise 1 to perform the following:
#
# Add a button to the window with the text "Click me!"
# Display an information message box with the text "Hello, PyQt!" when the button is clicked

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import sys


def on_button_click():
    QMessageBox.information(window, "Information", "Hello, PyQt")


# Create the application object
app = QApplication(sys.argv)

# Create the main window
window = QMainWindow()
window.setWindowTitle("My First PyQt App")
window.setGeometry(300, 200, 400, 300)

# Creating a button
button = QPushButton("Click me!", window)
button.setToolTip("This is an example button")
button.move(150, 150)
button.clicked.connect(on_button_click)

# Show the window
window.show()

# Execute the event loop
sys.exit(app.exec_())
