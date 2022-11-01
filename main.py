from cProfile import label
import gradio as gd
import uuid
import json


def create_filename():
    filename = str(uuid.uuid4())
    return filename

def create_file(topic, source, learning_goals):
    learning_goals = learning_goals.strip()
    learning_goals_list = learning_goals.split('/n')
    contents = {'topic': topic,
    'source': source,
    'learning_goals': learning_goals_list}

    filename = 'data/' + create_filename() + '.json'

    with open(filename, 'w') as f:
        f.write(json.dumps(contents))
    
    return 'file written to ' + filename

with gd.Blocks() as app:
    md = ''
    with open("instructions.md", 'r') as f:
        md = f.read()
    gd.Markdown(md)
    topic = gd.Text(label="Topic")
    source_text = gd.TextArea(label="Source text")
    learning_goals = gd.TextArea(label="Learning goals")
    output = gd.Text()
    btn = gd.Button(value="Save to dataset")
    btn.click(create_file, [topic, source_text, learning_goals], output)

app.launch()