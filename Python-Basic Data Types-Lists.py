if __name__ == '__main__':
    N = int(input());
    list=[];
    for i in range (0,N):
        inp=input();
        ip=inp.split(" ");
        if (ip[0]=='insert'):
            list.insert(int(ip[1]),int(ip[2]));
        elif(ip[0]=='print'):
            print(list);
        elif(ip[0]=='remove'):
            list.remove(int(ip[1]));
        elif(ip[0]=='sort'):
            list.sort();
        elif(ip[0]=='pop'):
            list.pop();
        elif(ip[0]=='reverse'):
            list.reverse();
        elif(ip[0]=='append'):
            list.append(int(ip[1]));
