import concurrent.futures

def your_function(temperature):

    result = temperature + 10  
    return result

def main():
    temperatures = [310, 311, 312, 313, 314]
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(your_function, temperatures))
    
    print(results)

if __name__ == "__main__":
    main()
