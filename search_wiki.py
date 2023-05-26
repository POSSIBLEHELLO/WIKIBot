import wikipediaapi


def get_wiki_page(text: str):
    wiki = wikipediaapi.Wikipedia('en')
    result = wiki.page(text)
    

    return result.summary