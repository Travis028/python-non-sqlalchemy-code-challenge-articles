class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        self._title = None
        self.title = title
        self.author = author
        self.magazine = magazine
        author._articles.append(self)
        magazine._articles.append(self)
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be between 5 and 50 characters")
        if self._title is not None:
            raise AttributeError("Title cannot be changed after initialization")
        self._title = title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise ValueError("Author must be an Author instance")
        self._author = author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be a Magazine instance")
        self._magazine = magazine


class Author:
    def __init__(self, name):
        self._name = None
        self.name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        if self._name is not None:
            raise AttributeError("Name cannot be changed after instantiation")
        self._name = name

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self._articles:
            return None
        return list({magazine.category for magazine in self.magazines()})


class Magazine:
    _all_magazines = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []
        Magazine._all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) < 2 or len(name) > 16:
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if not isinstance(category, str):
            raise ValueError("Category must be a string")
        if len(category) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._category = category

    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author for article in self._articles})

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1
        
        contributing = [author for author, count in author_counts.items() if count > 2]
        return contributing if contributing else None

    @classmethod
    def top_publisher(cls):
        if not cls._all_magazines:
            return None
        return max(cls._all_magazines, key=lambda mag: len(mag.articles()))