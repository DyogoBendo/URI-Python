from sys import stdin, stdout

if __name__ == "__main__":
    n = int(input())

    qtd_gc_c = 0
    qtd_gc_e = 0
    gc_c = 0
    gc_e = 0
    for i in range(n):
        ida, volta = stdin.readline().split()        
        if ida == 'chuva':
            if qtd_gc_c == 0:
                gc_c += 1
            else:
                qtd_gc_c -= 1
            qtd_gc_e += 1
        if volta == 'chuva':
            if qtd_gc_e == 0:
                gc_e += 1
            else:
                qtd_gc_e -= 1
            qtd_gc_c += 1
    print(gc_c, gc_e)            
        


        

