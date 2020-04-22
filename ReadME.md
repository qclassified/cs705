# Part 2: Develop and write a report: 25pt (5+1+2+4+2+1+5+2+3)

Please review the python source codes from lecture 2 (Building smallest blockchain.txt) and lecture 3 (PoW-2.txt). 
The first application shows a chain of blocks, but it does not provide any proof of work. 
Second code shows how to build a simple proof of work, but it does not show any block chain. 
Using the knowledge of these two codes please build a simple local blockchain application where there will be 3-4 users (Alice, Bob, Charlie,….). 
They will exchange some values (like currency) to each other. Then these transactions will be gathered and stored in the blockchain. 
Before storing, the miners should validate the transactions and perform proof of work to create the block and store it in the chain. 

You can have as much as features in your application as you wish but not less than the below: 
1.	Make use of merkle tree to store the transaction hash. 5
2.	Predefined transaction pools between the users.1
3.	You need be able to demonstrate creating genesis block and then adding following blocks in the chain. 2
4.	Demonstrate that miners are solving PoW puzzle and one get selected who solves it first. 4
5.	Demonstrate and explain how integrity and verifiability are ensured. 2
6.	The block should contain atleast the Hash=H(root hash of merkle tree, prev hash, nonce, timestamp) 1
7.	Also please make sure:
a.	Clear and all step by step explanation 5
b.	Showing the full blockchain in output as well as in report. 2
8.	Explain the benefits of using merkle tree in this context. What would happen if you would not use the merkle tree to store all the transactions’ hash? 3
You can use any platform to build this application. 

Prepare a report (like the Ethereum application manuals) and explain each and every possible function, provide screen shot of your code and output. 
