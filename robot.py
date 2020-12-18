import seamonsters as sea 
import wpilib
import rev
import math

class PracticeBot(sea.SimulationRobot):

    def robotInit(self):
        leftSpark = sea.createSpark(1, rev.MotorType.kBrushless)
        rightSpark = sea.createSpark(2, rev.MotorType.kBrushless)

        for spark in [leftSpark, rightSpark]:
            spark.restoreFactoryDefaults()
            spark.setIdleMode(rev.IdleMode.kBrake)

        leftWheel = sea.AngledWheel(leftSpark, -1, 0, math.pi/2, 1, 16)
        rightWheel = sea.AngledWheel(rightSpark, 1, 0, math.pi/2, 1, 16)

        self.drivetrain = sea.SuperHolonomicDrive()
        self.drivetrain.addWheel(leftWheel)
        self.drivetrain.addWheel(rightWheel)

        for wheel in self.drivetrain.wheels:
            wheel.driveMode = rev.ControlType.kVelocity

        sea.setSimulatedDrivetrain(self.drivetrain)

    @staticmethod
    def degreesPerSecond(turn):
        """Takes a number representing the number of revolutions per second
        you want the robot to turn, then returns that number converted to
        a number for use in the PracticeBot.drive(...) method."""

        return math.radians(turn) * (3.0/5.0)

    def autonomous(self):
        speed = 5
        # turnModifier is -1 if the robot is turning left, 1 if the robot is turning right
        turnModifier = 1
        for _ in range(5):
            # go forward long
            self.drivetrain.drive(speed, math.pi/2, 0)
            yield from sea.wait(100 / (speed / 4))

            # turn
            self.drivetrain.drive(0, math.pi/2, PracticeBot.degreesPerSecond(180 * turnModifier))
            yield from sea.wait(25)

            # go forward short
            self.drivetrain.drive(speed, math.pi/2, 0)
            yield from sea.wait(55 / (speed / 4))

            # turn
            self.drivetrain.drive(0, math.pi/2, PracticeBot.degreesPerSecond(180 * turnModifier))
            yield from sea.wait(25)

            # switch turn direction
            turnModifier *= -1

        # go forward long
        self.drivetrain.drive(speed, math.pi/2, 0)
        yield from sea.wait(100  / (speed / 4))

        # stop moving
        self.drivetrain.drive(0, math.pi/2, 0)
        while 1:
            yield

if __name__ == "__main__":
    wpilib.run(PracticeBot)