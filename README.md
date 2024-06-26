# AirBnB Clone

This project is a command-line interface for managing data related to an Airbnb-like platform. It includes models for different entities such as users, places, cities, amenities, and reviews.

## Command Interpreter

To start the command interpreter, run: ./console.py
This will launch the interactive console, where you can use various commands to create, show, update, and destroy instances of different models.

Some examples:

- `create BaseModel`: Creates a new instance of the `BaseModel` class.
- `show BaseModel 49faff9a-6318-451f-87b6-910505c55907`: Prints the string representation of the `BaseModel` instance with the given ID.
- `update BaseModel 49faff9a-6318-451f-87b6-910505c55907 name "My First Model"`: Updates the `name` attribute of the specified `BaseModel` instance.
- `destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907`: Deletes the specified `BaseModel` instance.
- `all BaseModel`: Prints a list of all `BaseModel` instances.

For more information on available commands and their usage, type `help` in the console.
