class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    result = []
    nodes_to_visit = [self.root]

    while len(nodes_to_visit) > 0:
       # 1. Remove the first node from the `nodes_to_visit` list
      node = nodes_to_visit.pop(0)
      # 2. Check each id to see if it's equal to node['id'] and return that node else return None
      if node['id'] == id:
        return node 
      nodes_to_visit = node['children'] + nodes_to_visit
       # 3. Add its children (if any) to the BEGINNING of the `nodes_to_visit` list
    return None

