n = int(input())
s = set(map(int, input().split()))
c = int(input())

def set_update(s,c):
    for a in range(c):
        command_data = input()
        if len(command_data) > 1:
            data = command_data.split()
            command = command_data[0]
            value = command_data[1]
            s.f{command}(f{value})
        s.f{command_data}()
    return(s)



print(set_update(s, c))
