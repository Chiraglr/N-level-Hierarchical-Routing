import math

def dijkstras(a,s,d):
    n=len(a)
    dv=[]
    pv=[]
    for i in range(n):
        dv.append([999,i])
        pv.append(-1)
    dv[s].pop(0)
    dv[s].insert(0,0)
    dv.sort()
    vt=[]
    for i in range(n):
        v=dv.pop(0)
        vt.append(v[1])
        n-=1
        x=[]
        for i in range(len(dv)):
            x.append(dv[i][1])
        for j in x:
                if a[v[1]][j]!=999:
                    for k in range(len(dv)):
                        if dv[k][1]==j:
                            if (v[0]+a[v[1]][j])<dv[k][0]:
                                dv[k][0]=v[0]+a[v[1]][j]
                                pv[j]=v[1]
                                dv.sort()
    
    traverse=[]
    while(d!=s):
        traverse.insert(0,d)
        d=pv[d]
    traverse.insert(0,d)
    return traverse




def forward(src,dest,lvl,de,l,pos,ntwcost,r,nodes,bgr,prefix,origntwcost,cos):
    if lvl>(l-pos):
        for i in range(len(nodes[lvl-1])):
            a=0
            for k in range(len(nodes[lvl-1][i])):
                if nodes[lvl-1][i][k]==src:
                    a=k
            if src in nodes[lvl-1][i]:
                if dest in nodes[lvl-1][i]:
                    for j in range(len(nodes[lvl-1][i])):
                        if dest==nodes[lvl-1][i][j]:
                            trav=dijkstras(origntwcost[lvl-1][i],a,j)
                            for k in range(1,len(trav)):
                                print "->",
                                print nodes[lvl-1][i][trav[k]],
                            cos[0]+=ntwcost[lvl-1][i][a][j]
                            return dest,r[lvl-1][i][a][j]
                else:
                    poss=[]
                    for k in range(len(nodes[lvl-1][i])):
                        if prefix[pos][nodes[lvl-1][i][k]]==de[pos]:
                            poss.append(k)
                    
                    mi=0
                    for k in range(len(poss)):
                        if ntwcost[lvl-1][i][a][poss[mi]]>ntwcost[lvl-1][i][a][poss[k]]:
                            mi=k
                    trav=dijkstras(origntwcost[lvl-1][i],a,mi)        
                    for k in range(1,len(trav)):
                        print "->",
                        print nodes[lvl-1][i][trav[k]],
                    cos[0]+=ntwcost[lvl-1][i][a][poss[mi]]
                    return nodes[lvl-1][i][poss[mi]],r[lvl-1][i][a][poss[mi]]
                            
    else:
        for i in range(len(nodes[lvl])):
            if src in nodes[lvl][i]:
                    poss=[]
                    for j in range(len(nodes[lvl][i])):
                        if prefix[pos][nodes[lvl][i][j]]==de[pos]:
                            poss.append(j)
                    a=0
                    for k in range(len(nodes[lvl][i])):
                        if nodes[lvl][i][k]==src:
                            a=k
                    mi=0
                    for j in range(len(poss)):
                        if ntwcost[lvl][i][a][poss[mi]]>ntwcost[lvl][i][a][poss[j]]:
                            mi=j
                    trav=dijkstras(origntwcost[lvl][i],a,poss[mi])
                    for j in range(1,len(trav)):
                        print "->",
                        print nodes[lvl][i][trav[j]],
                    cos[0]+=ntwcost[lvl][i][a][poss[mi]]
                    return nodes[lvl][i][poss[mi]],r[lvl][i][a][poss[mi]]


def nodetobgr(src,lvl,ntwcost,r,nodes,bgr,origntwcost,cos):#lvl should be less than l never l... It cannot be the highest border #router
    for i in range(len(nodes[lvl])):
        for j in range(len(nodes[lvl][i])):
            if src==nodes[lvl][i][j]:
                p=[]
                for k in range(len(bgr[lvl][i])):
                    p.append(bgr[lvl][i][k])
                p1=[]
                for k in range(len(nodes[lvl][i])):
                    if nodes[lvl][i][k] in p:
                        p1.append(k)
                mi=0
                for k in range(len(p1)):
                    if ntwcost[lvl][i][j][p1[mi]]>ntwcost[lvl][i][j][p1[k]]:
                        mi=k
                trav=dijkstras(origntwcost[lvl][i],j,p1[mi])
                for k in range(1,len(trav)):
                    print "->",
                    print nodes[lvl][i][trav[k]],        
                cos[0]+=ntwcost[lvl][i][j][p1[mi]]      
                return p[mi], r[lvl][i][j][p1[mi]]             


def dvector(c,m):
    r=[]
    for i in range(m):
        r.append([])
        for j in range(m):
            r[i].append(j)
            
    for k in range(m):
        for i in range(m):
            for j in range(m):
                a=c[i][j]
                b=c[i][k]+c[k][j]
                c[i][j]=mini(a,b,i,j,k,r)
    return r
    
def mini(a,b,i,j,k,r):
    if b<a:
        r[i][j]=r[i][k]
        return b
    return a    





def pref(prefix,gr,i,l):
    prefix.append([])
    li=gr[l-i]
    k=s=0
    for j in range(len(li)-1):
        k=gr[l-i][j]
        s=gr[l-i][j+1]
        count=0
        for n in range(k,s):
            count+=1
            a=gr[l-i-1][n]
            u=gr[l-i-1][n+1]
            for m in range(l-i-1):
                a=gr[l-i-2-m][a]
                u=gr[l-i-2-m][u]
            for m in range(u-a):
                prefix[i].append(count)
    return




def strtoprefix(s,gr,ntw,l):
    s=s.replace("."," ")
    num=map(int,s.split())
    tk=[]
    for i in range(len(gr)):
        tk.append([])
        tk[i].insert(0,0)
        for j in range(1,len(gr[i])+1):
            tk[i].append(gr[i][j-1])
            tk[i][j]+=tk[i][j-1]    
    
    su=st=0
    for i in range(l):
        st=tk[l-1-i][su+num[i]-1]    
        su=st 
    su+=(num[l]-1)
    return su,num






fo=open("net3.txt","r")
n=int(fo.readline()) #number of nodes in network
l=int(fo.readline()) #number of levels

fo.readline()

cost=[]
for i in range(n):
    cost.append([])
    for j in range(n):
        if i==j:
            cost[i].append(0)
            continue
        cost[i].append(999)
        
w=int(fo.readline())
for i in range(w):
    row=int(fo.readline())
    col=int(fo.readline())
    cost[row][col]=int(fo.readline())
    cost[col][row]=cost[row][col]
recheck=[]
for i in range(n):
    recheck.append([])
    for j in range(n):
        recheck[i].append(cost[i][j])
waste=dvector(recheck,n)

fo.readline()
ntw=[]
#how many networks at level i
for i in range(l):
    ntw.append(int(fo.readline()))
ntw.append(1)

print "ntw is: "
print ntw
fo.readline()

nodes=[]
for i in range(l+1):
    nodes.append([])
    for j in range(ntw[i]):
        nodes[i].append([])
        w=int(fo.readline())        #number of level i and i-1 routers in level i network j
        for k in range(w):
            nodes[i][j].append(int(fo.readline()))        #level i and i-1 router numbers in level i network j

print "\nnodes is: "
print nodes
fo.readline()
bgr=[]
#border gateway router numbers in each network at each level
for i in range(l):
    bgr.append([])
    for j in range(ntw[i]):
        a=int(fo.readline())    #number of level i gateway routers in network j in level i
        bgr[i].append([])
        for k in range(a):
            bgr[i][j].append(int(fo.readline()))     #level i gateway router numbers:)

print "\nbgr is: "
print bgr

fo.readline()            
origntwcost=[]
ntwcost=[]
#cost matrix of every network from every level:)
for i in range(l+1):
    ntwcost.append([])
    origntwcost.append([])
    for j in range(ntw[i]):
        ntwcost[i].append([])
        origntwcost[i].append([])
        for k in range(len(nodes[i][j])):
            ntwcost[i][j].append([])
            origntwcost[i][j].append([])
            for h in range(len(nodes[i][j])):
                ntwcost[i][j][k].append(cost[nodes[i][j][k]][nodes[i][j][h]])
                origntwcost[i][j][k].append(ntwcost[i][j][k][h])
#the number of routers in each level i network:)
gr=[]
for i in range(l):
    gr.append([])
    for j in range(ntw[i]):
        gr[i].append(int(fo.readline()))

print "\ngr is: "
print gr        
fo.readline()

rp=[]
for i in range(len(gr)):
    rp.append([])
    for j in gr[i]:
        rp[i].append(j)

gr.append([len(gr[l-1])])

for i in gr:
    i.insert(0,0)
    k=i[0]
    for j in range(1,len(i)):
        i[j]+=k
        k=i[j]

#Here we create an array that the nodes can use to check if the node is in it's network:)
#this is crucial for routing as this array informs the router the direction in which to pass the packet:)
prefix=[]
for i in range(l):
    pref(prefix,gr,i,l)

prefix.append([])
for i in range(len(gr[0])-1):
    u=gr[0][i]
    k=gr[0][i+1]
    for j in range(k-u):
        prefix[l].append(j+1)
print

#here we create an array to be used to give the next hop information in the routing table:)
r=[]
for i in range(l+1):
    r.append([])
    for j in range(ntw[i]):
        r[i].append(dvector(ntwcost[i][j],len(ntwcost[i][j])))


p=True
print "Enter\n1.Routing packets in network\n2.displaying routing table of a node\n3.Memory efficiency of a node\n4.Exit"
while p:
    print "Enter choice "
    choice=input()
    if choice==1:
        str1=raw_input("Enter source router: ")
        str2=raw_input("Enter destination router: ")

        src,sr=strtoprefix(str1,rp,ntw,l)
        dest,de=strtoprefix(str2,rp,ntw,l)
        print src
        print dest
        print"Traversal is: \n\n"
        print src,
        osrc=src
        cos=[0]
        while sr!=de:
            pos=0
            for i in range(l+1):
                if sr[i]!=de[i]:
                    break
                pos+=1
            if pos==l+1:
                break
    
            lvl=[]
            for i in range(l):
                for j in range(ntw[i]):
                    if src in bgr[i][j]:
                        lvl.append(i+1)
            if len(lvl)==0:
                lvl.append(0)
    
            k=0
            for i in range(len(lvl)):
                if lvl[i]<=(l-pos):
                    k=i            
    
            if lvl[k]<(l-pos):
                src,q=nodetobgr(src,lvl[k],ntwcost,r,nodes,bgr,origntwcost,cos)
            else:
                src,q=forward(src,dest,lvl[k],de,l,pos,ntwcost,r,nodes,bgr,prefix,origntwcost,cos)
            for i in range(l+1):
                sr[i]=prefix[i][src]
        print "\nrouting efficiency is: %d"%((recheck[osrc][dest]/float(cos[0]))*100)
        print              
    elif choice==2:
        str1=raw_input("Enter router address ")
        src,sr=strtoprefix(str1,rp,ntw,l)
        seen=[]
        print "dest\tnext hop\tdist"
        for i in range(l+1):
            for j in range(ntw[i]):
                for k in range(len(nodes[i][j])):
                    if nodes[i][j][k]==src:
                        for u in range(len(nodes[i][j])):
                            if nodes[i][j][u]!=src:
                                if ntwcost[i][j][k][u]!=999 and nodes[i][j][u] not in seen:
                                    seen.append(nodes[i][j][u])
                                    print "%d\t%d\t\t%d"%(nodes[i][j][u],nodes[i][j][r[i][j][k][u]],ntwcost[i][j][k][u])
        print 
    elif choice==3:
        count=0
        str1=raw_input("Enter router address ")
        src,sr=strtoprefix(str1,rp,ntw,l)
        seen=[]
        for i in range(l+1):
            for j in range(ntw[i]):
                if src in nodes[i][j]:
                    for k in range(len(nodes[i][j])):
                        if nodes[i][j][k]==src:
                            for u in range(len(nodes[i][j])):
                                if ntwcost[i][j][k][u]!=999 and u!=k and nodes[i][j][u] not in seen:
                                    seen.append(nodes[i][j][u])
                                    count+=1
        print "memory efficiency is: ",
        print ((n-count)/float(n))*100
        print
    else:
        p=False






















