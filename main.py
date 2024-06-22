import pygame
import sys
import random


pygame.init()

# Değişkenler
width = 800
height = 500
ekran = pygame.display.set_mode((width, height))
font = pygame.font.SysFont(None, 30)
bullets = []
x_Pos=random.randint(390,420)
y_Pos=random.randint(240,260)
x_Vel = 1
y_Vel = 1
player_scores=0
player2_scores=0
pong = pygame.image.load("g/pong_map.png").convert_alpha()
pong = pygame.transform.scale(pong, (width, height))
menu = pygame.image.load("g/menu.png").convert_alpha()
menu = pygame.transform.scale(menu, (width, height))
go = pygame.image.load("g/game_over.png").convert_alpha()
go= pygame.transform.scale(go, (240, 380))
ses = pygame.mixer.Sound("g/pong_ses.wav")
ses2 = pygame.mixer.Sound("g/laser.wav")
scores = pygame.image.load('g/scores.png')
button_img = pygame.image.load('g/buton.png')
button_img2 = pygame.image.load('g/buton3.png')
button_img3 = pygame.image.load('g/buton2.png')
button_img4 = pygame.image.load('g/buton4.png')
button_img5 = pygame.image.load('g/buton5.png')
player_sayı=0
player2_sayı=0
buton=0

buton_genislik = 200
buton_yukseklik = 50
buton_x = (width - buton_genislik) // 2-22
buton_y = (height - buton_yukseklik) // 2+18

buton_genislik4 = 200
buton_yukseklik4 = 50
buton_x4 = (width - buton_genislik4) // 2-18
buton_y4 = (height - buton_yukseklik4) // 2+128

buton_genislik2 = 106
buton_yukseklik2 = 50
buton_x2 = (width - buton_genislik2) // 2-22
buton_y2 = (height - buton_yukseklik2) // 2+18

buton_genislik3 = 106
buton_yukseklik3 = 70
buton_x3 = (width - buton_genislik3) // 2+22
buton_y3 = (height - buton_yukseklik3) // 2+76

buton_genislik5 = 300
buton_yukseklik5 = 74
buton_x5 = (width - buton_genislik5) // 2+4
buton_y5 = (height - buton_yukseklik5) // 2+216

# Bullet Sınıfı
class Bullet:
    def __init__(self, x, y, color, speed):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 5
        self.color = color
        self.speed = speed
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    # Bullet haraketi 
    def move(self):
        self.x += self.speed
        self.rect.x = self.x

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

# Player 1 Sınıfı
class Character:
    def __init__(self, x, y, color, speed):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 90
        self.color = color
        self.speed = speed
        self.health = 100
        self.max_health = 100
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.can_shoot = True

    # Player 1 haraketi
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

        if self.y <= 20:
            self.y = 20
        if self.y >= height - 16 - self.height:
            self.y = height - 16 - self.height

        self.rect.topleft = (self.x, self.y)

    # Player 1 saldırısı
    def attack(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN] and self.can_shoot:
            bullet = Bullet(self.x, self.y + self.height // 2, (0, 193, 243), -20)
            bullets.append(bullet)
            self.can_shoot = False
            ses2.play()

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    # Player 1 sağlık çubuğu
    def draw_health_bar(self, surface):
        bar_width = 150
        bar_height = 20
        fill = (self.health / self.max_health) * bar_width

        outline_rect = pygame.Rect(10, 10, bar_width, bar_height)
        fill_rect = pygame.Rect(10, 10, fill, bar_height)

        pygame.draw.rect(surface, (0, 255, 0), fill_rect)
        pygame.draw.rect(surface, (0, 0, 0), outline_rect, 2)

    def hit(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

# Player 2 Sınıfı
class Character2:
    def __init__(self, x, y, color, speed):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 90
        self.color = color
        self.speed = speed
        self.health = 100
        self.max_health = 100
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.can_shoot = True

    # Player 2 haraketi
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed

        if self.y <= 20:
            self.y = 20
        if self.y >= height - 16 - self.height:
            self.y = height - 16 - self.height

        self.rect.topleft = (self.x, self.y)

    # Player 2 saldırısı
    def attack(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.can_shoot:
            bullet = Bullet(self.x + self.width, self.y + self.height // 2, (133, 0, 33), 20)
            bullets.append(bullet)
            self.can_shoot = False
            ses2.play()

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    # Player 2 sağlık çubuğu
    def draw_health_bar(self, surface):
        bar_width = 150
        bar_height = 20
        fill = (self.health / self.max_health) * bar_width

        outline_rect = pygame.Rect(640, 10, bar_width, bar_height)
        fill_rect = pygame.Rect(640, 10, fill, bar_height)

        pygame.draw.rect(surface, (0, 255, 0), fill_rect)
        pygame.draw.rect(surface, (0, 0, 0), outline_rect, 2)

    def hit(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

player = Character(740, height // 2, (0, 0, 0), 7)
player2 = Character2(30, height // 2, (0, 0, 0), 7)

clock = pygame.time.Clock()

# Oyunu baştan başlatmak
def reset_game():
    global x_Pos, y_Pos, x_Vel, y_Vel, bullets, player_sayı, player2_sayı, button_state
    x_Pos = random.randint(390, 420)
    y_Pos = random.randint(240, 260)
    x_Vel = 5
    y_Vel = 5
    bullets = []
    player.health = player.max_health
    player2.health = player2.max_health
    button_state = 0
    player2_sayı=0
    player_sayı=0

# Döngü
while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
      if event.type == pygame.KEYUP:
         if event.key == pygame.K_RETURN:
            player.can_shoot = True
         if event.key == pygame.K_SPACE:
            player2.can_shoot = True
      # Buton tıklamalarını ayarlama
      elif event.type == pygame.MOUSEBUTTONDOWN:
            fare_x, fare_y = pygame.mouse.get_pos()
            # buton==0 ise Menu ekranı açıldı, 
            # buton==1 ise Oyun başladı, 
            # buton==2 ise oyun bitti ve menu mü play again ekranı mi açıldı,
            # buton==3 ise score ekranı açıldı 
            if buton==0:
               if buton_x <= fare_x <= buton_x + buton_genislik and buton_y <= fare_y <= buton_y + buton_yukseklik:
                  buton=1
                  reset_game()

               if buton_x4 <= fare_x <= buton_x4 + buton_genislik4 and buton_y4 <= fare_y <= buton_y4 + buton_yukseklik4:
                     buton=3

            if buton==2:
                if button_img2 and (buton_x2-13) <= fare_x and fare_x<=buton_x2-13+buton_genislik2 and buton_y2 <= fare_y <= buton_y2 + buton_yukseklik2:
                    buton=0

                if button_img3 and button_img3 and (buton_x3-13) <= fare_x and fare_x<=buton_x3-13+buton_genislik3 and buton_y3 <= fare_y <= buton_y3 + buton_yukseklik3:
                 reset_game()
                 buton=1

            if buton==3:
               if button_img5 and button_img5 and (buton_x5-13) <= fare_x and fare_x<=buton_x5-13+buton_genislik5 and buton_y5 <= fare_y <= buton_y5 + buton_yukseklik5:
                 buton=0

    # Menuyü çiz
    if buton==0:
      ekran.blit(button_img4, (buton_x4, buton_y4))
      ekran.blit(button_img, (buton_x, buton_y))
      ekran.blit(menu, (0, 0))

    # Score ekranını çiz
    if buton==3:
        ekran.blit(button_img5, (buton_x5, buton_y5))
        ekran.blit(scores, (0, 0))
        font = pygame.font.Font(None, 80)
        text_surface = font.render(f"{player_scores}", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(width//2-210,320))
        text_surface2 = font.render(f"{player2_scores}", True, (0, 0, 0))
        text_rect2 = text_surface2.get_rect(center=(width//2+210,320))
        ekran.blit(text_surface, text_rect)
        ekran.blit(text_surface2, text_rect2)

    # Oyunu başlat
    if buton==1:
       # Playerları çiz
       kenar=pygame.draw.rect(ekran,(0, 0, 255), (0, 0, 16,500))
       kenar2=pygame.draw.rect(ekran,(0, 0, 255), (784, 0, 16,500))
       # Pong tahtasını çiz
       ekran.blit(pong, (0, 0))
       # Topu çiz
       pygame.draw.circle(ekran, (255, 127, 86), (x_Pos, y_Pos), 8)

       # Top hareketi
       x_Pos -= x_Vel
       y_Pos -= y_Vel

       # Top sekmesi
       if y_Pos > height - 26 or y_Pos < 26:
         y_Vel *= -1
         ses.play()

       # Playerlar ve Top  konum tanımlama
       player_rect = pygame.Rect(player.x, player.y, player.width, player.height)
       player2_rect = pygame.Rect(player2.x, player2.y, player2.width, player2.height)
       top_rect = pygame.Rect(x_Pos - 8, y_Pos - 8, 16, 16)

       # Kenar çarpışması , Player skor artışı
       if kenar.colliderect(top_rect):
          x_Pos=random.randint(390,420)
          y_Pos=random.randint(240,260)
          player2_sayı+=1

       if kenar2.colliderect(top_rect):
          x_Pos=random.randint(390,420)
          y_Pos=random.randint(240,260)
          player_sayı+=1

       # Top, Player çarpışması
       if player_rect.colliderect(top_rect):
           x_Vel*=-1
           y_Vel*=-1 
       if player2_rect.colliderect(top_rect):
            x_Vel*=-1
            y_Vel*=-1 

       # Playerların Metotunu tanımlama
       player.move()
       player.attack()

       player2.move()
       player2.attack()

       # Bullet ekleme
       for bullet in bullets:
         bullet.draw(ekran)

       # Bullet metotu ve Player, Bullet çarpışması
       for bullet in bullets[:]:
         bullet.move()
         if bullet.x < 0 or bullet.x > width:
           bullets.remove(bullet)
         else:
           if player_rect.colliderect(bullet.rect):
             player2.hit(8)
             bullets.remove(bullet)
           elif player2_rect.colliderect(bullet.rect):
             player.hit(8)
             bullets.remove(bullet)

       # Player 2 nin galibiyeti
       if player.health<=0 or player2_sayı>=3:
         font = pygame.font.Font(None, 40)
         text_surface = font.render("PLAYER 2 WIN", True, (0, 0, 0))
         text_rect = text_surface.get_rect(center=(width//2+5,40))

         ekran.blit(button_img2, (buton_x2-13, buton_y2-15))
         ekran.blit(button_img3, (buton_x2-13, buton_y2+40))
         ekran.blit(text_surface, text_rect)
         ekran.blit(go, (290, 60))
         y_Vel=0
         buton=2
         player2_scores+=1

       # Player 1 nin galibiyeti
       if player2.health<=0 or player_sayı>=3:
         font = pygame.font.Font(None, 40)
         text_surface = font.render("PLAYER WIN", True, (0, 0, 0))
         text_rect = text_surface.get_rect(center=(width//2+5,40))

         ekran.blit(button_img2, (buton_x2-13, buton_y2-15))
         ekran.blit(button_img3, (buton_x2-13, buton_y2+40))
         ekran.blit(text_surface, text_rect)
         ekran.blit(go, (290, 60))
         x_Vel=0
         y_Vel=0
         buton=2
         player_scores+=1

       # Player scorelerini oyun ekranında yazdırma
       font2 = pygame.font.Font(None, 60)
       text_surface = font2.render(f"{player_sayı}", True, (0, 0, 0))
       text_rect = text_surface.get_rect(center=(width//4,height//4-30))
       ekran.blit(text_surface, text_rect)
       text_surface2 = font2.render(f"{player2_sayı}", True, (0, 0, 0))
       text_rect2 = text_surface2.get_rect(center=(width//4+400,height//4-30))
       ekran.blit(text_surface2, text_rect2)

       # Playerları ve Health_Barları çizdirme
       player.draw(ekran)
       player.draw_health_bar(ekran)
       player2.draw(ekran)
       player2.draw_health_bar(ekran)

    pygame.display.flip()

    clock.tick(50)
