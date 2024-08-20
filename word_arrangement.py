import random

def read_words_from_file(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        words = [word for word in file.read().splitlines() if len(word) == 2]
    return words

def arrange_words(words):
    arrangement = {
        "1主人公の現在": words[0],
        "2主人公の近い未来": words[1],
        "3主人公の過去": words[2],
        "4援助者": words[3],
        "5敵対者": words[4],
        "6結末(目的)": words[5]
    }

    output_lines = []
    output_lines.append("                               4援助者:")
    output_lines.append(f"                                 {arrangement['4援助者']}")
    output_lines.append("")
    output_lines.append("3主人公の過去: 1主人公の現在: 2主人公の近い未来: 6結末(目的):")
    output_lines.append(f"   {arrangement['3主人公の過去']}" + 
                         "             {arrangement['1主人公の現在']}" +
                         "           {arrangement['2主人公の近い未来']}" +
                         "          {arrangement['6結末(目的)']}")
    output_lines.append("")
    output_lines.append("                               5敵対者:")
    output_lines.append(f"                                  {arrangement['5敵対者']}")

    return "\n".join(output_lines)

def main():
    file_path = input("Enter the path to the text file: ")
    
    words = read_words_from_file(file_path)
    
    if len(words) < 6:
        print("The file must contain at least 6 words with exactly 2 characters each.")
        return

    random.shuffle(words)

    output_content = arrange_words(words[:6])
    
    output_file_path = "output.txt"
    with open(output_file_path, 'w', encoding="utf-8") as output_file:
        output_file.write(output_content)
    
    print(f"The arranged words have been written to {output_file_path}")

if __name__ == "__main__":
    main()
