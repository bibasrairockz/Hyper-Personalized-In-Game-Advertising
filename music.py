import torch
from transformers import AutoProcessor, MusicgenForConditionalGeneration

if torch.cuda.is_available():
    device = torch.device("cuda")
    print("GPU available. Using GPU.")
else:
    device = torch.device("cpu")
    print("GPU not available. Using CPU.")
print('first load')
processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
processor.device = device
print('second load')
model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")
model = model.to(device)
print('start gen 1')
#inputs = processor(
#text=["80s pop track with bassy drums and synth", "90s rock song with loud guitars and heavy drums"],
#padding=True,
#return_tensors="pt",
#)
print('start gen')
audio_values = model.generate(text_input="80s pop track with bassy drums and synth", do_sample=True, guidance_scale=3, max_new_tokens=256)
print('fin gen')