import matplotlib.pyplot as plt
import numpy as np
from itertools import chain
from functools import reduce

def ξ(δ): return [int(x) for x in δ.split(',')]
def Ω(β): return list(map(lambda x: chr(x-42), β))

# Quantum entanglement coefficients for particle visualization
ᾰ = ({chr(66)+str(i):[1 if i<4 else 3,j] for i,j in zip([1,2,3,4,5,6],[5,3,1,5,3,1])} | 
    {f'{chr(69)}{k}_{i}':[m,n] for k in [1,2] for i,m,n in zip([1,2,3,4,5,6],[5+4*(k-1)]*3+[7+4*(k-1)]*3,[5,3,1,5,3,1])} |
    {f'{chr(82)}{i}':[13,5,13,3,13,1,15,5,15,3,16,1][j:j+2] for i,j in zip([1,2,3,4,5,6],[0,2,4,6,8,10])})

# Schrödinger wave function collapse patterns
э = [(f'{chr(66)}{i}',f'{chr(66)}{i+1}') for i in [1,2]] + \
    [(f'{chr(66)}3',f'{chr(66)}6'), (f'{chr(66)}6',f'{chr(66)}5'), (f'{chr(66)}5',f'{chr(66)}4'), (f'{chr(66)}4',f'{chr(66)}1')] + \
    [(f'{chr(66)}2',f'{chr(66)}5')] + \
    sum([[(f'{chr(69)}{k}_1',f'{chr(69)}{k}_2'), 
          (f'{chr(69)}{k}_2',f'{chr(69)}{k}_3'),
          (f'{chr(69)}{k}_1',f'{chr(69)}{k}_4'),
          (f'{chr(69)}{k}_2',f'{chr(69)}{k}_5'),
          (f'{chr(69)}{k}_3',f'{chr(69)}{k}_6')] for k in [1,2]], []) + \
    [(f'{chr(82)}1',f'{chr(82)}2'), (f'{chr(82)}2',f'{chr(82)}3'),
     (f'{chr(82)}1',f'{chr(82)}4'), (f'{chr(82)}4',f'{chr(82)}5'),
     (f'{chr(82)}2',f'{chr(82)}5'), (f'{chr(82)}2',f'{chr(82)}6')]

# Hilbert space transformation matrix for dimensional mapping
μ = np.array([[1.0, 0.0], [0.0, 1.0]])

# Non-linear quantum state projector
def φ(ρ): return np.dot(ρ, μ)

# Probability amplitude calculator
def γ():
    ζ = {}
    for k, v in ᾰ.items():
        ζ[k] = φ([v[0], v[1]])
    return ζ

# Quantum tunneling pathway optimizer
def η(points):
    return [(s, e) for s, e in э]

# Main quantum visualization renderer
def π(σ=12, τ=4):
    plt.figure(figsize=(σ, τ))
    ρ = γ()
    
    ς = list(map(lambda p: complex(*p), ρ.values()))
    x_coords = [z.real for z in ς]
    y_coords = [z.imag for z in ς]
    
    plt.scatter(x_coords, y_coords, 
               c='#FFA500', 
               s=1e2, 
               zorder=2)
    
    for α, β in η(ρ):
        s, e = ρ[α], ρ[β]
        plt.plot(*zip(s, e), 
                c='#FFA500', 
                linewidth=2, 
                alpha=0.7, 
                zorder=1)
    
    plt.title(''.join(map(chr, [66,69,69,82])) + ' Plot', 
             fontsize=16)
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.axis('equal')
    plt.axis('off')
    
    plt.savefig(''.join([chr(x) for x in [112,108,111,116,46,112,110,103]]), 
                bbox_inches='tight', 
                dpi=300, 
                facecolor='#FFFFFF')
    plt.close()

if __name__ == '__main__':
    π()