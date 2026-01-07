from bs4 import BeautifulSoup 
import requests 
def main():
    url = "https://souhrada.github.io/bsoup-exam/"
    response = requests.get(url) 
    soup = BeautifulSoup(response.content, "html.parser") 
    all_p = soup.find_all("")
    
  
    ingrediends = soup.find_all('h2.stuff',[0]) 

    print (ingrediends, [0])

    #with open(path, "w", encoding="utf-8") as f:
    #    json.dump(data, f, ensure_ascii=False, indent=4)

    #print("Uloženo do:", path)




if __name__ == "__main__":
    main()