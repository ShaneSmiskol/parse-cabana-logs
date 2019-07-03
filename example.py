import matplotlib.pyplot as plt

def hex_to_binary(hexdata):
    return (bin(int(hexdata, 16))[2:]).zfill(len(hexdata) * 4) # adds leading/trailing zeros

def start_example():
    with open('corolla.csv', 'r') as f:
        csv = f.read().split('\n')
    
    data = []
    for line in csv:
        if line != "" and line != 'time,addr,bus,data':
            line = line.split(",")
            data.append({'time': float(line[0]), 'addr': int(line[1]), 'bus': int(line[2]), 'data': line[3]})
    
    GAS_PEDAL = [i for i in data if i['addr'] == 705 and i['bus'] == 0]
    print(len(GAS_PEDAL))
    
    GAS_POS = []
    for i in GAS_PEDAL:
        this_GP = hex_to_binary(i['data']) # convert hex to binary
        this_GP = int(this_GP[48:56], 2) # get gas pedal position and convert binary to decimal
        GAS_POS.append(this_GP * 0.005) # toyota pedal position is factor of 0.005
    
    plt.plot(range(len(GAS_POS)), GAS_POS)
    plt.show()