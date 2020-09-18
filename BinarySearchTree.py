def bst_search(tree, key):
    if not tree:
        return None
    elif tree[0] == key:
        return tree[1]
    elif tree[0] < key:
        return bst_search(tree[2], key)
    else:
        return bst_search(tree[3], key)
