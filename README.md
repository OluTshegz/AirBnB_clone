# 0x00. AirBnB clone - The Console

Welcome to the 0x00. AirBnB clone project! This project aims to create a simplified version of the AirBnB website, focusing on the backend logic and command-line interface.

## Project Description

This project is an AirBnB clone implemented in Python. It allows users to create, manage, and interact with various objects such as Users, Places, Reviews, and more, all through a command-line interface (CLI). The project emphasizes the use of object-oriented programming principles and modular design to create a scalable and maintainable codebase.

## Command Interpreter Description

The command interpreter provides a CLI for interacting with the AirBnB clone. Here's how you can get started and use it:

### How to Start the Command Interpreter

To start the command interpreter, follow these steps:

1. Clone the repository and navigate to the project directory.
2. Open a terminal or command prompt.
3. Run the following command:

   ```shell
   $ ./console.py
   ```

   Alternatively, you can also use the command `python3 console.py` to start the interpreter.

### How to Use the Command Interpreter

Once the command interpreter is running, you can use various commands to interact with the AirBnB clone. Here are some supported basic commands, but are not limited to:

-   `create <class_name>`: Creates a new instance of the specified class.
-   `show <class_name> <id>`: Displays the string representation of a specified instance.
-   `update <class_name> <id> <attribute_name> "<new_value>"`: Update(s) the specified attribute(s) of the instance.
-   `destroy <class_name> <id>`: Deletes the specified instance.
-   `all [class_name]`: Displays/prints all instances of the specified class, or all instances across all classes if no class is specified.
-   `quit`: Exits the command interpreter.

### Examples

Here are a few examples of how to use the command interpreter:

- To create a new user instance:

  ```shell
  (hbnb) create User
  ```

- To display the details of a specific user instance:

  ```shell
  (hbnb) show User 1234-5678-9012
  ```

- To update the email or name attribute of a user instance:

  ```shell
  (hbnb) update User 1234-5678-9012 email "newemail@example.com"
  ```
  ```shell
  (hbnb) update User 1234-5678-9012 name "John Doe"
  ```

- To display all instances of a specific class:

  ```shell
  (hbnb) all User
  ```

- To quit or exit the command interpreter:

  ```shell
  (hbnb) quit
  ```
  ```shell
  (hbnb) exit
  ```

These are just a few examples, and there are many more commands and functionalities available in the command interpreter. Feel free to explore more commands and functionalities within the command interpreter!

## Contributors

This project was developed by [Your Name] and [Other Contributor]. Please refer to the [AUTHORS](AUTHORS) file for more information.

## License

This project is licensed under the [MIT License](LICENSE).

## Conclusion

Thank you for checking out the 0x00. AirBnB clone project. We hope you find it informative and useful for understanding how to build a command-line interface for managing objects in Python. If you have any questions or feedback, please don't hesitate to reach out. Happy coding!
