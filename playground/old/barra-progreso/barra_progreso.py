from time import sleep

def progress_bar(part, total, tamano = 15):
    frac = part / total
    completed = int(frac * tamano)
    missing = tamano - completed
    bar = f"[{'*' * completed}{'-' * missing}] {frac:.1%}"
    return bar

n = 30
for i in range(n + 1):
    sleep(0.1)
    print(progress_bar(i, n, 15), end="\r")
    if i == 30:
        print(progress_bar(i, n, 15))
