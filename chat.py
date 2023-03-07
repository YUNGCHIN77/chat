def read_file(filename):
    chat = []
    with open(filename, "r", encoding = "utf-8") as f:
        for line in f:
            chat.append(line.strip())
    return chat

def convert(chat):
    new = []
    person = None
    
    for line in chat:
        if line == "Miracle":
            person = "Miracle"
            continue
        elif line == "Brian":
            person = "Brian"
            continue
        if person:    
            new.append(person + ": " + line)
        
    print(new)    
    return new

    
def write_file(filename, new):
    with open(filename, "w", encoding = "utf-8") as f:
        for line in new:
            f.write(f"{line}\n") 
def main():
    chat = read_file("input.txt")
    new = convert(chat)    
    write_file("output.txt", new)
    
main()            
          
