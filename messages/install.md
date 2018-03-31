# Javascript Extract Function

This is a lightweight Sublime Text 3 plugin that will extract and create a function from the highlighted text. It works in three steps:

1. Highlight the text
2. Select which type of function to create
3. Name your function

Your text will be wrapped into a new Javascript function, depending on what you selected and called right afterwards. You can either automatically paste the new function right in the file, or copy it to clipboard and paste it wherever you like.

## Usage

To run the Javascript Extract Function command... open the Sublime Text Command Palette and type "Extract Javascript Function."

You can also right-click on a selected piece of code in a file to bring up the Context Menu and select "Extract Javascript Function."

### Key Bindings

The plugin adds two key bindings that you can use as shortcuts.

* `alt + f` will ask you to select what type of function to extract your function into
* `shift + alt + f` will automatically extract an arrow function and paste it into your code

## Author

Bogdan Lazar

## License

The MIT License (MIT)

Copyright (c) 2018 Bogdan Lazar
