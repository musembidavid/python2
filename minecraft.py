from ursina import *
from ursina.prefabs.third_person_controller import ThirdPersonController

app = Ursina()
Sky(texture='sky_sunset')
player = ThirdPersonController()

boxes = []
for n in range(992):
  for k in range(1992):
    box = Button(color=color.white, model='cube', position=(k,0,n),
                 texture='block.png',parent=scene, origin_y=0.5)
    boxes.append(box)

def input(key):
  for box in boxes:
    if box.hovered:
      if key == 'left mouse down':
        new = Button(color=color.white, model='cube',position= box.position + mouse.normal,
                     texture= 'block.png', parent=scene, origin_y=0.5)
        boxes.append(new)
      
      if key == 'right mouse down':
        boxes.remove(box)
        destroy(box)
        if key == 'e':
          boxes.append(new)
app.run()