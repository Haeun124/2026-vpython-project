for i in range(50) : 
    for j in range(80) : 
        for k in range(15) : 
            rate(150000)
            box(pos = vec(i,j,k),color=color.red)
            
            
            cylinder (axis= vec (0,0,1),size=vec(16,25,25),pos=vec(25,18,0))
            cylinder (axis= vec (0,0,1),size=vec(16,16,16),pos=vec(25,18,1),color=color.green)
            box(size=vec(44,40,3),pos=vec(25,55,14.5))
