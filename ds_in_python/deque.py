from collections import deque

# Create a deque
d = deque()

# Add elements to the deque
d.append(1)        # Add to the right
d.appendleft(2)    # Add to the left

print("Deque after append and appendleft:", d)

# Remove elements from the deque
d.pop()            # Remove from the right
d.popleft()        # Remove from the left

print("Deque after pop and popleft:", d)

# Add multiple elements to the deque
d.extend([3, 4, 5])        # Add to the right
d.extendleft([6, 7, 8])    # Add to the left

print("Deque after extend and extendleft:", d)

# Rotate the deque
d.rotate(1)    # Rotate to the right
print("Deque after rotating to the right:", d)

d.rotate(-1)   # Rotate to the left
print("Deque after rotating to the left:", d)

# Access elements in the deque
print("First element:", d[0])
print("Last element:", d[-1])