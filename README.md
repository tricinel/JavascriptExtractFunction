# Javascript Extract Function

This is a lightweight Sublime Text 3 plugin that will extract and create a function from the highlighted text. It works in three steps:

1. Highlight the text
2. Select which type of function to create
3. Name your function

Your text will be wrapped into a new Javascript function, depending on what you selected and called right afterwards. You can either automatically paste the new function right in the file, or copy it to clipboard and paste it wherever you like.

## Installation

You can install `JavascriptExtractFunction` via [Package Control](https://packagecontrol.io/).

1. Press <kbd>cmd/ctrl</kbd> + <kbd>shift</kbd> + <kbd>p</kbd> to open the command palette.
2. Type `Install package` and press enter. Then search for `JavascriptExtractFunction`

## Usage

To run the Javascript Extract Function command... open the Sublime Text Command Palette and type "Extract Javascript Function."

You can also right-click on a selected piece of code in a file to bring up the Context Menu and select "Extract Javascript Function."

### Key Bindings

The plugin adds two key bindings that you can use as shortcuts.

* <kbd>alt</kbd> + <kbd>m</kbd> will ask you to select what type of function to extract your function into
* <kbd>shift</kbd> + <kbd>alt</kbd> + <kbd>m</kbd> will automatically extract an arrow function and paste it into your code

### Limitations

This plugin does not currently support multiple selections. If you select more than one block, only the first one will be used in function creation.
