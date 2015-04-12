import time

def mclick(i):
    if exists(i):
        time.sleep(1)
        m = find(i)
        hover(m)
        print(m)
        m.mouseMove()
        m.click()
        time.sleep(1)

while True:
    time.sleep(1)
    try:
        time.sleep(1)
        if find("1428843888287.png"):
            switchApp("EasyUO")
            mclick("1428839892356.png")
            mclick("1428840036362.png")
    except:
        time.sleep(1)
    try:
        if find("1428839970411.png"):
            switchApp("Ultima Online")
            mclick("1428845018827.png")
            print("toto")
            switchApp("EasyUO")
            mclick("1428840007966.png")
            mclick("1428840036362.png")
    except:
        time.sleep(1)
