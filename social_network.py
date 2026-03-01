class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
   '''
    
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''
    
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name in self.people:
            print(f"{name} already exists in the network.")
        else:
            self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} doesn't exist!")
            return
        if person2_name not in self.people:
            print(f"Friendship not created. {person2_name} doesn't exist!")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for person in self.people.values():
            friend_names = [friend.name for friend in person.friends]
            print(f"{person.name} is friends with: {', '.join(friend_names)}")



if __name__ == "__main__":
    network = SocialNetwork()


    network.add_person("Alex")
    network.add_person("Jordan")
    network.add_person("Morgan")
    network.add_person("Taylor")
    network.add_person("Casey")
    network.add_person("Riley")


    network.add_person("Alex")


    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Morgan")
    network.add_friendship("Jordan", "Taylor")
    network.add_friendship("Morgan", "Casey")
    network.add_friendship("Taylor", "Riley")
    network.add_friendship("Casey", "Riley")
    network.add_friendship("Morgan", "Riley")
    network.add_friendship("Alex", "Taylor")


    network.add_friendship("Jordan", "Johnny")

    print("\n--- Social Network ---")
    network.print_network()



"""
Design Memo:

A graph is the ideal structure for representing a social network because relationships
between users are naturally bidirectional and non-hierarchical. In a social network,
each person can be connected to many others, and those connections do not follow a
strict parent-child structure. Using an adjacency list allows each Person object to
maintain a list of friends, making it easy to add and access connections efficiently.

A list would not work well because it does not inherently represent relationships
between elements. We would need additional logic to track who is connected to whom.
Similarly, a tree would not be appropriate because trees enforce a hierarchical
structure with only one parent per node. Social networks are not hierarchical;
they are many-to-many relationships, which makes graphs much more suitable.

One trade-off I noticed is that adding friendships requires checking that both users
exist and preventing duplicate connections. While adding a friend is efficient
(approximately O(1) average time), printing the network requires iterating over all
people and their friend lists, which takes O(V + E) time, where V is the number of
people and E is the number of friendships. However, this is expected behavior in
graph traversal. Overall, the adjacency list structure provides a flexible and
scalable way to represent dynamic relationships in a social network.
"""
