### What, in your opinion, is an important part of code reviews? That is, what is something you pay attention to when you review code, and that you appreciate when others do the same for your code?

####Answer: 
First I look at the description to get a basic understanding of what the code is trying to achieve, then I skim over the code for readability and most importantly see if the code looks easy to read at first glance. Then I look at the variables and figure out what they are doing, if the variables are named accordingly this should be easy depending on what the code is trying to do. Then I look at how the functions are organized to figure out if they follow a uniform logic and are not spurrious.

### We have an awful lot of computers here, and it gets pretty confusing with slightly different things running on all of them. How could containers help us improve this situation? Docker can run their own environments they are separate from the operating system.

####Answer: 
Containers allow easy distribution of all the dependancies needed to run a program regardless of the master computer. Meaning that whether the person using the code has a Windows, Linux, or Mac it will work the same because the container sort of virtualizes a very tiny operating system that only has the necessary packages needed to run that program. This allows ease between users to be able to test and deply the different containers that serve the purpose that is needed from them. Basically makes a developers life a lot more convinient allowing for more deployment and less debugging.