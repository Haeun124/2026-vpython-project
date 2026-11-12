import random
c=cylinder(size=vec(44,2,2),pos=vec(-21.3,-37,7.5),color=color.red,opacity=0.5)

box(size=vec(50,80,15),pos = vec(0,0,0),color=vec(255,243,242))           
cylinder (axis= vec (0,0,1),size=vec(16,25,25),pos=vec(0,-19,-6.7),color=color.red)
cylinder (axis= vec (0,0,1),size=vec(16,16,16),pos=vec(0,-19,-6.6),color=color.green)
box(size=vec(52,82,16),pos=vec(0,0,0),color=vec(192,224,252))




b=box(size=vec(44,40,1),pos=vec(0,17,8.5),texture = "https://i.postimg.cc/QCCDtvNh/IMG-0282.jpg")
a=["https://i.postimg.cc/d3QHbTBH/IMG-0283.jpg","https://i.postimg.cc/9QxL9McB/IMG-0287.jpg", "https://i.postimg.cc/d3QHbTBH/IMG-0283.jpg" ]

while True :
    rate(100)
    k = keysdown()
    if ' ' in k :
        for i in range(3) : 
            b.texture=a[i]
        c.color =vec(random.random(),random.random(),random.random())



triangleshapew = [[1.5,0], [0,2.3],[-1.5,0], [1.5,0]]
linepath = [vec(0,-9.7,-4), vec(0,-9.7,10)]
wedge = extrusion(shape= triangleshapew, path= linepath)

triangleshaped = [[-2.3,0], [0,1.5],[0,-1.5], [-2.3,0]]
linepath = [vec(9,-19,-4), vec(9,-19,10)]
wedge = extrusion(shape= triangleshaped, path= linepath)

triangleshapea = [[2.3,0], [0,1.5],[0,-1.5], [2.3,0]]
linepath = [vec(-9,-19,-4), vec(-9,-19,10)]
wedge = extrusion(shape= triangleshapea, path= linepath)

triangleshapex = [[1.5,0], [0,-2.3],[-1.5,0], [1.5,0]]
linepath = [vec(0,-28,-4), vec(0,-28,10)]
wedge = extrusion(shape= triangleshapex, path= linepath)
