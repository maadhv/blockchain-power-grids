from brownie import recordstore , accounts
import random
import matplotlib.pyplot as plt

def deploy():
    
    account = accounts[1]
    store = recordstore.deploy({"from":account})
    
    return store

'''def check_value(store):
    
    value = store.get_supply()
    print(f"value stored in block: {value}")
    
    transaction = store.update_supply(240,{"from":accounts[1]})
    transaction.wait(1)
    
    value = store.get_supply()
    print(f"value stored in block: {value}")'''
    
def init(store):
    store.set_data("xxxxx",0,0,0)
    
def add_values(store):
    sd = random.randint(200,300)
    temp = random.randint(75,80)
    sect = ["sector A","sector B","sector C"]
    idx = random.randint(0,3)
    store.update_data(sect[idx],sd,sd,temp)
    
def check_values(store):
    output = store.print_data()
    
    print(f"sector: {output[0]}")
    print(f"supply: {output[1]}")
    print(f"demand: {output[2]}")
    print(f"temeprature: {output[3]}")
    
def live_check(store):
    '''
    using random values to replicate sensor values 
     as gathering sensor data is outside the time and computational
     limtis of the hackathon
     '''
    sd = random.randint(200,300)
    temp = random.randint(75,80)
    sect = ["sector A","sector B","sector C"]
    idx = random.randint(0,3)
    store.update_data(sect[idx],sd,sd,temp)
    output = store.print_data()
    
    print(f"sector: {output[0]}")
    print(f"supply: {output[1]}")
    print(f"demand: {output[2]}")
    print(f"temeprature: {output[3]}")
    
def plot_supply(store):
    
    #stimulating sensor data
    supply = [220,224,256,264,267,270]
    values = store.print_data()
    supply.append(values[1])
    sp = str(values[1])
    plt.plot(supply,marker = 'o')
    plt.xlabel('hours')
    plt.ylabel('supply MWe')
    plt.title("MWe production")
    plt.text(0, 1,f"production: {sp} \n demand: {sp}" , verticalalignment='bottom', horizontalalignment='left',
             transform=plt.gca().transAxes, fontsize=12, color='green')
    plt.grid(True)
    plt.show()
    
def plot_temp(store):
    #stimulating sensor data
    supply = [77,78,77,80,75,79]
    values = store.print_data()
    supply.append(values[3])
    sp = str(values[3])
    plt.plot(supply,marker = 'o')
    plt.xlabel('hours')
    plt.ylabel('temperature (C)')
    plt.title("Temperature reading")
    plt.text(0, 1,f"temperature: {sp}" , verticalalignment='bottom', horizontalalignment='left',
             transform=plt.gca().transAxes, fontsize=12, color='green')
    plt.grid(True)
    plt.show()
    
    
    
def main():
    
    store = deploy()
    init(store)
    #check_values(store)
    live_check(store)
    plot_supply(store)
    plot_temp(store)
    
    