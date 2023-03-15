import sys
import time
from PyQt5.QtWidgets import QApplication
import hands
start = time.perf_counter()
app = QApplication(sys.argv)

print(hands.judge_direction(2))  # 判断 上
end = time.perf_counter()
print(end-start)
sys.exit(app.exec_())
