import pyautogui as pt

# pantalla_botonVideo="batalla_botonVideo.png"
pantalla_batalla="pantalla_batalla.png"
pantalla_cartas="pantalla_cartas.png"
pantalla_evento="pantalla_evento.png"
pantalla_tienda="pantalla_tienda.png"
summon="batalla_summon.png"



def init():
    # print(pt.size())
    while True:
        position=pt.locateCenterOnScreen(pantalla_batalla,region=(1000,0, 920, 1080), confidence=.8)
        if position==None:
            print("no")
        else:
            pt.moveTo(position)
            pt.click()
init()
# def pantalla():

#     if pt.locateCenterOnScreen(pantalla_batalla,region=(1000,0, 920, 1080), confidence=.8)!=None:
#         return "batalla"
#     elif pt.locateCenterOnScreen(pantalla_cartas,region=(1000,0, 920, 1080), confidence=.8)!=None:
#         return "cartas"
#     elif pt.locateCenterOnScreen(pantalla_evento,region=(1000,0, 920, 1080), confidence=.8)!=None:
#         return "evento"
#     elif pt.locateCenterOnScreen(pantalla_tienda,region=(1000,0, 920, 1080), confidence=.8)!=None:
#         return "tienda"

# init()