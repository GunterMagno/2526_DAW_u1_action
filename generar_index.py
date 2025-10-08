def main():
    with open("report.md", "r", encoding="utf-8") as f:
        contenido = f.read()

    with open("index.md", "w", encoding="utf-8") as f:
        f.write(contenido)
        
if __name__ == "__main__":
    main()