def klasyfikator(napis):
    slowa = []
    for slowo in napis.split():
        if len(slowo) <= 5:
            przedrostek = "+ "
        else:
            przedrostek = "- "
        nowe_slowo = przedrostek + slowo
        print(nowe_slowo)

klasyfikator("Lorem ipsum dolor siot amet, consectetur adipiscing elit.")
