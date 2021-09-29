import requests
import xml.etree.ElementTree as ET

# IT JUST FUCKING WORKS LOL

first_item_info = []
TEMP_XML_FILE = "iptrss/movieinfo/file.xml"
LAST_MOVIE_FILE = "iptrss/movieinfo/lastmovie.txt"

def main():
    feed_url = "https://iptorrents.com/t.rss?u=315854;tp=07d2b12c3465a70e02608702b3f65c3a;48;7;20;38;100;101;89;68;62;6;90;87;54;22;99;4;5;66;65;79;23;55;25;26;82;24;83;download"
    data = requests.get(feed_url).content

    with open(TEMP_XML_FILE, "w", encoding="utf-8") as fmake1:
        fmake1.write(data.decode())

    tree = ET.parse(TEMP_XML_FILE)
    root = tree.getroot()

    global first_item_info

    j = 0
    for elem in root:
        for subelem1 in elem:
            for i in subelem1:
                if j <= 3:
                    # print(i.text)
                    first_item_info.append(f"{i.text}")
                    j += 1
                else:
                    break
            
    print("[+] Latest request:", first_item_info[0])

    with open(LAST_MOVIE_FILE, "r", encoding="utf-8") as lastmvname:
        last_movie_name = lastmvname.read()
    
    if last_movie_name == first_item_info[0]:
        print("[-] The latest title has not been updated yet")
    else:
        print("[+] New latest title:", first_item_info[0])
        with open(LAST_MOVIE_FILE, "w", encoding="utf-8") as newlastmv:
            newlastmv.write(first_item_info[0])
    
    first_item_info.clear()




main()