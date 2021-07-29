import pygame

def init():
    pygame.init()
    win = pygame.display.set_mode((300, 300))

def getKey(keyName):
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    theKey = getattr(pygame,'K_{}'.format(keyName))
    if keyInput[theKey]:
        ans = True
    pygame.display.update()
    return ans

def main():
    if getKey("LEFT"):
        print("تم الضغط على اتجاه اليسار")
    if getKey("RIGHT"):
        print("تم الضغط على اتجاه اليمين")


if __name__ == '__main__':
    init()
    while True:
        main()