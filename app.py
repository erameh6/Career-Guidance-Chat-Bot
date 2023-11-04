import sys
import openai
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox,
    QTextEdit
)

openai.api_key = "YOUR_OPENAI_API_KEY"

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Create the widgets
        self.logo_label = QLabel()
        self.logo_pixmap = QPixmap('robot.png').scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.logo_label.setPixmap(self.logo_pixmap)

        self.input_label = QLabel('Ask about your career path:')
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText('Type Here...')
        self.answer_label = QLabel('Career Advice:')
        self.answer_field = QTextEdit()
        self.answer_field.setReadOnly(True)

        # Generate a color for button background
        button_color = QColor(0, 174, 255)  # RGB value for a shade of blue
        self.submit_button = QPushButton('Get Advice')
        self.submit_button.setStyleSheet(
            f"""
            QPushButton {{
                background-color: {button_color.name()};
                border: none;
                color: red;
                padding: 15px 32px;
                font-size: 18px;
                font-weight: bold;
                border-radius: 18px;
                }}
            QPushButton:hover {{
                background-color: {button_color.lighter(110).name()};
            }}
            """
        )

        # ... (same popular questions layout as before)

        # Create a layout
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignCenter)

        # ... (same widget addition to layout as before)

        # Set the layout
        self.setLayout(layout)

        # Set the window properties
        self.setWindowTitle('Career Path Advisor')
        self.setGeometry(200, 200, 600, 600)

        # Connect the submit button to the function which queries OpenAI API
        self.submit_button.clicked.connect(self.get_answer)

    def get_answer(self):
        question = self.input_field.text()

        completion = openai.Completion.create(
            engine="davinci",
            prompt=f"You are a career advisor. Provide advice on the career path for someone interested in {question}. Include the steps and skills required.",
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7
        )

        answer = completion.choices[0].text.strip()

        self.answer_field.setText(answer)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
