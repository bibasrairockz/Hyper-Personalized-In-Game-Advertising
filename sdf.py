from diffusers import StableDiffusionPipeline
import matplotlib.pyplot as plt
import torch

model_id1 = "dreamlike-art/dreamlike-diffusion-1.0"

pipe = StableDiffusionPipeline.from_pretrained(model_id1, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "Parle-G baby, buiscuit brand is Parle-G, looking cool, realistic face, wearing baby cloths, black hair, image should like a brand banner"

image = pipe(prompt).images[0]
    
print("[PROMPT]: ",prompt)
plt.imshow(image)
plt.savefig('foo.png')
plt.axis('off')
plt.show()