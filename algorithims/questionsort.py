from objects import question

def sort(q):
    if len(q) > 1:
        mid = len(q)//2
        l = q[:mid]
        r = q[mid:]
        sort(l)
        sort(r)
        i = 0
        j = 0
        k = 0
        while i < len(l) and j < len(r):
            if l[i].qid < r[k].qid:
                q[k] = l[i]
                i += 1
            else:
                q[k] = r[j]
                j += 1
            k += 1
        while i < len(l):
            q[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            q[k] = r[j]
            j += 1
            k += 1