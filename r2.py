def read_file(filename):
    chat = []
    with open(filename, "r", encoding = "utf-8") as f:
        for line in f:
            chat.append(line.strip())
    return chat


def convert(chat):
    person = None
    show_word_count = 0
    show_sticker_count = 0
    show_image_count = 0
    brian_sticker_count =0
    brian_word_count = 0
    brian_image_count = 0
    for line in chat:
        new = line.split(" ")
        time = new[0]
        name = new[1]     
        if name == "秀":
            if new[2] == "貼圖" :
                show_sticker_count += 1
            elif new[2] == "圖片" :
                show_image_count += 1
            else:
                for m in new[2:]:
                    show_word_count += len(m)                     
        elif name == "黃永欽":
            if new[2] == "貼圖":
                brian_sticker_count += 1
            elif new[2] == "圖片" :
                brian_image_count += 1
            else:
                for m in new[2:]:
                    brian_word_count += len(m)
    print(f"秀說了{show_word_count},傳了{show_sticker_count}個貼圖,傳了{show_image_count}張圖片")
    print(f"黃永欽說了{brian_word_count},傳了{brian_sticker_count}個貼圖,傳了{brian_image_count}張圖片")
    return new

    
def write_file(filename, new):
    with open(filename, "w", encoding = "utf-8") as f:
        for line in new:
            f.write(f"{line}\n")
            
            
def main():
    chat = read_file("LINE.txt")
    new = convert(chat)    
    #write_file("output.txt", new)
    
main()            
          

