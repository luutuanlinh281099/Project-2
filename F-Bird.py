#thêm thư viện
import pygame
from random import randint
#tạo 1 pygame và khai báo các giá trị
pygame.init()
#tạo màn hình, tên game, thời gian, âm thanh, phông chữ, điểm
screen = pygame.display.set_mode((500,700))
pygame.display.set_caption('Luu Tuan Linh')
clock = pygame.time.Clock()
sound = pygame.mixer.Sound('no6.wav')
font1 = pygame.font.SysFont('Arial', 30)
font2 = pygame.font.SysFont('Arial', 50)
diem = 0
WHITE = (255,255,255)
YELLOW = (255,255,0)
RED = (255,0,0)
#tạo vị trí lúc đầu của 3 ống
tube1_x = 250
tube2_x = 500
tube3_x = 750
#chiều rộng của ống
tube_width = 50
#chiều cao của ống
tube1_height = randint(100,500)
tube2_height = randint(100,500)
tube3_height = randint(100,500)
#khoảng cách giữa 2 ống đối nhau
kc = 150
#vận tốc các đối tượng
tube_vt = 5
bird_vt = 0
bird_tl = 0.5
#tọa độ bắt đâu của chim
bird_x = 50
bird_y = 350 
#hình ảnh của ống, nền, cát, chim
tube_img = pygame.image.load('images/tube.png')
tube_op_img = pygame.image.load('images/tube_op.png')
background_img = pygame.image.load('images/background.png')
background_img = pygame.transform.scale(background_img,(500,700))
sand = pygame.image.load('images/sand.png')
sand = pygame.transform.scale(sand,(500,200))
bird_img = pygame.image.load('images/bird.png')
bird_img = pygame.transform.scale(bird_img,(40,40))
#trạng thái của ống đã đc đi qua chưa
tube1_pass = False
tube2_pass = False
tube3_pass = False
#trạng thái game
running = True
display = 1
while running == True:
    #âm thanh
    pygame.mixer.Sound.play(sound)
    #tạo fps
    clock.tick(30)  
    #tạo nền 
    screen.fill(WHITE)
    #thêm background
    screen.blit(background_img,(0,0))
    #tạo cát
    screen.blit(sand,(0,600))
    #tạo điểm
    diem_text = font1.render("ĐIEM : " + str(diem), True, YELLOW)
    screen.blit(diem_text,(150,5))
    #thêm ống 1 
    tube1_img = pygame.transform.scale(tube_img,(tube_width, tube1_height))
    tube1 = screen.blit(tube1_img,(tube1_x,0))
    #thêm ống 2
    tube2_img = pygame.transform.scale(tube_img,(tube_width, tube2_height))
    tube2 = screen.blit(tube2_img,(tube2_x,0))
    #thêm ống 3
    tube3_img = pygame.transform.scale(tube_img,(tube_width, tube3_height))
    tube3 = screen.blit(tube3_img,(tube3_x,0))
    #thêm ống đối diện 1 
    tube1_op_img = pygame.transform.scale(tube_op_img,(tube_width,800-(tube1_height + kc)))
    tube1_op = screen.blit(tube1_op_img,(tube1_x,tube1_height + kc))
    #thêm ống đối diện 2
    tube2_op_img = pygame.transform.scale(tube_op_img,(tube_width,800-(tube2_height + kc)))
    tube2_op = screen.blit(tube1_op_img,(tube2_x,tube2_height + kc))
    #thêm ống đối diện 3
    tube3_op_img = pygame.transform.scale(tube_op_img,(tube_width,800-(tube3_height + kc)))
    tube3_op = screen.blit(tube1_op_img,(tube3_x,tube3_height + kc))  
    #thêm con chim
    bird = screen.blit(bird_img,(bird_x,bird_y))
    #chim rơi
    bird_y = bird_y + bird_vt
    bird_vt = bird_vt + bird_tl
    #ống di chuyển
    tube1_x = tube1_x - tube_vt
    tube2_x = tube2_x - tube_vt
    tube3_x = tube3_x - tube_vt
    #tạo ống mới khi đi hết chiều rộng ống
    if tube1_x < -tube_width:
        tube1_x = 700
        tube1_y = randint(100,500)
        tube1_pass = False
    if tube2_x < -tube_width:
        tube2_x = 700
        tube2_y = randint(100,500)
        tube2_pass = False
    if tube3_x < -tube_width:
        tube3_x = 700
        tube3_y = randint(100,500)
        tube3_pass = False
    #cộng điểm
    if tube1_x + tube_width < bird_x and tube1_pass == False:
        diem = diem + 1
        tube1_pass = True
    if tube2_x + tube_width < bird_x and tube2_pass == False:
        diem = diem + 1
        tube2_pass = True
    if tube3_x + tube_width < bird_x and tube3_pass == False:
        diem = diem + 1
        tube3_pass = True
    #va chạm vs ống
    tubes = [tube1,tube2,tube3,tube1_op,tube2_op,tube3_op]
    for tube in tubes:
        if bird.colliderect(tube):
            pygame.mixer.pause()
            tube_vt = 0
            bird_vt = 0
            lose = font2.render("GAME OVER", True, RED)
            lose_score = font2.render("ĐIEM : " + str(diem), True, RED)
            screen.blit(lose,(150,300))
            screen.blit(lose_score,(150,350))
    #rơi chạm đất hoặc trần
    if bird_y < 0 or bird_y > 700:
        pygame.mixer.pause()
        tube_vt = 0 
        bird_vt = 0
        lose = font2.render("GAME OVER", True, RED)
        lose_score = font2.render("ĐIEM : " + str(diem), True, RED)
        screen.blit(lose,(150,300))
        screen.blit(lose_score,(150,350))
    #bắt đầu game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #nhấn Space
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_vt = 0
                bird_vt = bird_vt - 5
    pygame.display.flip()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_KP_ENTER:
            running = True
pygame.quit()
