class TextProcessor:
    # Implement method overloading for format_text method
    def format_text(self, *args):
        if len(args) == 1:
            return str(args[0]).upper()
        else:
            a, b = args
            return a+b



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
