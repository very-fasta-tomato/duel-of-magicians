def dictxml(d, root_node=None):
    wrap = False if None == root_node or isinstance(d, list) else True
    root = 'objects' if None == root_node else root_node
    root_singular = root[:-1] if 's' == root[-1] and None == root_node else root
    xml = ''
    children = []

    if isinstance(d, dict):
        for key, value in dict.items(d):
            if isinstance(value, dict):
                children.append(dictxml(value, key))
            elif isinstance(value, list):
                children.append(dictxml(value, key))
            else:
                xml = xml + ' ' + key + '="' + str(value) + '"'
    else:
        for value in d:
            children.append(dictxml(value, root_singular))

    end_tag = '>' if 0 < len(children) else '/>'

    if wrap or isinstance(d, dict):
        xml = '<' + root + xml + end_tag

    if 0 < len(children):
        for child in children:
            xml = xml + child

        if wrap or isinstance(d, dict):
            xml = xml + '</' + root + '>'

    return xml


