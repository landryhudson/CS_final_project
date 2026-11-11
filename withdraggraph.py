


Fdrag=-0.5*C*d*A*mag(vf2)**2*hat(vf2)
    p2=p2+(gravity+Fdrag)*delta_t
    baseball2.pos = baseball2.pos + p2/m*delta_t 
