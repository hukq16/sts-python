from ..core.Settings import Settings
import re

class DescriptionLine:
    text: str = None
    width: float = None
    cachedTokenizedText: [str] = None
    cachedTokenizedTextCN: [str] = None
    offsetter = Settings.scale * 10.0

    def __init__(self, text: str, width: float):

        self.text = text.strip()
        self.width = width - self.offsetter

    def getCachedTokenizedText(self):
        if self.cachedTokenizedText is None:
            self.cachedTokenizedText = self.tokenize(self.text)

        return self.cachedTokenizedText

    def getCachedTokenizedTextCN(self):
        if self.cachedTokenizedTextCN is None:
            self.cachedTokenizedTextCN = self.tokenizeCN(self.text)

        return self.cachedTokenizedTextCN

    @staticmethod
    def tokenize(desc: str):
        tokenized = re.split(r"\s+", desc)

        i = 0
        while i < len(tokenized):
            tokenized[i] = tokenized[i] + ' '
            i += 1
        return tokenized

    @staticmethod
    def tokenizeCN(desc: str):
        tokenized = re.split(r"\s+", desc)

        i = 0
        while i < len(tokenized):
            tokenized[i] = tokenized[i].replace("!", "")
            i += 1

        return tokenized

    def getText(self):
        return self.text

    def __str__(self):
        return self.text
