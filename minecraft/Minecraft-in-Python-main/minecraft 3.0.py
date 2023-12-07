
#these are the imports
import ursina
import random
import perlin_noise
from asyncio.windows_events import NULL
from ursina import *
from ursina.mesh_importer import *
from ursina.prefabs.first_person_controller import FirstPersonController
from perlin_noise import PerlinNoise
app = Ursina()
# getting the texures of blocks
grass_texture = load_texture("assets/grassreal_block.png")
stone_texture = load_texture("assets/stonereal_block.png")
brick_texture = load_texture("assets/brickreal_block.png")
dirt_texture = load_texture("assets/dirtreal_block.png")
glass_texture = load_texture("assets/glass_block.png")
glass_hand = load_texture("assets/glassblock_hand.png")
deepslate_texture = load_texture("assets/deepslatereal_block.png")
granite_texture = load_texture("assets/granitereal_block.png")
log_texture = load_texture("assets/oaklogreal_block.png")
planks_texture = load_texture("assets/oakplanksreal_block.png")
coalore_texture = load_texture("assets/coalore_block.png")
ironore_texture = load_texture("assets/ironore_block.png")
creeper_texture = load_texture("assets/creeper.png")
sky_texture = load_texture("assets/skybox.png")
arm_texture = load_texture("assets/arm_texture.png")
punch_sound = Audio("assets/punch_sound", loop=False, autoplay=False)
seednos = []
block_pick = 1
toggleP = False
toggleE = False
texture = grass_texture
bg = None
window.fps_counter.enabled = True
window.exit_button.visible = True

#update func
def update():
    global block_pick
    global texture
    global toggleP
    if held_keys["left mouse"] or held_keys["right mouse"]:
        hand.active()
    else:
        hand.passive()
    
    if held_keys["g"]:
        if block_pick < 9:
            time.sleep(0.1)
            block_pick = block_pick + 1
            block.selectBlock(texture)
        else:
            block_pick = block_pick
            block.selectBlock(texture)   
    if held_keys["f"]:
        if block_pick > 1: 
           time.sleep(0.1)
           block_pick = block_pick - 1
           block.selectBlock(texture)
        else:
           block_pick = block_pick
           block.selectBlock(texture)
    if held_keys["r"]:
        restart()
    if held_keys["p"]:
        if toggleP == False:
            mouse.visible = True
            mouse.locked = False
            window.fullscreen = False
            window.exit_button.enabled = True
            toggleP = True
        else:
            mouse.visible = False
            mouse.locked = True
            window.fullscreen = True
            window.exit_button.enabled = False
            toggleP = False
    if held_keys["escape"]:
        quit()


class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=grass_texture):
        super().__init__(
            parent=scene,
            position=position,
            model="block",
            origin_y=1,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            scale=0.5,
            collider="box",
        )

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                punch_sound.play()
                if block_pick == 1:
                    voxel = Voxel(
                        position=self.position + mouse.normal, texture=grass_texture
                    )
                if block_pick == 2:
                    voxel = Voxel(
                        position=self.position + mouse.normal, texture=stone_texture
                    )
                if block_pick == 3:
                    voxel = Voxel(
                        position=self.position + mouse.normal, texture=brick_texture
                    )
                if block_pick == 4:
                    voxel = Voxel(
                        position=self.position + mouse.normal, texture=dirt_texture
                    )
                if block_pick == 5:
                    voxel = Voxel(
                        position=self.position + mouse.normal, texture=glass_texture
                    )
                if block_pick == 6:
                    voxel = Voxel(
                        position=self.position + mouse.normal, texture=deepslate_texture
                    )
                if block_pick == 7:
                    voxel = Voxel(
                        position=self.position + mouse.normal, texture=granite_texture
                    )
                if block_pick == 8:
                    voxel = Voxel(
                        position=self.position + mouse.normal, texture=log_texture
                    )
                if block_pick == 9:
                    voxel = Voxel(
                        position=self.position + mouse.normal, texture=planks_texture
                    )
            if key == "right mouse down":
                punch_sound.play()
                destroy(self)


class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model="sky_dome",
            texture="sky_default",
            scale=150,
            double_sided=True,
        )


class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model="assets/arm",
            texture=arm_texture,
            scale=0.2,
            rotation=Vec3(150, -10, 0),
            position=Vec2(0.4, -0.6),
        )

    def active(self):
        self.position = Vec2(0.3, -0.5)

    def passive(self):
        self.position = Vec2(0.4, -0.6)


class Block(Entity):
    def __init__(self, texture):
        super().__init__(
            parent=camera.ui,
            model="block",
            texture=texture,
            scale=0.08,
            rotation=Vec3(60, 120, 50),
            position=Vec2(0.26, -0.20),
        )

    def selectBlock(self,texture):
        destroy(self)
        block = Block(texture)
        if block_pick == 1:
            texture = grass_texture
        elif block_pick == 2:
            texture = stone_texture
        elif block_pick == 3:
            texture = brick_texture
        elif block_pick == 4:
            texture = dirt_texture
        elif block_pick == 5:
            texture = glass_hand
        elif block_pick == 6:
            texture = deepslate_texture
        elif block_pick == 7:
            texture = granite_texture
        elif block_pick == 8:
            texture = log_texture
        elif block_pick == 9:
            texture = planks_texture
        print(texture)
        block = Block(texture)

seed = "12222333344443344444"
digitnos = random.randint(1,64)
for count in range(digitnos):
 seednos.append(str(random.randint(0,9)))
for count in range(0,digitnos):
 seed = seed + seednos[count]
 
seed = int(seed)
wh= random.randint(1,100000000000000000)
ht= random.randint(1,100000000000000000)
terrain_width = wh
terrain_height = ht
h = 0
prev_y = 1
noise = PerlinNoise(octaves = 34,seed = seed)
amp = 10
freq = 40
for i in range(terrain_width*terrain_width):
    voxel = Voxel(position = Vec3(floor(i/terrain_width),0,floor(i%terrain_width)),texture = grass_texture)
    y = floor(noise([voxel.x/freq, voxel.z/freq])*amp)+amp
    voxel.y = y
for h in range(terrain_height):
    for i in range(terrain_width*terrain_width):
        voxel = Voxel(position = Vec3(floor(i/terrain_width),y,floor(i%terrain_width)),texture = dirt_texture)
        y = (floor(noise([voxel.x/freq, voxel.z/freq])*amp)+amp)-(h+1)
        voxel.y = y

window.fullscreen = True

def restart():
    voxel = Voxel(position=Vec3(10, 34, 10),texture = None)
    player = FirstPersonController(
        position=Vec3(10, 32, 10), height=2, jumpHeight=1, gravity=1
    )
    


restart()
sky = Sky()
hand = Hand()
block = Block(texture)
app.run()
