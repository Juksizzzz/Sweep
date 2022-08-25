#python

#Code creates robot path with going around the obstacles and checking if robot fits between two obstacles

job = Swarm.StartJob('Clean area 1')
agv = Swarm.GetAgvById('rudolph')

speed = 20
curveSpeed = 20
hasRelativeCoordinates = False
direction = 'front'
lineSize = 2
angle = 90
robotWidth = 1
i = 0
safety = 0.05
newStart = 0
goAroundCurve = 0.3
skipLoop = 0
curveRadius = 0.5

def createLine(newStart, target, angle, lineSize, direction, speed=speed):
    finish = [newStart[0]+(lineSize*math.cos(math.radians(angle))), newStart[1]+(lineSize* math.sin(math.radians(angle)))]
    line = agv.CreatePathSegment(newStart , None , finish, None, speed, direction, hasRelativeCoordinates)
    target.append(line)
    return finish

def bezierByAngle(start, target, angle, angle2, lenght, direction, speed=curveSpeed):
    finish1 = [start[0]+(lenght*math.cos(math.radians(angle))),start[1]+(lenght*math.sin(math.radians(angle)))]
    finish2 = [finish1[0]+(lenght*math.cos(math.radians(angle+angle2))),finish1[1]+(lenght*math.sin(math.radians(angle+angle2)))]
    line = agv.CreatePathSegment(start, finish1 , finish2 , None, speed, direction, hasRelativeCoordinates)
    target.append(line)
    return finish2


target = []

tasks = []

commands = ["createLine([32.5, 7.570260820665796],target,90,2.58,'front',20)", "createLine([32.5, 10.150260820665794],target,90,-2.08,'back',20)", "bezierByAngle([32.5, 8.070260820665796],target,-90,90,0.5,'back',10)", "createLine([33.0, 7.570260820665796],target,180,0.5,'front',20)", "createLine([32.5, 7.570260820665796],target,180,0.52,'front',20)", "bezierByAngle([31.98, 7.570260820665796],target,180,-90,0.5,'front',10)", "createLine([31.48, 8.070260820665796],target,90,2.5,'front',20)", "createLine([31.48, 10.570260820665796],target,90,-2.5,'back',20)", "bezierByAngle([31.48, 8.070260820665796],target,-90,90,0.5,'back',10)", "createLine([31.98, 7.570260820665796],target,180,0.5,'front',20)", "createLine([31.48, 7.570260820665796],target,180,0.52,'front',20)", "bezierByAngle([30.96, 7.570260820665796],target,180,-90,0.5,'front',10)", "createLine([30.46, 8.070260820665796],target,90,2.5,'front',20)", "createLine([30.46, 10.570260820665796],target,90,-2.5,'back',20)", "bezierByAngle([30.46, 8.070260820665796],target,-90,90,0.5,'back',10)", "createLine([30.96, 7.570260820665796],target,180,0.5,'front',20)", "createLine([30.46, 7.570260820665796],target,180,0.52,'front',20)", "bezierByAngle([29.94, 7.570260820665796],target,180,-90,0.5,'front',10)", "createLine([29.44, 8.070260820665796],target,90,2.5,'front',20)", "createLine([29.44, 10.570260820665796],target,90,-2.5,'back',20)", "bezierByAngle([29.44, 8.070260820665796],target,-90,90,0.5,'back',10)", "createLine([29.94, 7.570260820665796],target,180,0.5,'front',20)", "createLine([29.44, 7.570260820665796],target,180,0.44,'front',20)", "bezierByAngle([29.0, 7.570260820665796],target,180,-90,0.5,'front',10)", "createLine([28.5, 8.070260820665796],target,90,2.5,'front',20)", "bezierByAngle([28.5, 10.570260820665796],target,90,-90,0.5,'front',10)", "createLine([29.0, 11.070260820665796],target,0,2.38,'front',20)", "bezierByAngle([31.38, 11.070260820665796],target,0,-90,0.5,'front',10)"]

for i in range(len(commands)):
    finish = eval(commands[i])


task = agv.CreateBezierPathExecuteTask(target)
tasks.append(task)


agv.StartMission(tasks).Wait()


job.Wait(1)