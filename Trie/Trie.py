class TrieNode:
	def __init__(self):
		self.children = {}
		self.EndOfWord = False


class TriePrefixTree:
	def __init__(self):
		self.root = TrieNode()

	def insert(self, word):
		curr = self.root
		for c in word:
			if c not in curr.children:
				curr.children[c] = TrieNode()
			curr = curr.children[c]
		curr.EndOfWord = True

	def search(self, word):
		curr = self.root
		for c in word:
			if c not in curr.children:
				return False
			curr = curr.children[c]
		return curr.EndOfWord

	def startsWith(self, prefix):
		curr = self.root
		for c in prefix:
			if c not in curr.children:
				return False
			curr = curr.children[c]
		return True

