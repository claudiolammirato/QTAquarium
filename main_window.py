from PySide6.QtWidgets import QWidget, QPushButton, QSlider, QHBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Aquarium Smart")
        
        button = QPushButton("Press me!!!")
        button.setCheckable(True)
        #self.setCentralWidget(button)
        button.clicked.connect(self.button_clicked)

        slider = QSlider()
        slider.setMinimum(0)
        slider.setMaximum(100)
        slider.setValue(50)
        slider.valueChanged.connect(self.respond_to_slider)

        layout = QHBoxLayout()
        layout.addWidget(button)
        layout.addWidget(slider)
        self.setLayout(layout)
    
    
    def button_clicked(self, data):
            print("cliccato!!!", data)
        
    def respond_to_slider(data):
            print("slider Value: ", data)

