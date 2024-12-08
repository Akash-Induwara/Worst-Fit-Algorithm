# Function to implement the Worst Fit memory allocation algorithm
def worst_fit(memory_blocks, requests):
    # Copy memory blocks to avoid modifying the original list
    remaining_blocks = memory_blocks[:]
    
    # To store allocation results (-1 indicates unallocated)
    allocation = [-1] * len(requests)
    
    
    # Process each memory request
    for i, request in enumerate(requests):
        # Find the index of the largest block that can accommodate the request
        max_index = -1
        for j in range(len(remaining_blocks)):
            if remaining_blocks[j] >= request:
                if max_index == -1 or remaining_blocks[j] > remaining_blocks[max_index]:
                    max_index = j
        
        # Allocate memory if a suitable block is found
        if max_index != -1:
            allocation[i] = max_index
            remaining_blocks[max_index] -= request
            print(f"Request {request} allocated to Block {memory_blocks[max_index]} (Remaining: {remaining_blocks[max_index]})")
        else:
            print(f"Request {request} could not be allocated (No suitable block found).")
    
    # Output final results
    print("\nFinal Allocation Results:")
    for i, req in enumerate(requests):
        if allocation[i] != -1:
            print(f"Request {req} allocated to Block {memory_blocks[allocation[i]]}.")
        else:
            print(f"Request {req} could not be allocated.")
    
    print("\nRemaining Memory Blocks:", remaining_blocks)
    return allocation, remaining_blocks


# Main Execution
if __name__ == "__main__":
    # Ask the user to enter memory blocks
    print("Enter the sizes of memory blocks separated by spaces:")
    memory_blocks = list(map(int, input().split()))
    
    # Ask the user to enter memory requests
    print("Enter the sizes of memory requests separated by spaces:")
    requests = list(map(int, input().split()))
    
    # Display initial inputs
    print("\nInitial Memory Blocks:", memory_blocks)
    print("Memory Requests:", requests)
    
    # Run the Worst Fit Algorithm
    allocation, remaining_blocks = worst_fit(memory_blocks, requests)
