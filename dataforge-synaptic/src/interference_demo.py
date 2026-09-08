import numpy as np
import matplotlib.pyplot as plt

def dense_memory(d=16, N=30, seed=7):
    rng = np.random.default_rng(seed)
    K = rng.normal(size=(N, d)); K /= np.linalg.norm(K, axis=1, keepdims=True)
    V = rng.normal(size=(N, d)); V /= np.linalg.norm(V, axis=1, keepdims=True)
    W = K.T @ V
    sims = []
    for i in range(N):
        pred = W.T @ K[i]; pred /= np.linalg.norm(pred) + 1e-12
        sims.append(float(pred @ V[i]))
    return float(np.mean(sims))

def sweep(max_N=30, d=16, repeats=100):
    Ns=np.arange(1,max_N+1); vals=[]
    for n in Ns:
        vals.append(np.mean([dense_memory(d=d,N=int(n),seed=1000+r) for r in range(repeats)]))
    return Ns,np.array(vals)

if __name__ == '__main__':
    Ns,y=sweep()
    plt.figure(figsize=(8.5,4.8)); plt.plot(Ns,y,marker='o',linewidth=2,markersize=3)
    plt.axvline(16,linestyle='--',linewidth=1.4)
    plt.xlabel('Stored associations (N)'); plt.ylabel('Mean cosine similarity')
    plt.title('Toy dense Hebbian memory: interference with increasing load')
    plt.grid(True,alpha=.25); plt.tight_layout(); plt.savefig('interference_toy.png',dpi=180)
    print('Saved interference_toy.png')
