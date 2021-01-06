import xml.etree.ElementTree as et
from sys import path 
path.append("../types")
from tag import tag

class DataBase : 
    def open_xml(self, xml_path) : 
        tree = None
        try:
            tree = et.parse(xml_path)
        except : 
            open(xml_path, "w").close()

        if tree == None:
            root = et.Element("items")
            tree = et.ElementTree(root)
            tree.write(xml_path)
        return tree
    
    def add_tag(self, new_tag) : 
        tree = self.open_xml("tags.xml")
        root = tree.getroot()
        tag_element = root.makeelement("tag", {})
        id_sub_element = et.SubElement(tag_element, "id")
        name_sub_element = et.SubElement(tag_element, "name")
        is_active_sub_element = et.SubElement(tag_element, "is_active")
        id_sub_element.text = str(new_tag.get_id())
        name_sub_element.text = new_tag.get_name()
        is_active_sub_element.text = str(new_tag.get_is_active())
        root.append(tag_element)

        tree.write("tags.xml")
    
    def get_tags(self) : 
        tree = self.open_xml("tags.xml")
        root = tree.getroot()
        tags = []
        for item in root : 
            tag_item = tag(item.find("name").text)
            tag_item.set_id(item.find("id").text)
            tag_item.set_is_active(item.find("is_active").text)
            tags.append(tag_item)
        return tags
