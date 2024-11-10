# import heapq
# from collections import Counter, namedtuple

# class Node(namedtuple("Node", ["char", "freq", "left", "right"])):
#     def __lt__(self, other): return self.freq < other.freq  # For heap comparisons

# def huffman_encoding(text):
#     # Count frequencies and build the heap
#     freq = Counter(text)
#     heap = [Node(char, freq[char], None, None) for char in freq]
#     heapq.heapify(heap)

#     # Build the Huffman Tree
#     while len(heap) > 1:
#         left = heapq.heappop(heap)
#         right = heapq.heappop(heap)
#         merged = Node(None, left.freq + right.freq, left, right)
#         heapq.heappush(heap, merged)



#     # Generate codes
#     def build_codes(node, prefix=""):
#         if node.char: codes[node.char] = prefix
#         else:
#             build_codes(node.left, prefix + "0")
#             build_codes(node.right, prefix + "1")

#     codes = {}
#     root = heap[0]
#     build_codes(root)

#     # Encode the text
#     encoded_text = "".join(codes[char] for char in text)
#     return codes, encoded_text

# # Example usage
# text = "huffman example"
# codes, encoded_text = huffman_encoding(text)
# print("Character Codes:", codes)
# print("Encoded Text:", encoded_text)

import heapq
from collections import Counter , namedtuple

class Node(namedtuple("Node",["char","freq","left","right"])):
    def __lt__(self , other): return self.freq < other.freq


def huffman_encoding(text):

    freq = Counter(text)
    heap = [Node(char, freq[char],None ,None)for char in freq]
    heapq.heapify(heap)

    while( len(heap) > 1):
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq ,left , right)
        heapq.heappush(heap,merged)

    def build_codes(node, prefix=""):
        if node.char:
            codes[node.char] = prefix
        else:
            build_codes(node.left,prefix="0")
            build_codes(node.right,prefix="1")

    codes= {}
    root = heap[0]
    build_codes(root)

    encoded_text = "".join(codes[char] for char in text)
    return codes, encoded_text

text = "huffman example"
codes, encoded_text = huffman_encoding(text)
print("Character Codes:", codes)
print("Encoded Text:", encoded_text)