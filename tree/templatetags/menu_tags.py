from django.template import RequestContext
from django.templatetags.cache import register
from tree.models import Menu


@register.inclusion_tag("tree/menu.html", takes_context=True)
def draw_menu(context: RequestContext, menu_name: str) -> dict:
    request = context["request"]
    elements = list(filter(None, request.path.split("/")))
    element_html = f'<a href="/{menu_name}">{menu_name}</a></br>'

    if elements and menu_name in elements:
        menu_items = Menu.objects.select_related("menu_name", "parent").filter(
            menu_name__name=menu_name
        )

        new_menu_items = []
        for menu_item in menu_items:
            if menu_item.menu_name.name == elements[0]:
                if str(menu_item.parent) in elements or menu_item.parent is None:
                    new_menu_items.append(menu_item)

        roots = Node().get_item(new_menu_items)
        result = NodeMenuHtmlRender(roots)
        return {"menu": element_html, "menu_items": result.tree()}
    return {"menu_items": element_html}


class Node:
    __slots__ = "children", "item", "item_slug", "objects", "roots"

    def __init__(self, children=None, item=None, item_slug=None):
        self.objects = {}
        self.roots = []
        self.item = item
        self.item_slug = item_slug
        self.children = children

    def get_item(self, menu_items):
        for item in menu_items:
            if item.pk in self.objects:
                elem = self.objects[elem]
                elem.item = item
            else:
                elem = Node(children=[], item=item, item_slug=item.slug)
                self.objects[item.pk] = elem

            if item.parent is None:
                self.roots.append(elem)
            else:
                if item.parent_id in self.objects:
                    parent_elem = self.objects[item.parent_id]
                else:
                    parent_elem = Node(children=[], item=item, item_slug=item.slug)
                parent_elem.children.append(elem)
        return self.roots


class NodeMenuHtmlRender:
    __slots__ = "html_result", "roots"

    def __init__(self, roots):
        self.html_result = None
        self.roots = roots

    def tree(self):
        self.html_result = "<ul>"
        for root in self.roots:
            self.tree_recursion(root, 0)
        self.html_result += "</ul>"
        return self.html_result

    def tree_recursion(self, root, level=0):
        self.html_result += f"<li><a href='{root.item.slug}'>{root.item}</a>"
        if len(root.children) > 0:
            self.html_result += "<ul>"
            for node in root.children:
                self.tree_recursion(node, level + 1)
            self.html_result += "</ul>"
        self.html_result += "</li>"
