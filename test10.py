def playing(best):
best 6 = -1
time = 3000
if best6 == 7:
choice()
game_layout_display.blit(post, (0, 0))
game_layout_display.blit(mother_board, (width_screen / 2 - 250, height_screen / 2 - 250))
xcr = xcy = xcg = xcb = 406 - 25
ycr = ycy = ycg = ycb = 606 - 25
game_layout_display.blit(red_c, (xcy, ycy))
if 5 &gt; best &gt; 1 or best == 21:
game_layout_display.blit(yellow_c, (xcy, ycy))
 
if 5 &gt; best &gt; 2 or best == 21:
game_layout_display.blit(green_c, (xcg, ycg))
 
if 5 &gt; best &gt; 2:
game_layout_display.blit(blue_c, (xcb, ycb))
gamer1 = "Player 1"
gamer1score = 0
if best == 21:
gamer2 = "Computer"
gamer2score = 0
if 5 &gt; best &gt; 1:
gamer2 = "Player 2"
gamer2score = 0
if 5 &gt; best &gt; 2:
gamer3 = "Player 3"
gamer3score = 0
if 5 &gt; best &gt; 3:
gamer4 = "Player 4"
gamer4score = 0
tips = 1
play = True
while True:
less = False
set = False
time = 3000
game_layout_display.blit(post, (0, 0))
game_layout_display.blit(mother_board, (width_screen / 2 - 250, height_screen / 2 - 250))
mouse = pygame.mouse.get_pos()
 
for event in pygame.event.get():
 
if event.type == pygame.QUIT:
Quit()
if event.type == pygame.KEYDOWN:
if event.key == pygame.K_ESCAPE:
Quit()
 
if best == 21:
if button1("Player 1", mouse[0], mouse[1], 100, 700, 200, 50, red_color, grey_color, 30):
if tips == 1:
gamer1score, less, set, six = turn(gamer1score, less, set)
if not six:
tips += 1
xcr, ycr = movement(gamer1score)
if gamer1score == 100:
time = pygame.time.get_ticks()
while pygame.time.get_ticks() - time &lt; 2000:
message_display1_screen("Player 1 Wins", 650, 50, 50, blue_color)
pygame.mixer.Sound.play(win)
pygame.display.update()
break
 
button1("Computer", mouse[0], mouse[1], 400, 700, 200, 50, yellow_color, grey_color, 30)
if True:
if tips == 2:
gamer2score, less, set, six = turn(gamer2score, less, set)
xcy, ycy = movement(gamer2score)
if not six:
tips += 1
if best &lt; 3 or best == 21:
tips = 1
 
if gamer2score == 100:
time_clock = pygame.time.get_ticks()
while pygame.time.get_ticks() - time_clock &lt; 2000:
message_display1_screen("Computer Wins", 650, 50, 50, black_color)
pygame.mixer.Sound.play(lose)
pygame.display.update()
break
if 5 &gt; best &gt; 1:
if button1("Player 1", mouse[0], mouse[1], 100, 700, 200, 50, red_color, grey_color, 30):
if tips == 1:
gamer1score, less, set, six = turn(gamer1score, less, set)
xcr, ycr = movement(gamer1score)
if not six:
tips += 1
if gamer1score == 100:
time_clock = pygame.time.get_ticks()
while pygame.time.get_ticks() - time_clock &lt; 2000:
message_display1_screen("Player 1 Wins", 650, 50, 50, black_color)
pygame.mixer.Sound.play(win)
pygame.display.update()
break
 
if button1("Player 2", mouse[0], mouse[1], 400, 700, 200, 50, yellow_color, grey_color, 30):
if tips == 2:
gamer2score, less, set, six = turn(gamer2score, less, set)
xcy, ycy = movement(gamer2score)
if not six:
tips += 1
if best &lt; 3:
tips = 1
 
if gamer2score == 100:
time_clock = pygame.time.get_ticks()
while pygame.time.get_ticks() - time_clock &lt; 2000:
message_display1_screen("Player 2 Wins", 650, 50, 50, black_color)
pygame.mixer.Sound.play(win)
pygame.display.update()
break
 
if 5 &gt; best &gt; 2:
if button1("Player 3", mouse[0], mouse[1], 700, 700, 200, 50, green_color, grey_color, 30):
if tips == 3:
gamer3score, less, set, six = turn(gamer3score, less, set)
xcg, ycg = movement(gamer3score)
if not six:
tips += 1
if best &lt; 4:
tips = 1
 
if gamer3score == 100:
time_clock = pygame.time.get_ticks()
while pygame.time.get_ticks() - time_clock &lt; 2000:
message_display1_screen("Player 3 Wins", 650, 50, 50, black_color)
pygame.mixer.Sound.play(win)
pygame.display.update()
break
 
if 5 &gt; best &gt; 3:
if button1("Player 4", mouse[0], mouse[1], 1000, 700, 200, 50, blue_color, grey_color, 30):
if tips == 4:
gamer4score, less, set, six = turn(gamer4score, less, set)
xcb, ycb = movement(gamer4score)
if not six:
tips += 1
if best &lt; 5:
tips = 1
 
if gamer4score == 100:
time_clock = pygame.time.get_ticks()
while pygame.time.get_ticks() - time_clock &lt; 2000:
message_display1_screen("Player 4 Wins", 650, 50, 50, black_color)
pygame.mixer.Sound.play(win)
pygame.display.update()
break
 
best6 = button("Back", mouse[0], mouse[1], 0, 0, 200, 50, red_color, blue_red_color, 30, 7)
game_layout_display.blit(red_c, (xcr, ycr))
if 5 &gt; best &gt; 1 or best == 21:
game_layout_display.blit(yellow_c, (xcy + 2, ycy))
 
if 5 &gt; best &gt; 2:
game_layout_display.blit(green_c, (xcg + 4, ycg))
 
if 5 &gt; best &gt; 3:
game_layout_display.blit(blue_c, (xcb + 6, ycb))
 
if less:
time_clock = pygame.time.get_ticks()
while pygame.time.get_ticks() - time_clock &lt; 2000:
message_display1_screen("There's a Ladder!", 650, 50, 35, black_color)
pygame.display.update()
if set:
time_clock = pygame.time.get_ticks()
while pygame.time.get_ticks() - time_clock &lt; 2000:
message_display1_screen("There's a Snake!", 650, 50, 35, black_color)
pygame.display.update()
 
time_clocks.tick(7)
pygame.display.update()