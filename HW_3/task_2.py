# 2. Write a script to remove empty elements from a list.
#     Test list: [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]

m_list=[(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []] 

for item in m_list:
    if len(item) == 0:
        m_list.remove(item)

print(m_list)

print(len([]))
# this is strange.. 