import gradio as gr


def greet(name, is_morning, temperature):
    salutation = "Good morning" if is_morning else "Good evening"
    greeting = f"{salutation} {name}. It is {temperature} degrees today"
    celsius = (temperature - 32) * 5 / 9
    return greeting, round(celsius, 2)


demo = gr.Interface(
    fn=greet,
    inputs=["text", "checkbox", gr.Slider(0, 100)],
    outputs=["text", "number"],
)
demo.launch()


# fn: the function to wrap a UI around
# inputs: which component(s) to use for the input (e.g. "text", "image" or "audio")
# outputs: which component(s) to use for the output (e.g. "text", "image" or "label")
# demo = gr.Interface(fn=greet, inputs="text", outputs="text")
