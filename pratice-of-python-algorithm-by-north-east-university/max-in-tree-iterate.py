'''
这个对程序很好利用的递归，体会递归的强大力量
'''
tree=[
				30,

				[52,
					[23,[],[]],
					[74,[],[]],
				],

				[15,
					[86,[],[]],
					[10,[],[]]
				]

			]

def getmax(tree):
    if tree != []:
        max = tree[0]
        for sub in tree[1:]:
            if sub != []:
                b = getmax(sub)
                if max <= b:
                    max = b
        return max
    else:
        return None

print(getmax(tree))