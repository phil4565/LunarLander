# Lunar Lander: AI-controlled play

# Instructions:
#   Land the rocket on the platform within a distance of plus/minus 20, 
#   with a horizontal and vertical speed less than 20
#
# Controlling the rocket:
#    arrows  : Turn booster rockets on and off
#    r       : Restart game
#    q / ESC : Quit

from LunarLander import *

xstart = 0 + 300*(np.random.rand()*2-1)

env = LunarLander()
env.reset()
env.rocket.x = xstart
exit_program = False
while not exit_program:
    env.render()
    (x, y, xspeed, yspeed), reward, done = env.step((boost, left, right)) 

    # Process game events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_program = True
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_ESCAPE, pygame.K_q]:
                exit_program = True
            if event.key == pygame.K_UP:
                boost = True
            if event.key == pygame.K_DOWN:
                boost = False
            if event.key == pygame.K_RIGHT:
                left = False if right else True
                right = False
            if event.key == pygame.K_LEFT:
                right = False if left else True
                left = False
            if event.key == pygame.K_r:
                boost = False        
                left = False
                right = False
                env.reset()

    # INSERT YOUR CODE HERE
    if yspeed <= 10:
        boost = False
    elif yspeed > 20 and y < 200:
        boost = True    

    if x > 0:
        right = True
    elif x < 0:
        left = True

    if abs(x) < 10:
        if xspeed > 10:
            left = False
        elif xspeed < -10:
            right = False
    else:
        if xspeed > 30:
            left = False
        elif xspeed < -30:
            right = False

    # END OF YOUR CODE

env.close()

sim = LunarLander()
sim.reset()
sim.rocket.x = xstart
exit_program = False
while not exit_program:
    sim.render()
    (x, y, xspeed, yspeed), reward, done = sim.step((boost, left, right)) 

    # Process game events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_program = True
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_ESCAPE, pygame.K_q]:
                exit_program = True
            if event.key == pygame.K_UP:
                boost = True
            if event.key == pygame.K_DOWN:
                boost = False
            if event.key == pygame.K_RIGHT:
                left = False if right else True
                right = False
            if event.key == pygame.K_LEFT:
                right = False if left else True
                left = False
            if event.key == pygame.K_r:
                boost = False        
                left = False
                right = False
                sim.reset()

    # INSERT YOUR CODE HERE
    if yspeed <= 10:
        boost = False
    elif yspeed > 20 and y < 200:
        boost = True    

    if x > 0:
        right = True
    elif x < 0:
        left = True

    if abs(x) < 150:
        if xspeed > 10:
            left = False
        elif xspeed < -10:
            right = False
    else:
        if xspeed > 30:
            left = False
        elif xspeed < -30:
            right = False

    # END OF YOUR CODE

sim.close()