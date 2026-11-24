import random
c=cylinder(size=vec(44,2,2),pos=vec(-21.3,-37,7.5),color=color.red,opacity=0.5)
b=box(size=vec(44,40,1),pos=vec(0,17,8.5),texture = "https://i.postimg.cc/rpS02r1h/IMG-0302.jpg")
a=["https://i.postimg.cc/PJN5JpD5/IMG-0282.jpg","https://i.postimg.cc/d3QHbTBH/IMG-0283.jpg","https://i.postimg.cc/1RjYjXqk/IMG-0287.jpg", "https://i.postimg.cc/3RnJTmT7/IMG-0288.jpg","https://i.postimg.cc/s2fg0wkK/IMG-0289.jpg","https://i.postimg.cc/T1KyNCDw/IMG-0290.jpg","https://i.postimg.cc/8CT7g16X/IMG-0291.jpg","https://i.postimg.cc/cHzNDDKd/IMG-0301.jpg","https://i.postimg.cc/BvtXnmmw/IMG-0293.jpg"]
    
cylinder (axis= vec (0,0,1),size=vec(16,25,25),pos=vec(0,-19,-6.7),color=vec(255/255,220/255,234/255))
cylinder (axis= vec (0,0,1),size=vec(16,16,16),pos=vec(0,-19,-6))
box(size=vec(52,82,16),pos=vec(0,0,0),color=vec(201/255,236/255,255/255))

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
            
i = 0
while True :
    rate(5)
    k = keysdown()
    if ' ' in k :  
        b.texture=a[i%9]
        c.color =vec(random.random(),random.random(),random.random())
        i = i + 1

