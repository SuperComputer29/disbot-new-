from someRandomFunctions.datechainnotsus import dateGen as dG
import time as t

date = dG()
while True:
    current_t = t.localtime()
    current_clock = t.strftime("%H%M", current_t)
    print(current_clock)
    if current_clock == "2329":
        print(date)