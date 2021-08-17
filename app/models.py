class Articles:
    '''
     Article class to define Article Objects
    '''

    def __init__(self,title, image, description, author, url, publishedAt, content):
        self.title = title
        self.image = image
        self.description = description
        self.author = author
        self.url = url
        self.publishedAt = publishedAt
        self.content = content

        




class Source:
    '''
     Source class to define Source Objects
    '''

    def __init__(self, id, name, description, url, category, language):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language


