# напиши свій код тут
key_switch_camera = "c"  # камера прив'язана до героя чи ні
key_switch_mode = "z"  # можна проходити крізь перешкоди чи ні


key_forward = "w"  # крок вперед (куди дивиться камера)
key_back = "s"  # крок назад
key_left = "a"  # крок вліво (вбік від камери)
key_right = "d"  # крок вправо
key_up = "e"  # крок вгору
key_down = "q"  # крок вниз


key_turn_left = "n"  # поворот камери праворуч (а світу - ліворуч)
key_turn_right = "m"  # поворот камери ліворуч (а світу – праворуч)


def check_dir(self, angle):
    """повертає заокруглені зміни координат X, Y,
    відповідні переміщенню у бік кута angle.
    Координата Y зменшується, якщо персонаж дивиться на кут 0,
    та збільшується, якщо дивиться на кут 180.
    Координата X збільшується, якщо персонаж дивиться на кут 90,
    та зменшується, якщо дивиться на кут 270.
       кут 0 (від 0 до 20)      ->        Y - 1
       кут 45 (від 25 до 65)    -> X + 1, Y - 1
       кут 90 (від 70 до 110)   -> X + 1
       від 115 до 155            -> X + 1, Y + 1
       від 160 до 200            ->        Y + 1
       від 205 до 245            -> X - 1, Y + 1
       від 250 до 290            -> X - 1
       від 290 до 335            -> X - 1, Y - 1
       від 340                   ->        Y - 1"""
    if angle >= 0 and angle <= 20:
        return (0, -1)
    elif angle <= 65:
        return (1, -1)
    elif angle <= 110:
        return (1, 0)
    elif angle <= 155:
        return (1, 1)
    elif angle <= 200:
        return (0, 1)
    elif angle <= 245:
        return (-1, 1)
    elif angle <= 290:
        return (-1, 0)
    elif angle <= 335:
        return (-1, -1)
    else:
        return (0, -1)


class Hero:
    def __init__(self, pos, land):
        self.land = land
        self.mode = True  # режим проходження крізь усе
        self.hero = loader.loadModel("smiley")
        self.hero.setColor(1, 0.5, 0)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()

    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.setR(0)
        base.camera.setP(0)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)
        self.cameraOn = True

    def cameraUp(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2] - 3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False

    def changeView(self):
        if self.cameraOn == True:
            self.cameraUp()
        else:
            self.cameraBind()

    def accept_events(self):
        base.accept(key_switch_camera, self.changeView)

        base.accept(key_turn_left, self.turn_left)
        base.accept(key_turn_left + "-repeat", self.turn_left)

        base.accept(key_turn_right, self.turn_right)
        base.accept(key_turn_right + "-repeat", self.turn_right)

    def turn_left(self):
        self.hero.setH((self.hero.getH() + 5) % 360)

    def turn_right(self):
        self.hero.setH((self.hero.getH() - 5) % 360)
