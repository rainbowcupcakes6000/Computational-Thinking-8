###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("winter")

q1 = codesters.Square(100, 100, 200, 'blue')
q2 = codesters.Square(-100, 100, 200, 'yellow')
q3 = codesters.Square(-100, -100, 200, 'red')
q4 = codesters.Square(100, -100, 200, 'green')

s1 = codesters.Sprite("travis", 96, 102)
s1.set_size(1)
s2 = codesters.Sprite("drake", -100, -100)
s2.set_size(0.9)
s3 = codesters.Sprite("jfkfc", 100, -100)
s3.set_size(0.9)
s4 = codesters.Sprite("cardinal", -100, 100)
s4.set_size(0.5)

message1 = codesters.Text("Jack Howard Gregersen",0,220,"red")
message2 = codesters.Text("I'm proud to be jack",0,-220,"black")