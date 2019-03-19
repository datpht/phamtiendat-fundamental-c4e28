from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes

colors_text = []
colors_shape = []
for i in range(len(shapes)):
    fig = shapes[i]
    colors_text.append(fig['text'])
    colors_shape.append(fig['color'])

def generate_quiz():

    text = choice(colors_text)
    color = choice(colors_shape)
    return [
                text,
                color,
                randint(0, 1) # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):
    if quiz_type == 0:
        if x in range(20,121) and y in range(60,161):
            mouse_pressing = 'blue'
        elif x in range(140,241) and y in range(60,161):
            mouse_pressing = 'red'
        elif x in range(20,121) and y in range(180,281):
            mouse_pressing = 'yellow'
        elif x in range(140,241) and y in range(180,281):
            mouse_pressing = 'green'
        if mouse_pressing == text:
            return True
        else:
            return False
    if quiz_type == 1:
        if x in range(20,121) and y in range(60,161):
            mouse_pressing = '#3F51B5'
        elif x in range(140,241) and y in range(60,161):
            mouse_pressing = '#C62828'
        elif x in range(20,121) and y in range(180,281):
            mouse_pressing = '#FFD600'
        elif x in range(140,241) and y in range(180,281):
            mouse_pressing = '#4CAF50'  

        if mouse_pressing == color :
            return True
        else:
            return False
        
    
