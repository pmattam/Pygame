import pygame

shape = "CIRCLE"

class Circles(object):

    def __init__(self, screen, display, circles_list):
        self.screen = screen
        self.display = display
        self.circles_list = circles_list
    
    def drawCircles(self):
        for circle in self.circles_list:
            pygame.draw.circle(self.display, circle["color"], (circle["x"], circle["y"]), circle["rad"], circle["fill"])
        pygame.display.update()
        for circle in self.circles_list:
            self.circlesUpdate(circle)
    
    def circlesUpdate(self, circle):
        circle["x"] += circle["dirx"]
        circle["y"] += circle["diry"]
        if circle["x"] + circle["rad"] > self.screen[0]:
            circle["dirx"] = -circle["dirx"]
        if circle["y"] + circle["rad"] > self.screen[1]:
            circle["diry"] = -circle["diry"]
        if circle["x"] - circle["rad"] < 0:
            circle["dirx"] = -circle["dirx"]
        if circle["y"] - circle["rad"] < 0:
            circle["diry"] = -circle["diry"]

class Squares(object):

    def __init__(self, screen, display, squares_list):
        self.screen = screen
        self.display = display
        self.squares_list = squares_list
    
    def drawSquares(self):
        for square in self.squares_list:
            pygame.draw.rect(self.display, square["color"], (square["x"], square["y"], square["width"], square["height"]), square["fill"])
        pygame.display.update()
        for square in self.squares_list:
            self.squaresUpdate(square)

    def squaresUpdate(self, square):
        square["x"] += square["dirx"]
        square["y"] += square["diry"]
        if square["x"] + square["width"] > self.screen[0]:
            square["dirx"] = -square["dirx"]
        if square["y"] + square["height"] > self.screen[1]:
            square["diry"] = -square["diry"]
        if square["x"] - square["width"] < 0:
            square["dirx"] = -square["dirx"]
        if square["y"] - square["height"] < 0:
            square["diry"] = -square["diry"]

class Rectangles(object):

    def __init__(self, screen, display, rectangles_list):
        self.screen = screen
        self.display = display
        self.rectangles_list = rectangles_list
    
    def drawRectangles(self):
        for rectangle in self.rectangles_list:
            pygame.draw.rect(self.display, rectangle["color"], (rectangle["x"], rectangle["y"], rectangle["width"], rectangle["height"]), rectangle["fill"])
        pygame.display.update()
        for rectangle in self.rectangles_list:
            self.rectanglesUpdate(rectangle)

    def rectanglesUpdate(self, rectangle):
        rectangle["x"] += rectangle["dirx"]
        rectangle["y"] += rectangle["diry"]
        if rectangle["x"] + rectangle["width"] > self.screen[0]:
            rectangle["dirx"] = -rectangle["dirx"]
        if rectangle["y"] + rectangle["height"] > self.screen[1]:
            rectangle["diry"] = -rectangle["diry"]
        if rectangle["x"] - rectangle["width"] < 0:
            rectangle["dirx"] = -rectangle["dirx"]
        if rectangle["y"] - rectangle["height"] < 0:
            rectangle["diry"] = -rectangle["diry"]

def getCircles():
    circ1 = {"x" : 100, "y" : 100, "rad" : 50, "dirx" : 5, "diry" : 5, "color" : (255, 0, 0), "fill" : 5}
    circ2 = {"x" : 300, "y" : 25, "rad" : 25, "dirx" : 10, "diry" : 10, "color" : (0, 155, 0), "fill" : 4}
    circ3 = {"x" : 700, "y" : 500, "rad" : 75, "dirx" : 10, "diry" : 10, "color" : (155, 155, 0), "fill" : 0}
    circ4 = {"x" : 250, "y" : 575, "rad" : 50, "dirx" : 5, "diry" : 5, "color" : (255, 155, 0), "fill" : 0}
    circ5 = {"x" : 400, "y" : 300, "rad" : 75, "dirx" : 5, "diry" : 5, "color" : (0, 155, 155), "fill" : 2}
    circ6 = {"x" : 25, "y" : 525, "rad" : 25, "dirx" : 10, "diry" : 10, "color" : (155, 155, 155), "fill" : 0}
    return [circ1, circ2, circ3, circ4, circ5, circ6]

def getSquares():
    sq1 = {"x" : 100, "y" : 100, "width" : 50, "height": 50, "dirx" : 5, "diry" : 5, "color" : (0, 255, 0), "fill" : 5}
    sq2 = {"x" : 300, "y" : 25, "width" : 100, "height": 100, "dirx" : 3, "diry" : 3, "color" : (10, 155, 10), "fill" : 4}
    sq3 = {"x" : 700, "y" : 500, "width" : 75, "height": 75, "dirx" : 15, "diry" : 15, "color" : (155, 155, 0), "fill" : 0}
    sq4 = {"x" : 250, "y" : 575, "width" : 75, "height": 75, "dirx" : 5, "diry" : 5, "color" : (255, 155, 100), "fill" : 0}
    sq5 = {"x" : 400, "y" : 300, "width" : 25, "height": 25, "dirx" : 25, "diry" : 25, "color" : (0, 155, 155), "fill" : 0}
    sq6 = {"x" : 25, "y" : 525, "width" : 60, "height": 60, "dirx" : 2, "diry" : 2, "color" : (155, 155, 155), "fill" : 3}
    return [sq1, sq2, sq3, sq4, sq5, sq6]

def getRectangles():
    rec1 = {"x" : 25, "y" : 525, "width" : 50, "height": 150, "dirx" : 5, "diry" : 5, "color" : (0, 255, 0), "fill" : 5}
    rec2 = {"x" : 400, "y" : 300, "width" : 100, "height": 125, "dirx" : 3, "diry" : 3, "color" : (10, 155, 10), "fill" : 4}
    rec3 = {"x" : 250, "y" : 575, "width" : 75, "height": 145, "dirx" : 4, "diry" : 4, "color" : (155, 155, 0), "fill" : 0}
    rec4 = {"x" : 700, "y" : 500, "width" : 125, "height": 75, "dirx" : 5, "diry" : 5, "color" : (255, 155, 100), "fill" : 0}
    rec5 = {"x" : 300, "y" : 25, "width" : 75, "height": 125, "dirx" : 7, "diry" : 7, "color" : (0, 155, 155), "fill" : 0}
    rec6 = {"x" : 100, "y" : 100, "width" : 90, "height": 60, "dirx" : 2, "diry" : 2, "color" : (155, 155, 155), "fill" : 3}
    return [rec1, rec2, rec3, rec4, rec5, rec6]


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = (900, 700)
    display = pygame.display.set_mode(screen)
    bg_img = pygame.image.load("bg_img.png")
    pygame.display.set_caption("Shapes")
    circles_list = getCircles()
    circles = Circles(screen, display, circles_list)
    squares_list = getSquares()
    squares = Squares(screen, display, squares_list)
    rectangles_list = getRectangles()
    rectangles = Rectangles(screen, display, rectangles_list)
    done = False

    while not done:
        display.blit(bg_img, (0,0))
        shapeName = pygame.font.Font('freesansbold.ttf', 30).render(shape, 1, (155, 155, 155))
        shapeRect = shapeName.get_rect()
        shapeRect.topleft = (390, 10)
        display.blit(shapeName, shapeRect)
        clickInfo = pygame.font.Font('freesansbold.ttf', 20).render("click on the shape name", 1, (155, 155, 155))
        clickRect = clickInfo.get_rect()
        clickRect.topleft = (350, 670)
        display.blit(clickInfo, clickRect)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                position = pygame.mouse.get_pos()
                if shapeRect.collidepoint(position):
                    update_shape(display)
            if event.type == pygame.QUIT:
                done = True
        if (shape == "CIRCLE"):   
            # circle_sound = pygame.mixer.Sound('circle.wma')
            # circle_sound.play()
            circles.drawCircles()
        elif (shape == "SQUARE"):
            squares.drawSquares()
        elif (shape == "TRIANGLE"):
            pygame.display.update()
        elif (shape == "RECTANGLE"):
            rectangles.drawRectangles()

        clock.tick(60)

    pygame.quit()

def update_shape(display):
    global shape
    if shape == "CIRCLE":
        shape = "SQUARE" 
    elif shape == "SQUARE":
        shape = "TRIANGLE"
    elif shape == "TRIANGLE":
        shape = "RECTANGLE"
    elif shape == "RECTANGLE":
        shape = "CIRCLE"
        
if __name__ == '__main__':
    main()


