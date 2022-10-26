import pygame
import functions as func
import data as data
import threading, time

pygame.init()
pygame.font.init()


clock = pygame.time.Clock()
global win
win = pygame.display.set_mode((data.width, data.height), pygame.RESIZABLE)

font = pygame.font.Font(None, 25)
MsmllArial = pygame.font.SysFont('Arial', 30)
smllArial = pygame.font.SysFont('Arial', 20)
Arial = pygame.font.SysFont('Arial', 35)

prevTime = time.time()

logo = pygame.image.load("./src/assets/logo.ico")
pygame.display.set_caption(data.name + " " + data.version)
pygame.display.set_icon(logo)
Running = data.running
tick = 1
class box:
  def __init__(self):
    self.xvel = 0.3 * data.width
    self.yvel = 0.35 * data.height
    self.x = 80
    self.y = 100
    self.sizex = 30
    self.sizey = 30
    
    
    
  def draw(self, color):
        global colide
        # print(mouse_pos)
        if self.x <= 0:
          self.xvel = abs(self.xvel)
          
        if self.x+self.sizex >= data.width:
          self.xvel = -abs(self.xvel)
        if self.y <= 0:
          self.yvel = abs(self.yvel)
        if self.y + self.sizey >= data.height:
          self.yvel = -abs(self.yvel)
        
        
        pygame.draw.rect(win, color, (self.x, self.y, self.sizex, self.sizey))
        
  def move(self):
    global Dt
    self.x = self.x + self.xvel * abs(Dt)
    self.y = self.y + self.yvel * abs(Dt)
    
    
        
box = box()

def UpdateRes():
  newW = pygame.display.Info().current_w
  newH = pygame.display.Info().current_h
  if newH != data.height or newW != data.width:
    
    data.width = newW
    data.height = newH
    box.xvel = 0
    box.yvel = 0
    box.xvel = 0.3 * data.width
    box.yvel = 0.35 * data.height
  

def UpdateTick():
  global tick
  global Running
  while Running:
    pygame.display.Info()
    if tick >= 1536:
      tick = 1
    tick = tick + 1
    #print(tick)
    time.sleep(0.02)

def  main():
  global Dt
  global Running
  global tick
  global prevTime
  while Running:
    
    
    
    now = time.time()
    Dt = prevTime - now
    prevTime = now
    win.fill(data.color.BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    framerate = round(clock.get_fps(), 1)
    if data.verbos == True:
      win.blit(font.render("FPS: {}".format(framerate),
             True, data.color.BLUE3), (10, 10))
      win.blit(font.render("DeltaTime: {}".format(round(Dt, 5)),
             True, data.color.BLUE3), (10, 30))
      win.blit(font.render("Position: ({}, {})".format(round(box.x, 1), round(box.y, 1)),
             True, data.color.BLUE3), (10, 50))
    box.draw(func.rainbow_color(tick))
    box.move()
    pygame.display.update()
    clock.tick()
    UpdateRes()
  pass


if __name__ == '__main__':
  tickThread =threading.Thread(target=UpdateTick)
  tickThread.start()
  main()