# Python Program

# Methods having same name but different sequence of parameters

# Define Class
class Display():
    
    # Define Methods
    def output(self, n = int, c = chr):
        print(n, "\t", c)

    def output(self, c = chr, n = int):
        print(c, "\t", n)
    
# Creating class instance
dsp = Display()

# Call the Methods
dsp.output(15, "Programming Skills")
dsp.output("Programming Skills", 10)

print("----------------------------------------------")

# Actually Python does not support Method Overloading

# Thanks for Watching