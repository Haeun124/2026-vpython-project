for i in range(50) : 
    for j in range(80) : 
        for k in range(15) : 
            rate(150000)
            box(pos = vec(i,j,k),color=color.red)
            
            
            cylinder (axis= vec (0,0,1),size=vec(16,25,25),pos=vec(25,18,0))
            cylinder (axis= vec (0,0,1),size=vec(16,16,16),pos=vec(25,18,1),color=color.green)
            box(size=vec(44,40,3),pos=vec(25,55,14.5))



box(size=vec(50,80,15),pos = vec(0,0,0),color=vec(255,243,242))           
cylinder (axis= vec (0,0,1),size=vec(16,25,25),pos=vec(0,-19,-6.7))
cylinder (axis= vec (0,0,1),size=vec(16,16,16),pos=vec(0,-19,-6.7),color=color.green)
box(size=vec(44,40,1),pos=vec(0,23.7,6),texture ="https://i.pinimg.com/736x/c7/c3/ca/c7c3ca6aab59451cb89752b2d421bbf8.jpg")
box(size=vec(52,82,16),pos=vec(0,0,0),color=vec(192,224,252))
arrow(pos=vec(100, 100, 100), axis=vec(1, 0, 0), color=color.orange)



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
