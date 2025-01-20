from collections import deque
favorite_deque = deque(["Sammy", "Jamie", "Mary"])
favorite_deque.appendleft("Alice") #ajout au début de favorite_deque
favorite_deque.append("Bob") #ajout à la fin de favorite_deque
print(favorite_deque) #affiche deque(['Alice', 'Sammy', 'Jamie', 'Mary', 'Bob'])
favorite_deque.pop() #affiche Bob
favorite_deque.popleft() #affiche: Alice
print(favorite_deque)
