

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        
        def convert_item_to_html(item):
            return " " + item[0] + '="' + item[1] + '"'

        return "".join(map(convert_item_to_html, self.props.items()))
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if not self.value:
            raise ValueError("Leaf node must have a value")
        if self.tag is None:
            return str(self.value)
        return f'<{self.tag}{self.props_to_html()}>{str(self.value)}</{self.tag}>'
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}. {self.children}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent node must have a tag")
        if self.children == None:
            raise ValueError("Parent node must have children")
        if not isinstance(self.children, list):
            raise ValueError("ParentNode.children must be a list type")
        
        return f'<{self.tag}{self.props_to_html()}>{"".join(map(lambda child: child.to_html(), self.children))}</{self.tag}>'

