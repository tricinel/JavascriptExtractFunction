# Javascript Extract Function - Sublime Text 3 Plugin
# Created by by Bogdan Lazar (@tricinel)
# MIT

import textwrap
import sublime
import sublime_plugin
from .Edit import Edit as Edit

class JavascriptExtractFunctionCommand(sublime_plugin.TextCommand):
  def run(self, _edit, auto_paste=True, skip_quick_panel=False, command_index=0):
    commands = ["Extract arrow function", "Extract regular function", "Extract anonymous function"]

    self.auto_paste = auto_paste

    if skip_quick_panel:
      self.get_function_name(command_index)
    else:
      self.view.window().show_quick_panel(commands, self.get_function_name)

  def get_function_name(self, command_index):
    if command_index == 0:
      self.view.window().show_input_panel("Function name:", "", self.create_arrow_function, None, None)
    if command_index == 1:
      self.view.window().show_input_panel("Function name:", "", self.create_regular_function, None, None)
    if command_index == 2:
      self.view.window().show_input_panel("Function name:", "", self.create_anonymous_function, None, None)

  def create_arrow_function(self, function_name):
    function_name = self.format_function_name(function_name)
    self.replace_with_function_name(function_name, 0)

  def create_regular_function(self, function_name):
    function_name = self.format_function_name(function_name)
    self.replace_with_function_name(function_name, 1)

  def create_anonymous_function(self, function_name):
    function_name = self.format_function_name(function_name)
    self.replace_with_function_name(function_name, 2)

  def replace_with_function_name(self, function_name, command_index):
    region = self.get_region()
    method_body = self.get_region_text(region)
    new_method = self.build_new_method(function_name, method_body, command_index)

    new_content = ""

    if self.auto_paste:
      new_content += new_method

    if self.region_ends_with_newline(region):
      new_content += "\n"

    new_content += function_name + "();"

    with Edit(self.view) as edit:
      edit.replace(region, new_content)

    self.view.window().run_command('reindent')

    if not self.auto_paste:
      self.copy_method_to_clipboard(function_name, new_method)

  def get_region(self):
    regions = self.view.sel()
    return regions[0]

  def get_region_text(self, region):
    return self.view.substr(region)

  # Created by https://github.com/pashamur/ruby-extract-method/blob/master/RubyExtractMethod.py
  def region_ends_with_newline(self, region):
    return self.view.rowcol(region.end())[1] == 0

  def build_new_method(self, function_name, method_body, command_index):
    if command_index == 0:
      new_method = "\nconst " + function_name + " = () => {\n"
    if command_index == 1:
      new_method = "\nvar " + function_name + " = function " + function_name + "() {\n"
    if command_index == 2:
      new_method = "\nfunction " + function_name + "() {\n"

    new_method += self.indent_text(method_body)
    new_method += "\n};\n"

    if self.auto_paste:
      new_method += "\n"

    return new_method

  def copy_method_to_clipboard(self, function_name, new_method):
    sublime.set_clipboard(new_method)
    message = "The method " + function_name + " is now in your clipboard."
    message += "Use your keybinding for paste-with indent to paste it into your code."
    self.display_message(message)

  # Created by https://github.com/pashamur/ruby-extract-method/blob/master/RubyExtractMethod.py
  def indent_text(self, text):
    indentation = self.get_indentation_string()
    dedented_text = textwrap.dedent(text)
    indented_text = "\n".join(indentation + line for line in dedented_text.splitlines())
    return indented_text

  # Created by https://github.com/pashamur/ruby-extract-method/blob/master/RubyExtractMethod.py
  def get_indentation_string(self):
    if self.use_spaces_for_indentation():
      return self.tab_size() * " "
    return "\t"

  # Created by https://github.com/pashamur/ruby-extract-method/blob/master/RubyExtractMethod.py
  def tab_size(self):
    return self.view.settings().get('tab_size', 2)

  # Created by https://github.com/pashamur/ruby-extract-method/blob/master/RubyExtractMethod.py
  def use_spaces_for_indentation(self):
    return self.view.settings().get('translate_tabs_to_spaces', True)

  @staticmethod
  def display_message(value):
    active_view = sublime.active_window().active_view()
    key = "javascript_extract_method_msg"

    active_view.erase_status(key)
    active_view.set_status(key, value)

  @staticmethod
  def format_function_name(function_name):
    if len(function_name.split(" ")) > 1:
      words = function_name.split(" ")
      first, rest = words[0].lower(), words[1:]
    else:
      first = function_name
      rest = []
    return first + "".join(word.capitalize() for word in rest)
