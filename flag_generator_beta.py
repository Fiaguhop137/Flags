import pygame,threading
pygame.init()
HEIGHT=360
WIDTH=int(HEIGHT*4/3)
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Flag generator (beta)")
clock=pygame.time.Clock()
code=""
last_code=code
def terminal_input():
    global code
    while True:
        try:
            text=input("Paste or type your code here: ").strip().lower()
            code="".join([c for c in text if c in "0123456789abcdef"])
        except EOFError:
            break
def main():
    global code
    global last_code
    threading.Thread(target=terminal_input,daemon=True).start()
    running,fps=True,24
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        if code!=last_code:
            screen.fill((0,0,0))
            stripe_count=len(code)//6
            for i in range(stripe_count):
                y1=i*HEIGHT//stripe_count
                y2=(i+1)*HEIGHT//stripe_count
                r=int(code[i*6:i*6+2],16)
                g=int(code[i*6+2:i*6+4],16)
                b=int(code[i*6+4:i*6+6],16)
                pygame.draw.rect(screen,(r,g,b),(0,y1,WIDTH,y2-y1))
            pygame.display.flip()
            last_code=code
        clock.tick(fps)
main()
pygame.quit()
