# rayleigh damping 
bi = 0.02
bj = 0.02
wi = 2*math.pi*0.2 #rad/s
wj = 2*math.pi*20 #rad/s
a0 = 2*wi*wj*(bi*wj-bj*wi)/(wj**2-wi**2)
a1 = 2*(bj*wj-bi*wi)/(wj**2-wi**2)
ops.rayleigh(a0,0,0,a1)