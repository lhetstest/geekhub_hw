# 2. Write a script to remove empty elements from a list.
#     Test list: [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]

m_list=[(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []] 

m_list_new = []
for item in m_list:
    if item:
        m_list_new.append(item)

print(m_list_new)