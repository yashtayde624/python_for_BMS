def main():
    n = input("file name").strip().lower()
    if n.endswith("jpg") or n.endswith("jpeg"):
        print ("image/jpeg")
    elif n.endswith("pdf"):
        print("application/pdf")
    elif n.endswith("gif"):
        print("image/gif")
    elif n.endswith("png"):
        print("image/png")
    elif n.endswith("txt"):
        print("text/plain")
    elif n.endswith("zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

main()
