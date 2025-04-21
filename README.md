# Bank Account Simulation Project

### Description
The purpose of this project is to demonstrate a firm grasp of various python topics. Some of these include, unittesting, custom expections, aspects of the collections library, OOP, aspects of tkinter and some basic recusrion.

### Features 
This projects features a simple but clear ui allowing the user to make withdrawls and deposits, keep track of all of them, buy items and keep a record of all purchases, all while keeping track of the users balance and not allowing them to spend more than they have.

#### Account:
- The user will initially be prompted to create an account with there name and a dialy withdrawl limit. They are able to change both of these, given certain condotions are met, at a later date.

#### Withdrawl and deposit history:
- This is kept track of using a UserDict with the __setitem__ method overridden to allow for more context specfic entries. Each entry is conposed of a an id, they key, that also specifies whether it was a withdrawl or deposit. The accompaniying value is a namedTuple that holds all pertinent information

#### Deposits and withdrawls:
- A few functions are defined to allow the user to make deposits and withdraws, based on the current balance. A custome excpetion accompanies these that is raised if the users tries to make a withdrawl that exceeds there balance.

#### Transaction histry:
- This portion has a similar structure to "Withdrawl and deposit history". A UserDict with an ooverriden __setItem__ method, a named tuple, a function to get the transaction origing, are what compose the logic and strucure of this dection. This portion works hand in hand with the functionailty for the shop which will be described shortly.

#### Shop (making transactions):
- A simple set of functions allows for the user to buy or skip random items. If they choose to purchase the item and have a balanace that allows for it the purchase will be made, the balance updated, and the transcation recorded. If the purchase amount exceeds the balance an exception will be thrown.

### Technologies
The libraries used in order of usage are as follows, collections, tkinter, random.

#### Collections:
- Used for UserDict and NamedTuple

#### tkinter:
- Used for GUI

#### Random
- Used purley for randint.


### Future additions
- User authenticitions (login and password)
- Scam simulation and detection
