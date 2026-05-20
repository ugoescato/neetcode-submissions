class TextProcessor:
    # Implement method overloading for format_text method
    def format_text(self, txt1, txt2=None):
        if txt2==None:
            return txt1.upper()
        else:
            return txt1+txt2



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
