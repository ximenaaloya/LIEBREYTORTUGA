import time
from PyQt6.QtCore import QThread, pyqtSignal

class SubProceso(QThread):
    actualizar = pyqtSignal(int, int)

    def __init__(self, label, tiempo, tipo):
        super().__init__()
        self.label = label
        self.tiempo = tiempo
        self.tipo = tipo

    def run(self):
        while True:
            x = self.label.x()
            y = self.label.y()

            if x < 550 and y <250:
                x += 10

            elif x >= 550 and y < 250:
                y += 10
            elif x > 10 and y >=250:
                x -= 10
            if self.tipo == "Liebre" and y == 250 and x == 400:
                time.sleep(6)
            print(f"y: {y}")
            print(f"x: {x}")
            self.actualizar.emit(x, y)
            time.sleep(self.tiempo / 1000.0)