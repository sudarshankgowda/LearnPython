import multiprocessing.process

def print_process_data(chunk):
    print(f"The chunk data from process : {chunk}")

chunks = [1,2,3,4,5,6,7,8,9]
if __name__=="__main__":
    processes = []
    for chunk in chunks:
        process = multiprocessing.Process(target=print_process_data, args=(chunk,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()