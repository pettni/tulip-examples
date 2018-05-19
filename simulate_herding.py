import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def loc_to_xy(loc):
  spl = loc[1:].split('x')
  return np.array([int(spl[0]), int(spl[1])])

def simulate(controller, fts):
  # Simulation of the herding system

  # Constants
  Tmax = 180   # max sim time

  # Initial states
  rob_init = 'a5x3'
  cat_init = 'a0x2'
  dog1_init = 'a4x4'
  dog2_init = 'a5x0'
  mouse_init = 'a3x0'

  t = 0

  # Graph locations
  loc = dict()
  loc['rob'] = rob_init
  loc['cat'] = cat_init
  loc['dog1'] = dog1_init
  loc['dog2'] = dog2_init
  loc['mouse'] = mouse_init

  rob_x = np.zeros([2, Tmax+1])
  rob_x[:,0] = loc_to_xy(rob_init)

  cat_x = np.zeros([2, Tmax+1])
  cat_x[:,0] = loc_to_xy(cat_init)

  dog1_x = np.zeros([2, Tmax+1])
  dog1_x[:,0] = loc_to_xy(dog1_init)

  dog2_x = np.zeros([2, Tmax+1])
  dog2_x[:,0] = loc_to_xy(dog2_init)

  mouse_x = np.zeros([2, Tmax+1])
  mouse_x[:,0] = loc_to_xy(mouse_init)

  while t < Tmax:
  
    outputs = {key: False for key in controller.input_vars}

    # set outputs related to FTS
    outputs['eloc'] = loc['rob']
    for ap in fts.atomic_propositions:
      outputs[ap] = ap in fts.node[loc['rob']]['ap']

    # set remaining outputs
    outputs['cat'] = loc['cat'] == loc['rob'] and not outputs['cat_target']
    outputs['dog'] = (loc['dog1'] == loc['rob'] or loc['dog2'] == loc['rob']) and not outputs['dog_target']
    outputs['mouse'] = loc['mouse'] == loc['rob'] and not outputs['mouse_target']

    sys_props = controller.move(**outputs)

    # print sys_props
    action = sys_props['sys_actions']

    # Move robot and animals
    new_loc_rob = [e[1] for e in \
               fts.transitions.find(loc['rob'], 
                                    with_attr_dict={'sys_actions':action}
                                   ) \
              ][0]
    
    # Move animals
    if sys_props['yarn'] and loc['rob'] == loc['cat']:
      loc['cat'] = new_loc_rob
    if sys_props['bone'] and loc['rob'] == loc['dog1']:
      loc['dog1'] = new_loc_rob
    if sys_props['bone'] and loc['rob'] == loc['dog2']:
      loc['dog2'] = new_loc_rob
    if sys_props['flute'] and loc['rob'] == loc['mouse']:
      loc['mouse'] = new_loc_rob

    # print "time {}: moved from {} to {} by going {}".format(t, loc['rob'], new_loc_rob, action)
    
    t += 1
    loc['rob'] = new_loc_rob

    rob_x[:, t] = loc_to_xy(loc['rob'])
    cat_x[:, t] = loc_to_xy(loc['cat'])
    dog1_x[:, t] = loc_to_xy(loc['dog1'])
    dog2_x[:, t] = loc_to_xy(loc['dog2'])
    mouse_x[:, t] = loc_to_xy(loc['mouse'])


  def plot_trace(ax, xy, t_plot, xyoff, color):
    if t_plot >= xy.shape[1]:
      t_plot = xy.shape[1]-1
    ax.plot(xyoff[0]+xy[0,0], xyoff[1]+xy[1,0], marker='o', color=color)
    ax.plot(xyoff[0]+xy[0,:t_plot+1], xyoff[1]+xy[1,:t_plot+1], color=color)
    ax.plot(xyoff[0]+xy[0,t_plot], xyoff[1]+xy[1,t_plot], marker='x', color=color)

  def color_ap(ax, ap, color):
    for node, _ in fts.states.find(with_attr_dict={'ap': {ap}}):
      ax.add_patch(
        patches.Rectangle(loc_to_xy(node), 1, 1, color=color)
      )


  for t_plot in np.arange(0, Tmax, 10):

    fig = plt.figure()
    ax = fig.gca()

    ax.set_xticks(np.arange(0, 7.1, 1))
    ax.set_yticks(np.arange(0, 7.1, 1))

    color_ap(ax, 'blocked', 'black')
    color_ap(ax, 'cat_target', 'lightblue')
    color_ap(ax, 'mouse_target', 'lightgreen')
    color_ap(ax, 'dog_target', 'pink')

    plt.grid()

    plot_trace(ax, rob_x, t_plot, [0.5, 0.5], 'black')
    plot_trace(ax, cat_x, t_plot, [0.3, 0.3], 'blue')
    plot_trace(ax, mouse_x, t_plot, [0.3, 0.7], 'green')
    plot_trace(ax, dog1_x, t_plot, [0.7, 0.7], 'red')
    plot_trace(ax, dog2_x, t_plot, [0.7, 0.3], 'orange')

    plt.title('t = {}'.format(t_plot))

    plt.show()

