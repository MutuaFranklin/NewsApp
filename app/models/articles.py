class Articles:
    '''
     Article class to define Article Objects
    '''

    def __init__(self,title, image, description, author, url, publishedAt):
        self.title = title
        self.image = image
        self.description = description
        self.author = author
        self.url = url
        self.publishedAt = publishedAt