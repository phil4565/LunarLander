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
import pandas as pd
import xlsxwriter

itterations = 96
intervals = [10, 150]
fuelData = [[],[]]

for i in range(itterations):
    print(f"Running iteration {i}")
    xstart = 0 + 300*(np.random.rand()*2-1)
    for idInterval, interval in enumerate(intervals):
        env = LunarLander()
        env.reset()
        env.rocket.reset()
        env.clock.tick(120)
        env.rocket.x = xstart
        exit_program = False
        while not exit_program:
            #env.render()
            (x, y, xspeed, yspeed), reward, done = env.step((boost, left, right)) 
            left, right = False, False
                  
            if yspeed <= 10:
                boost = False
            elif yspeed > 20 and y < 200:
                boost = True    

            if x > 0:
                right = True
            elif x < 0:
                left = True

            if abs(x) < interval:
                if xspeed > 10:
                    left = False
                elif xspeed < -10:
                    right = False
            else:
                if xspeed > 30:
                    left = False
                elif xspeed < -30:
                    right = False

            if env.game_over:
                if env.won:
                    fuelData[idInterval].append(env.rocket.fuel)
                else:
                    fuelData[idInterval].append(0)
                exit_program = True
        env.close()

workbook = xlsxwriter.Workbook("fuelData.xlsx")
for dataset in fuelData:
    worksheet = workbook.add_worksheet()
    for entryIndex, entry in enumerate(dataset):
        worksheet.write(entryIndex, 0, entry)
workbook.close()