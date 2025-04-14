import os
import tempfile
import shutil

class BasicCodeEditor:
    def __init__(self):
        self.code_snippets = []  # Stores recent code snippets for suggestions
        self.temp_dir = tempfile.mkdtemp()  # Temporary directory to avoid storage fill-up

    def write_code(self, code):
        """Simulates writing code with suggestions."""
        self.code_snippets.append(code)
        print("\n💡 Suggestion: Did you mean?", self.get_suggestions(code))

    def get_suggestions(self, code):
        """Returns basic code suggestions based on previous snippets."""
        return [snippet for snippet in self.code_snippets if snippet.startswith(code[:3])]

    def execute_code(self, code):
        """Executes Python code and handles errors gracefully."""
        try:
            exec(code, {})  # Execute in an isolated environment
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")

    def clear_temp(self):
        """Clears temporary storage to prevent disk usage."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)
        print("🗑️ Temporary files cleared!")

# Example Usage
editor = BasicCodeEditor()
editor.write_code("print('Hello, world!')")
editor.execute_code("print('Running in Basic Mode')")
editor.clear_temp()
