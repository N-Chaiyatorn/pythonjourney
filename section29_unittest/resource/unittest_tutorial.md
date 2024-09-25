# What is unit test.
`unit test` is testing method process that utilize framework or any platform test your project by isolate each components which can be `functions` or `methods` and test them isolatlly to make sure that your project can work correctly and verify every process performance.

Initially `unit test` focus in testing some smallest unit such as `function` or `method` to verify your code quality and performance.

Developers who implement unit testing should understand every process of project and understand about `class`, `function`, `method` and you should understand the systems that your project work with for example: database system, external system.

Bear in mind that unit testing is the first process of testing program so overall testing have various process as follow:
```
1. Unit testing (Test each unit seperated)
        |
       \|/
2. Integrated testing (Test entire code base by combine every unit together and test it)
        | 
       \|/
3. System testing
        |
       \|/
4. Acceptance testing
```
## Benefit of unit testing.
- It will cover uncover bug and unexpected bug that you can't notice them in code.

- It help you to save your time to fix or verify where the bug is occur in your code.

- When you make a new change you can edit some bug and execute code confidently with no regression result to exists code.

## Type of unit testing.
### Manual.
- This method will be used by writing some manual code by developers.

- This method is compatible when you working with small project because it have less-consistent and take time-consuming.


### Automated.
- This method will uses software platform to test our code, it provide good efficiency and low time consuming which can consist large project. 

- Example: jest, unittest

## Unit testing cycle of life.
```
 --> Make new changes --> Unit test --> detect bug and edit them then unit test again --
 |                                                                                      |
 |--------------------------- Update to repo <-- Review code <--------------------------|
```

- You should consider 3 features in your new change:
```
1. Input or argument.
2. Process.
3. Returned value compared to our expect data.
```

