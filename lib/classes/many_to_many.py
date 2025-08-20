# classes/many_to_many.py

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Author name must be a non-empty string")
        self._name = name  
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        
        pass

    def articles(self):
        """Return list of Article instances written by this author"""
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        """Return unique magazines the author has written for"""
        mags = [article.magazine for article in self.articles()]
        return list(dict.fromkeys(mags)) if mags else []

    def add_article(self, magazine, title):
        """Create a new article for this author"""
        return Article(self, magazine, title)

    def topic_areas(self):
        """Return unique categories of magazines written for"""
        mags = self.magazines()
        if not mags:
            return None
        return list(dict.fromkeys([mag.category for mag in mags]))


class Magazine:
    all = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string 2-16 chars")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        self._name = name
        self._category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        """Return list of articles for this magazine"""
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        """Return unique authors who have written for this magazine"""
        authors = [article.author for article in self.articles()]
        return list(dict.fromkeys(authors)) if authors else []

    def article_titles(self):
        arts = self.articles()
        if not arts:
            return None
        return [article.title for article in arts]

    def contributing_authors(self):
        """Authors who wrote more than 2 articles for this magazine"""
        authors = self.contributors()
        result = [author for author in authors if len([a for a in author.articles() if a.magazine == self]) > 2]
        return result if result else None

    @classmethod
    def top_publisher(cls):
        if not cls.all or not Article.all:
            return None
       
        return max(cls.all, key=lambda mag: len(mag.articles()), default=None)


class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title length must be between 5 and 50 characters")
        
        self._title = title  
        self.author = author 
        self.magazine = magazine  

        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
      
        pass

    def __repr__(self):
        return f"<Article title='{self.title}'>"