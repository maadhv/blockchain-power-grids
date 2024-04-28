from brownie import recordstore

def main():
    
    output = recordstore[1]
    print(output.print_dsata())