class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    
    def __init__(self,name,number):
        self.name=name
        self.number=number

    def __repr__(self):
        return f"{self.name}:{self.number}")

class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
   
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None

class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    
    def __init__(self,size=10):
        self.size=size
        self.data=[None]*self.size

    def hash_function(self,key):
        hash_sum=0
        for i, char in enumerate(key):
            hash_sum+=(i+1)*ord(char)
        return hash_sum % self.size

    def insert(self,value,key):
        index=self.hash_function(key)
        new_node=Node(key,value)
        if self.data[index] is None:
            self.data[index]=new_node
            return
        current=self.data[index]
        while True:
            if current.key==key:
                current.value=value
                return
            if current.next is None:
                break
            current=current.next
        current.next=new_node
    
    def search(self,key):
        index=self.hash_function(key)
        current=self.data[index]
        while current:
            if current.key==key:
                return current.value
            current=current.next
        return None

    def print_table(self):
        for i, node in enumerate(self.data):
            print(f"Index {i}:",end=" ")
            current=Node
            if not current:
                print("empty")
            else:
                while current:
                    print(f"[{current.key}:{current.value.number}]", end=" -> ")
                    current=current.next
                print('None')

# Test your hash table implementation here.  
if __name__ == "__main__":
    table =HashTable(size=10)
    table.insert("Alice",Contact("Alice","555-1234"))
    table.insert("Bob",Contact("Bob","555-5678"))
    table.insert("Charlie",Contact("Charlie","555-8765"))
    table.insert("Alicia",Contact("Alicia","555-9999"))

    print("\n--- Contact Lookup ---")    
    print(table.search("Alice"))    
    print(table.search("Bob"))    
    print(table.search("Eve"))

    print("\n--- Hash Table Structure ---")
    table.print_table()