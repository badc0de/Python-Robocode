#! /usr/bin/python
#-*- coding: utf-8 -*-

from robot import Robot # Import a base Robot


class BusyBee(Robot): # Create a Robot
    
    def init(self):
        """
        Function necessary for the game
        Initialize the robot
        """        
        
        # Set the bot color in RGB
        self.setColor(255, 234, 0)
        self.setGunColor(0, 0, 0)
        self.setRadarColor(255, 234, 0)
        self.setBulletsColor(250, 234, 0)
        
        # Get the map size
        size = self.getMapSize()

        # Show the radar
        self.radarVisible(True) 
        
    
    def run(self):
        """
        Function necessary for the game
        This is the main loop to run the robot
        """
        
        self.move(90) # Negative values go back
        self.turn(360) # Negative values turn counter-clockwise
        self.stop() # Stops the robot
        self.fire(3) # Fire (power between 1 and 10)
        
        self.move(100)
        self.turn(50)
        self.stop()
        bulletId = self.fire(2) #to let you you manage if the bullet hit or fail
        
        self.move(180)
        self.turn(180)
        self.gunTurn(90) #to turn the gun (negative values turn counter-clockwise)
        self.stop()
        self.fire(1) # To Fire (power between 1 and 10)

        self.radarTurn(180) #to turn the radar (negative values turn counter-clockwise)
        self.stop()
        
    def sensors(self):
        """
        Function necessary for the game
        Tick each frame to receive data about the game
        """
        pos = self.getPosition() # Return the center of the bot 
        x = pos.x() # Get the x coordinate 
        y = pos.y() # Get the y coordinate 
        angle = self.getGunHeading() # Returns the direction that the robot's gun is facing
        angle = self.getHeading() # Returns the direction that the robot is facing
        angle = self.getRadarHeading() # Returns the direction that the robot's radar is facing
        list = self.getEnemiesLeft() # Returns a list of the enemies alive in the battle
        
        for robot in list:
            id = robot["id"]
            name = robot["name"]
            # Each element of the list is a dictionnary with the bot's id and the bot's name
        
    def onHitByRobot(self, robotId, robotName):
        """
        What happens when the robot is crashed by another robot 
        """
        self.rPrint("Collision with another robot detected")

    def onHitWall(self):
        """
        What happens when the robot collides with a wall
        """
        self.reset() # Resets the run function to the beginning (auomatically called on hitWall, and robotHit event) 
        self.pause(100)
        self.move(-100)
        self.rPrint("Collision with a wall detected")
        self.setRadarField("large") # Change the radar field form
    
    def onRobotHit(self, robotId, robotName):
        """
        What happens when the robot crashes into another robot
        """
        self.rPrint('Collision with:' + str(robotName))
       
    def onHitByBullet(self, bulletBotId, bulletBotName, bulletPower):
        """
        Function necessary for the game
        What happens when the robot gets hit by a bullet
        """
        self.reset() # Resets the run fonction to the begining 
        self.rPrint ("Hit by " + str(bulletBotName) + "with power: " +str( bulletPower))
        
    def onBulletHit(self, botId, bulletId):
        """
        Function necessary for the game
        What happens when the robot hits another robot
        """
        self.rPrint ("hit by " + str(bulletBotName) + "with power:" +str( bulletPower))

    def onBulletMiss(self, bulletId):
        """
        Function necessary for the game 
        What happens when the robot misses
        """
        self.rPrint ("The bullet No."+ str(bulletId) + " missed")
        self.pause(10) #wait 10 frames
        
    def onRobotDeath(self):
        """
        Function necessary for the game
        What happens when the robot is destroyed 
        """
        self.rPrint ("I'm dead")
    
    def onTargetSpotted(self, botId, botName, botPos):
        """
        Function necessary for the game
        What happens when the robot see another one
        """
        self.fire(5)
        self.rPrint("Robot "+ str(botId) + "detected with coordinates:") 
        self.rPrint("\tx:" + str(botPos.x()) + "\n\ty:" + str(botPos.y()))
    
