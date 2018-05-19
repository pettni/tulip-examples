from tulip import transys

def fill_fts(fts):
  """Add a trap state and direct all outgoing actions to it"""
  fts.add_node('trap')
  for node in fts.nodes():
    actions = transys.MathSet(attr['sys_actions'] for _,_,attr in fts.transitions.find(node))
    for action in fts.sys_actions:
      if action not in actions:
        fts.add_edge(node, 'trap', sys_actions=action)
