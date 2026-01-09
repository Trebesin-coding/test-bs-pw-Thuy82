from bs4 import BeautifulSoup 
import requests 
def main():
    url = "https://souhrada.github.io/bsoup-exam/"
    response = requests.get(url) 
    soup = BeautifulSoup(response.content, "html.parser") 
    all_p = soup.find_all("") # jaký má toto účel?
    
  
    ingrediends = soup.find_all('h2.stuff',[0]) # jaký význam má [0] jako další argument?
    # 'h2.stuff' je csskový selector, který lze používat s .select() se s .find_all()

    print (ingrediends, [0]) # proč printujete [0]?

    #with open(path, "w", encoding="utf-8") as f:
    #    json.dump(data, f, ensure_ascii=False, indent=4)

    #print("Uloženo do:", path)
    
    # kde je proměnná path?



if __name__ == "__main__":
    main()