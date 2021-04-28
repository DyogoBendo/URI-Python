if __name__ == "__main__":
    body = []
    is_body = False
    ended = False
    while not ended:
        try:
            entrada = input()
            if entrada.find("</body>") > - 1:
                is_body = False
            
            if is_body:
                body.append(entrada)

            if entrada.find("<body>") > - 1:
                is_body = True            
            
            if entrada == "</html>":
                ended = True
        except:
            break
    for line in body:
        print(line)
    