# Function to implement Worst Fit memory allocation
def worst_fit(memory_blocks, requests):
    # Copy the memory blocks to avoid modifying the original list
    remaining_blocks = memory_blocks[:]
    
    # To store allocation results
    allocation = [-1] * len(requests)
    
    print("Initial Memory Blocks:", memory_blocks)
    print("Memory Requests:", requests)
    print("\nProcessing allocations...\n")
    
    # Process each request
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

# Example Input
memory_blocks = [100, 500, 200, 300, 600]
requests = [212, 417, 112, 426]

# Run the Worst Fit Algorithm
allocation, remaining_blocks = worst_fit(memory_blocks, requests)
